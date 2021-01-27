# -*-coding:utf-8-*-

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from . import SMTP_SERVER, MAL_SPL_DIR
from cls_url import URL


class emailAPTPOC:
    def __init__(self):
        try:
            self.smpt_server = smtplib.SMTP(SMTP_SERVER)
            self.smpt_server.set_debuglevel(1)
        except Exception as ex:
            return False

    def sendMail(self, _from, _to, _msg, _file):
        filename = os.path.basename(_file)
        msg = MIMEMultipart()
        msg["From"] = _from
        msg["To"] = _to
        msg['Subject'] = "{} file attach".format(filename).decode("cp949").encode("utf-8")
        msg.attach(MIMEText(_msg, "html"))

        try:
            with open(_file, "rb") as _f:
                part = MIMEApplication(
                    _f.read(),
                    Name=filename
                )
            # After the file is closed
            part['Content-Disposition'] = 'attachment; filename="{}"'.format(
                filename).decode("cp949").encode("utf-8")
            msg.attach(part)
        except Exception as ex:
            print ex
            pass

        try:
            self.smpt_server.sendmail(_from, _to, msg.as_string())
            print "send ok"
        except Exception as ex:
            print ex
            return False

    def run(self, _f, _url=None):
        mail_contents = "<h3>send mail</h3>"
        if _url is not None:
            mail_contents += "<br>" + _url
        self.sendMail('azabyo@epm.com', 'sis1220@nate.com',
                      mail_contents, os.path.join(MAL_SPL_DIR, _f))

    def __del__(self):
        self.smpt_server.quit()

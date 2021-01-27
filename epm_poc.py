# -*-coding:utf-8-*-
import os
from classes.cls_epm_poc import emailAPTPOC
from classes import MAL_SPL_DIR
from classes.cls_url import URL
from multiprocessing import Pool

def multi_run(_f):
    emailAPTPOC().run(_f)

def main(_multi=False, _multi_size=5):
    mal_url = URL.getMalURL()
    if mal_url is None:
        return

    mal_url_list = [x["_source"]["url"] for x in mal_url["hits"]["hits"]]

    if _multi is False:
        cnt = 0
        for _f in os.listdir(MAL_SPL_DIR):
            emailAPTPOC().run(_f, mal_url_list[cnt])
            cnt+=1
    else:
        file_list = os.listdir(MAL_SPL_DIR)
        p = Pool(_multi_size)
        p.map(multi_run, file_list)


if __name__ == "__main__":
    main()

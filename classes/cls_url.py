#-*-coding:utf-8-*-
import urllib2
import json

class URL:
    search_url = "http://10.250.252.103:9200/hacking_url_c2*/_search"

    def __init__(self):
        pass

    @staticmethod
    def getMalURL(_size=100):
        query_data = {
            "query":{
                "match":{
                    "data_type":"URL"
                }
            },"sort":{
                "time_insert":{
                    "order":"desc"
                }
            },
            "size" : _size,
            "_source": ["url", "time_insert"]
        }
        req = urllib2.Request(URL.search_url, json.dumps(query_data), {'content-type':'application/json'})
        try:
            res = urllib2.urlopen(req)
            return json.loads(res.read())
        except:
            return None

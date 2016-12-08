#!/home/work/.jumbo/bin/python
# -*- coding: utf-8 -*-
import multiprocessing
import urllib
import urllib2
import json
import sys 

def get_live():
    """
    直播数据
    """
    dir_path = "out/"
    filepath = dir_path + "live2.txt"
    fw = open(filepath, 'w')
    for page in range(1,100):
        #print page
        url = "http://api.open.qingting.fm/v6/media/categories/5/channels/order/0/curpage/" + str(page) + "/pagesize/100?access_token=ZTA0YTUzZDYtZDc1Ni00NTZiLTkyZWMtZWY3MjFiMTg2YWZh"
        print url
        live = do_request(url, "GET")
        #print live
        if(live):
            fw.write(live + "\n")
    fw.close()

def get_live_ca():
    """
    直播数据分类和地区
    """
    cate = '{"data":[{"id":1209,"name":"北京","sequence":14},{"id":1208,"name":"上海","sequence":15},{"id":1216,"name":"天津","sequence":16},{"id":1219,"name":"重庆","sequence":17},{"id":1215,"name":"广东","sequence":18},{"id":1212,"name":"浙江","sequence":19},{"id":1210,"name":"江苏","sequence":20},{"id":1213,"name":"湖南","sequence":21},{"id":1211,"name":"四川","sequence":22},{"id":1217,"name":"山西","sequence":24},{"id":1218,"name":"河南","sequence":25},{"id":1220,"name":"湖北","sequence":27},{"id":1221,"name":"黑龙江","sequence":28},{"id":1214,"name":"辽宁","sequence":29},{"id":1222,"name":"河北","sequence":30},{"id":1223,"name":"山东","sequence":31},{"id":1224,"name":"安徽","sequence":32},{"id":1226,"name":"福建","sequence":33},{"id":1227,"name":"广西","sequence":34},{"id":1228,"name":"贵州","sequence":35},{"id":1237,"name":"云南","sequence":36},{"id":1229,"name":"江西","sequence":37},{"id":1230,"name":"吉林","sequence":38},{"id":1241,"name":"陕西","sequence":39},{"id":1225,"name":"甘肃","sequence":39},{"id":1231,"name":"宁夏","sequence":40},{"id":1235,"name":"内蒙古","sequence":41},{"id":1234,"name":"海南","sequence":42},{"id":1233,"name":"西藏","sequence":43},{"id":1232,"name":"青海","sequence":44},{"id":1236,"name":"新疆","sequence":45},{"id":1335,"name":"新闻","sequence":1},{"id":1336,"name":"音乐","sequence":3},{"id":1337,"name":"经济","sequence":5},{"id":1338,"name":"交通","sequence":7},{"id":1520,"name":"校园","sequence":8},{"id":1339,"name":"都市","sequence":9},{"id":1340,"name":"曲艺","sequence":11},{"id":1341,"name":"体育","sequence":13},{"id":1342,"name":"综合","sequence":15},{"id":1343,"name":"生活","sequence":17},{"id":1344,"name":"文艺","sequence":19},{"id":1345,"name":"旅游","sequence":21},{"id":1347,"name":"方言","sequence":23},{"id":1774,"name":"外语","sequence":24}]}'
    cate_arr = json.loads(cate)
    print cate_arr
    dir_path = "out/"
    filepath = dir_path + "live_ca.txt"
    fw = open(filepath, 'w')
    for value in cate_arr['data']:
        for page in range(1,15):
            #print page
            url = "http://api.open.qingting.fm/v6/media/categories/5/channels/order/0/attr/" + str(value['id']) + "/curpage/" + str(page) + "/pagesize/100?access_token=ZTA0YTUzZDYtZDc1Ni00NTZiLTkyZWMtZWY3MjFiMTg2YWZh"
            print url
            live = do_request(url, "GET")
            #print live 
            if(live):
                print value['name']
                line = value['name'].encode('utf-8') + "," + live + "\n"
                print line
                fw.write(line)
    fw.close()



def do_request(url, method, params=None):
    """
    请求蜻蜓http接口
    """
    if params is not None:
        data = urllib.urlencode(params)
    if method == 'GET':
        if params is not None:
            if '?' in url: 
                url = url + '&' + data
            else:
                url = url + '?' + data
            #print url
        req = urllib2.Request(url)    
    elif method == 'POST':
        req = urllib2.Request(url, data)  
    try:    
        response = urllib2.urlopen(req)
        if response.code == 200:
            ret = response.read()
        else:
            ret = ''
    except Exception, e:    
        ret = ''
    #ret = json.loads(ret)
    data = ret
    return data
    
if __name__ == '__main__':
    #get_live()
    get_live_ca()

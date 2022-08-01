import requests     # 用来模拟浏览器发送请求
import random       # 随机数
import time         # 延迟的代码
import json         # 一种数据类型，和我们字典很类似

# 模拟浏览器所要发送的信息
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
    'cookie':'QN1=000087802eb443946740ea5e; _i=ueHd8LZNVnjXGS6Y-aC8bITDnuoX; QN57=16564897055030.7616148436862196; QN269=B8129470F78111EC9E2DFA163E03A4E8; fid=791acbe7-f40e-4e6e-941e-5b8544f0e570; QN300=s=baidu; QN99=5723; QunarGlobal=10.66.75.142_d32936_181b2a4d93f_-315c|1656560461496; QN601=208b57dd19a05a87a0feefd68135f8be; QN48=0000a3802f10439d0a70400c; QN205=s=baidu; QN277=s=baidu; QN58=1658303659191|1658305265112|8; qunar-assist={"version":"20211215173359.925","show":false,"audio":false,"speed":"middle","zomm":1,"cursor":false,"pointer":false,"bigtext":false,"overead":false,"readscreen":false,"theme":"default"}; csrfToken=W2q35iyFdWulcB2IU9IYPBuzB2ZJEhxF; QN163=0; HN1=v18eb62ccc941f0c141c6d31fc9d6946af; HN2=qurkqzczzgcur; ariaDefaultTheme=null; QN310=hrec_zaj86; ctt_june=1654604625968##iK3wWSv8VhPwawPwasvNWsTGX2PnVKvmaRWTVKDNEKt=VKX8EKv+WsD+WDamiK3siK3saKjAVRaOWSPsWS3OWhPwaUvt; _vi=L6ouUp32s8FA0VlwmC-5VIBDidcKCzds5LOvkPVs-ZxDtaHjsyOEjrxNG--htWFlmJ8a9Etjb05vN_ZxVELcSNg-hUN3Uq5tKnSgBufKlPoUNgMYR5dd6nsILQ2yfnRO4rkeufz_CWAqroSrnE-4Xy0dRdUABLP_TMC-JXfsnzRl; cs_june=09c4f80a76c806cc3f59cfbe672353b7f14cf7f57026eaf5f3b86ec80e5386b27f072a7c3e529dd4a6dfa45949de9dc307584e21d999b57f4deb7d2d4b73beeeb17c80df7eee7c02a9c1a6a5b97c117925db9139103ffeffbf03efccce726b415a737ae180251ef5be23400b098dd8ca; QN271=4aae4b20-9cd9-443f-805b-0a8d1e097d5c; QN267=0207852716902fba3ba; ctf_june=1654604625968##iK3wVRXOaUPwawPwa=fTasj8WRtOa2a8asgmWRPmaRWIVPXAaskGWDfTXSkRiK3siK3saKjAVRaOWsgmaRj+VhPwaUvt; __qt=v1|VTJGc2RHVmtYMStXTXRqTFlreUFDRkJSdjJyY3k4WG9NcTI1SUxvT3puWG5TOU1ReG5Vcmx4MGZsU3doY1BFcUdLNnY1T3V6Tm1IeGRMTlZ5NHZmRTBMT0hwSVRhbU85Z2o4V290QndneWFMT1FEL25VR05SR0tYVXJ2OWRycUx0ZmNudzY1ZlR2RWhTcDhBWXd5Y3RoOWN6WEh0bWp3ZE8vU1VRVlBkU0wwPQ==|1658367780978|VTJGc2RHVmtYMTlyWC92UzBDRmxzekN6UitxZ0xYWTcxVVdQcEpFZC9IQXY5M1B6MWVaT0VJQ3U1eTl1aHF1M084S1BITVJIK2ZuOHlKZnJRQStJeWc9PQ==|VTJGc2RHVmtYMStTVkorN1cyc1h5Z1BNRms5UjhRQ2hVdFo3dk05cElwVVRKMWkzdEJMbVFBSTRCQ2c3UXNaRTJ2SUdMZmFPZWVOS3hjanRtQlR2OVhEMm9ESTZzTkhsTHpoU09IS2pEU3dMaWxOeHE0VHdTZkhWbURGSTVnSWR4RmdJeVNTbWhhNXhEZlU3Q1ROeDdmdmt1UDVFMGIzc2xMbzl2cDN3VXVyakJFSjc0YStISERYeVgrZzFrdmdzYXhmWGZPUTRyOWpXOG8yM1ZvWUJMU0FjbnVibTZBeFdRTno0ZG9QN2hqQzlnVnJPSXVKVk13OXo2SUtqQkorb3UxbWxrTkhBRFRDSGs3KzVyMTBUdlFWckY4L0EvRXl4QUtBRDRWNENaYUNhQlJkL1haMThmcGJuUDNSUzJPbndxZmtJbGVFRUljVDFwRWNSZzJxdVJ3TUJMLzRIM0NCYWtER1FEUHY2bVd0YWsvUjlrTFpjcjBsQ0g1ZldBZGZ4Tnl3RTdJaTZsSTNjK1o4RmNiWVJ2VytHVElmVXlYSGVoQ1RpQ3Z4SEdGSWRXL20xZ1JwaXVldExWR1RQbTJZQk15anhPc05YZVZFcmpENXJrY1BDVzdQUjg5RzBIaUxoSDhzbTY4MXM4K2FCRllzNFprYmdDaHRaMnNmWllZdVNyR002bEtDaEg0aUNoVVRkWXR1RDI2ak5aK0lpTHRaUWRzMkduQkIzZHRNZWpCUVVjUkZ3TTVmWEJxTm9MWFVuTExtQ085QVp1MHVEQTRtQmEyZXdpaENKbTFIWVpCNldaSjBEd2ZqSXdNUkZOeFJna1UvSm1FZUMxUTNjVzRKd3dZZ0lFMTNjRjNKWnpGR21VQmM4ajNFYWRWWUVCNmNqWGJkS29JbWtNdkE9'
}

# 创建函数 用来获取数据
def crwal_tickets():
    i = 1

    while i<5:
        # 我们要抓取的网页数据的地址
        url = 'https://hotel.qunar.com/napi/ugcCmtList?hotelSeq=beijing_city_3183&page=1&onlyGuru=false&rate=all&sort=hot'

        # 请求对应的url的数据，并且把成功返回的数据存储在变量response中
        response = requests.get(url=url,headers=headers)
        # 对返回的内容使用text文本的方式进行解析，此时得到的就是一个json字符串
        html = response.text
        # print(html)

        # 此时数据已经获取，只需要分解出我们所需要的数据即可
        content = json.loads(html).get('data')
        print(content)
        commentList = content.get('list')
        print(commentList)

        #使用循环来获取景点列表
        for c in commentList:
            # 获取景点名
            content = c.get('content')
            print(content)      # content是一个Json格式字符串
            content_json = json.loads(content)  # 来解析json格式字符串
            print(type(content_json))
            feedContent = content_json.get('feedContent')
            print(feedContent)
            # # 获取景点星级
            # star = s.ge   t('star')
            # # 获取景点的分数
            # score = s.get('score')
            # 创建新的空字典用来存储数据
            my_dict = {}
            my_dict['feedContent'] = feedContent
            # my_dict['star'] = star
            # my_dict['score'] = score
            # print(my_dict)

            # 将数据持久化到文件中
            with open('comment.txt','a',encoding='utf-8') as f:
                f.write(str(my_dict)+"\n")

        i = i+1
        time.sleep(random.randint(10,20))

crwal_tickets()

























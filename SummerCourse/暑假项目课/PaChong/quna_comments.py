import json
import requests
import time
import random

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'cookie': 'SECKEY_ABVK=8TGriI+rPPKKNpd/ZzKhzohyyUkhYxHtKaLaUwr/FIc%3D; BMAP_SECKEY=o9Ezc68ZlgkY5LzTBhazdklyg9fQTVLvql5yzn8JsLiRdZLo7SSCzR1zmlK6DzZYblNG8AuSFFkiW7k4X3XjuNqprot3l4341ywGQcmFM343Rskjs0I7SeKuD4ZdJRYnJ3XYR_UxJf-rsGF2MLHytQi3YwVO8dJX88W_DHod3-I0jeTnXCTg9Ooyl4mxCAnT; QN1=00009180306c431f9600e62f; QN300=s%3Dbaidu; QN99=3515; QunarGlobal=10.66.75.142_d32936_1817550e3fb_1e2f|1655532736626; QN205=s%3Dbaidu; QN277=s%3Dbaidu; _i=DFiEZCZf68wwiVdetlJNVTN1DBvw; QN601=553727872ec2342d4419d1c82effc5a2; QN269=9AFFE250EECD11EC87DAFA163E9C4675; QN48=00008c802f10431f96105120; fid=10b6fe31-57f1-4df0-bd2f-9e45d269935e; QN243=10; ariaDefaultTheme=null; QN57=16555328340560.7386042760776945; QN63=%E5%8D%97%E4%BA%AC; QN71="MjE4Ljk0LjExNy4xNDY65Y2X5LqsOjE="; qunar-assist={%22version%22:%2220211215173359.925%22%2C%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false%2C%22readscreen%22:false%2C%22theme%22:%22default%22}; csrfToken=XdmuDDZXSULUmwblygpdqgcrnjKk44dY; Hm_lvt_15577700f8ecddb1a927813c81166ade=1655532835,1656174763; _vi=gnMkKkmRU5rX2s0E4F6dBieysGpi7HpK--0tRnwZ2ttA860ADdRIBhJII3vs02Pa8w1_YkEnPVdBEaT7i0At67LLWpemzRaGrZtsuySGPAsdtqTTYddbqvUJrp66sguSBn7e3eBQk83u6838yJSrs9StG5AJnogX2Rmwo_gqNGcu; QN267=667914800b9e940a1; QN67=1474%2C11289%2C6330; QN58=1656183238819%7C1656183268703%7C2; Hm_lpvt_15577700f8ecddb1a927813c81166ade=1656183269; QN271=1bfd1289-a2a7-4694-ad93-80c3ddb3ed0b; JSESSIONID=B280185CCF5726D65628DF87B42C2D68; __qt=v1%7CVTJGc2RHVmtYMStnOW1aWnU2UXpoNERreWFlbU5wdTJqUUY5bzh3Sjh1MVNVMTdjQnBQQWtsbEIySlY2ZEdPb1BpbHRkeWNmVFdHS25uYWhXS1NVeGlLOTdQNGVVQ0JzUmd1Q0tZbXRSVFY4cWxURktlMDZqY1E2c0dvZ3ZQZEF3K1lLUmdvSXBneWpUT1NyRGJMQ09wYlR3Z3FiWnk2dXVTSmlya2c4S0V3PQ%3D%3D%7C1656183367109%7CVTJGc2RHVmtYMSs0OVVQb0xCSkxZdjNuSzZvUXRyby92cS9jUzFlZlRhd1FIOW1vZmQ1M2R1SVd2U1ZHQ1kzN01jRm5KMERpREhyUk90YXA5UVdIM1E9PQ%3D%3D%7CVTJGc2RHVmtYMStaUlFZNnJVNEp3a1p4VkFac2ZFNWphNWxqa1FOMUJjYXp0dU8rTmVxQ2txaW9majFndFk1TXQ2c2JmbjRIUzNjZVh4U205RERBUUpXZVB1d1FPbGtxRG5QdndLM3ozNEtCZ0t1cUcyRnRNZGxhYVFFNmREb1ZSMEFTUFdmRGhud3NENHZrdnMrMXJhNFpxY0c3YzhGTlRYeUlkK2ZaYjE3UnpwbllZSWJiZW1PVzNyUVVtV1lSd2RZNUxLSVR5WEM4Uy9kMG1jRmd1eFpVQkxyRzFIamswQkVDUTVXMm0rclBTeXppMFErQzRVSWM3ZitQSHpLK2Z4RldpOGtWYXJGYlhoQ05QZVhmSmpvVUMxbkNQbWlzUUwvMCs2U3pTczROOWUrT1k4eGhqMjRjeDJqWkp4YUlSckQ5S2k1WElRZmVibVJpdjUzQnRsVUtac0dYblE1Qm9ZSjdCeTZpMGVicnA0Q3ZmT0xoN0lzRHpQSk9TTitRSHJXVW5neGRyU21OMUo1emU1amxMSE9qbmJkdkd4OENzUU5FMURTd29Rc0MyL0hEZE9EU2gzTThINm5XcFNUaTB0aEdUT2h3ZXA3TnNLSlAwNXJicSt4OEtIQmNlUVZGbFl6eTFySFJRN2JIK3JTTmpZMVdxOW93aWt6U1pvWm93M01ZZHZzWmVLR0hVSm5VcDNPT243SlRhQnkvTkxTSlpvZTQ2ODEwWU1HR0JDRHJ6WklNQnhsMVA2TWhJdmRQam5PNkh2MVc5YVd6cWcxcW9HT0c1SXRFWWVMS0lLbHQrUHE2TmhjaVZVWC95eEZHUWtxTzRMeUdHM2hhc3FoT1prWDk5SkxwOXJ3dm81c0dOdkhDYUZENTJ5Mm5RRTV0d2ZaaWhMQ2dhelNrdk5Yb3FOVERISGNYckZSZWJIRk1NdHR1a3phclNSR2ZQMkdzcDlWQzVwTVp1YjBLQVVCTEZSMWo1b0FSdWR4aXRRelNWU1RLV3FVQjJpNVN0SGdqbUtsdy9Wb053QXU3MGN6RjcrVXB2eHl4c2tUKzlnYUNUUWZ6emxQVnZGND0%3D'
}


def crawl_comments():
    num = 1

    while num < 9:
        # 通过网页分析找到景点评论的数据接口
#        url = 'https://piao.qunar.com/ticket/detailLight/sightCommentList.json?sightId=1474&index=' + str(num)
        url = 'https://piao.qunar.com/ticket/detailLight/sightCommentList.json?sightId=457472&index='+str(num)+'&page=1&pageSize=10&tagType=0'
        # 请求对应url的数据，并且把成功返回的数据存储在response中
        response = requests.get(url=url, headers=headers)

        # response.text 返回的是一个 unicode 型的文本数据
        html = response.text
        print(html)
        # 解析有效的JSON字符串并将其转换为Python字典,并获取data键对应的值

        data = json.loads(html).get('data')

        # 获取评论列表
        commentsList = data.get('commentList')

        # 遍历评论列表
        for c in commentsList:
            author = c.get('author')  # 获取用户昵称
            content = c.get('content')  # 获取评论内容

            # 去掉无意义的评论
            if content == '用户未点评，系统默认好评。':
                continue

            # 创建空字典存储我们想要的数据
            dict = {}
            dict['author'] = author
            dict['content'] = content
            print(dict)

            with open('comments.txt', 'a', encoding='utf-8') as f:
                # f.write(json.dumps(dict['content']).encode('utf-8').decode('unicode_escape') + '\n')
                f.write(str(dict['content'])+'\n')
            time.sleep(random.randint(1, 2))

        num += 1
        time.sleep(random.randint(3, 6))


crawl_comments()

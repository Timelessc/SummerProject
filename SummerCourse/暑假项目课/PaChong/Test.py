


# 首先定义header
import json
import requests

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'cookie': 'SECKEY_ABVK=gwdvvYFOIuaja04IjyvsPnGqs3me6f30SoUyDcu2FhM%3D; BMAP_SECKEY=gwdvvYFOIuaja04IjyvsPi2ZJcYDWS1Jkoc0rngvAKNwQmp1zcnowrl1c0yFEuIix222vaZI9MHHlb8LBmYQ_BuDiodKPPc_SvjG4Ij70viBhv7YwoqrBtwK4CY9LjKzcOnOLxrFuWqJi7JfyC3O0Iv85f822G3iJgr-0lk6EaZuQI1cEPjgulEkrCViqA0a; QN1=000087802eb443946740ea5e; _i=ueHd8LZNVnjXGS6Y-aC8bITDnuoX; QN57=16564897055030.7616148436862196; QN269=B8129470F78111EC9E2DFA163E03A4E8; fid=791acbe7-f40e-4e6e-941e-5b8544f0e570; QN300=s%3Dbaidu; QN99=5723; QunarGlobal=10.66.75.142_d32936_181b2a4d93f_-315c|1656560461496; QN601=208b57dd19a05a87a0feefd68135f8be; QN48=0000a3802f10439d0a70400c; QN63=%E5%8D%97%E4%BA%AC%7C%E5%8C%97%E4%BA%AC; QN205=s%3Dbaidu; QN277=s%3Dbaidu; QN71=MTIxLjIyNS4xMzUuMTU0OuWNl+S6rDox; QN67=11289%2C507956; qunar-assist={%22version%22:%2220211215173359.925%22%2C%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false%2C%22readscreen%22:false%2C%22theme%22:%22default%22}; csrfToken=T6zZtEnZ7aD7YTzN547KC5PGvf3E56gU; _vi=aK-EkTPdCdZBzKj0FGzMUX7pJTDzlIOg3ew6nb6F0Vh5l69tnWYg6pdsfp0G6x8iecvG2l60UHetKjBBpajeShnyZRsoXpL6vV-kLFz6tYlYxCVto-bPepJAUhoYkEp27qDcetOI3MmLx-OB-JLgQ6E05gEba4vLNSyWcPMl7WZM; QN163=0; Hm_lvt_15577700f8ecddb1a927813c81166ade=1656560468,1656811516,1657449745,1657505428; QN267=020785271696d903fd9; ariaDefaultTheme=undefined; QN58=1657505428165%7C1657505547575%7C5; Hm_lpvt_15577700f8ecddb1a927813c81166ade=1657505548; QN271=678b99c0-7c7b-43d2-bfb2-1d1166d2c4dd; JSESSIONID=C65F251B3FF873C55BD1ADDC76FBFFC1; __qt=v1%7CVTJGc2RHVmtYMSs3RVFMSW5RdlFaN2wyNnhGMjFiZHl1VFZENCtpUVZtSUN0UkM4R3dyWFp5LzgvQWZmTDIrNFNSdVZwSTlHOEJJNlYxVjk3ZHk2OUtNRFA3Y2lLZUR0MjNxMjA0L00zd0d1UG9XK1NpSHB1ZjRVUFp1UmxkWVVxS3VxVVQ1ZzNwVERmc2VQMkNkYTJBPT0%3D%7C1657505556172%7CVTJGc2RHVmtYMTh6U1BqT1M1cU1IaHJ6MFg3MXFhTml5em1yQ1RwQnZXUHNva0xXdDF5aTM0YTJHM2xia3phbnN5dmNzbU5MaXd3Ulp4alBYdW5kQ2c9PQ%3D%3D%7CVTJGc2RHVmtYMStXUVhTU3FObXFMODIxZHdFQjYvZGJoU3MyNHRaeE5iM2l3TXp5R2cvMHg0dlA2L1U0TWMzNG5tR1NVdDBSaDRJR2hPVVdtZ01WbkJFcGdpNiswUnZSbzhBeVBZblo4RURoZHQyV2htVC8yRERKRDFnZGg3M29yWGt4ekNNQnplYVF5NFdmQS9xb2R5OWZnK1p5ejhtQWg5cEtHekFZUFRsOVBwRlFkOE9lRm9ZZEs5b3hQSWJsM05mZVNxVjBQRXBQUnNkZjAxeTNuWkdVUWxsbmpUaEY3NTZMTkx6ZUhGSVZ5ZGlZT0prRXJtME4wQncvWFp5cVVvcmE5VjhRZjI5R2lndnVLT2tYVlBTY1A1NXJJYzRRMk9mc0FuSE1NbW91YU44N1d4VWVCZS9QeHNkMitkdUswOXFlRmZEUEduUm0xUDduWmRoUndEYmRjODNZbXN4QzNZREJvcnpWNlZ1OFpiT3V6cSt1ek0zcGgrV25hZndGYm5wMWFCWjJucGV0b1I0enNGbTFTVnZub2ZjNkFSdzJPa2ZZOTNXdjlWMFJEMlMrNFl5U0twejVWb2lNekEvbys4YWVKMklOWllTWE04YmppeWhVOGswVG9vdGQ0Nm1od0JSL2pLNzM3TkZaeWRIWHNub3oreW5ZZEtRNjU2QndtTlI5dkI2T3BPMzlTMWVnZnd3eUJ1UVZWUVY5bFp4MG92NVdhSFM0bGkwMW0yYWVPUlp4VWh4S0p2RHRLbXdVdmgvaGJvU3pDOGJrVzBGV1hubUw3VFdjQ2Y4aEljdWNKUnBxRTVzNlR2QW41SXV6aXpaR0dUQWJiVnl6dXkyY1ZGK3AzRDNFZ2dOU0dPem9NVXRnWTVWYkkvUHM2L1JORnZBYkZFSzBGbGNhbGJMYzVYbXJnYXJyTGQ2Rk42RnZkMHhJUFcxQlBBcHQrUXFEVVIxNmtYckJQOHo4aGRpeDJlZ2lZNjkzQ2p0K2NMazBpbTJvTk1WVXF4VlVNR295NVlhMnZTRzRYdVk2YnEveGQ0MlFFVEI5djhKVGxORkV2b3BDdlhlUHVaZnBHUmZZdzU2MVV4ck1rMWtTbEwvSw%3D%3D'
}

# 定爬虫方法
def crawl_tickets():
    i = 1       # 定义页数，我们可以爬取多个页面

    while i<2:  # 循环爬取

        url = 'https://piao.qunar.com/ticket/list.json?from=mpshouye_hotdest_more&keyword=%E5%8D%97%E4%BA%AC&page=2'

        # 通过requests向浏览器发送请求信息，将返回的数据存储在response中
        response = requests.get(url=url, headers=header)
        # 对response进行解析,此时获得的就是一个json字符串
        html = response.text

        # 对json字符串进行解析，并获取其中的data对应的值,此时得到的值就是一个字典
        content = json.loads(html).get('data')
        print(content)
        # 获取景点列表
        sightList = content.get('sightList')

        # 使用for循环遍历景点列表，并将其加入到一个字典中
        for s in sightList:
            sightName = s.get('sightName')   # 获取景点的名字
            star = s.get('star')        # 获取景点的星级
            score = s.get('score')      # 获取星级

            # 创建一个空的字典
            my_dict = {}
            my_dict['sightName'] = sightName
            my_dict['star'] = star
            my_dict['score'] = score
            print(my_dict)

            # 将字典写入到一个文件中
            with open('tickets.txt','a',encoding='utf-8') as f:
                f.write(str(my_dict)+'\n')
        i+=1

crawl_tickets()


import json
import requests
import time
import random

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
 #   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
 #   'cookie': 'SECKEY_ABVK=8TGriI+rPPKKNpd/ZzKhzgAR0kvyXVJf79+EBEcGApc%3D; BMAP_SECKEY=o9Ezc68ZlgkY5LzTBhazdo4rlNWuJrGRaI1rOvXIF2mgGcRi5zonOTozF_BXi3LsQhg7Ehxyq4amfuNf3qt93r_Ff18nlxTEIqoe4JamUqScJT6fDUtUTMi8Tac9SRuZzSVSw6xi8kbTZXHi-4O9cQWUV_RFjmt6-tiFT6MbQ53ZFnn9whnBU6ycvCfix4b-; QN1=00009180306c431f9600e62f; QN300=s%3Dbaidu; QN99=3515; QunarGlobal=10.66.75.142_d32936_1817550e3fb_1e2f|1655532736626; QN205=s%3Dbaidu; QN277=s%3Dbaidu; _i=DFiEZCZf68wwiVdetlJNVTN1DBvw; QN601=553727872ec2342d4419d1c82effc5a2; QN269=9AFFE250EECD11EC87DAFA163E9C4675; QN48=00008c802f10431f96105120; fid=10b6fe31-57f1-4df0-bd2f-9e45d269935e; QN243=10; ariaDefaultTheme=null; QN57=16555328340560.7386042760776945; QN63=%E5%8D%97%E4%BA%AC; QN67=6330; QN71="MjE4Ljk0LjExNy4xNDY65Y2X5LqsOjE="; qunar-assist={%22version%22:%2220211215173359.925%22%2C%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false%2C%22readscreen%22:false%2C%22theme%22:%22default%22}; csrfToken=XdmuDDZXSULUmwblygpdqgcrnjKk44dY; _vi=pzv8zEGe_ZMvmB-jpAS5wdnylSwcHZnTk65EJ6gfuw_TTf8izHR9nDQdHITov_4osE1LY_yJCCPgOewtnHAg7NvQFP-KqqTzQMn7IMAye2rndb2iEPHK9YMEytbtt77Lxa3IOtbhJ32ofsU9pmc69u0fwCFPNqwjE-9So79g0orh; Hm_lvt_15577700f8ecddb1a927813c81166ade=1655532835,1656174763; QN267=6679148002d52cb41; QN58=1656174759521%7C1656175392582%7C3; Hm_lpvt_15577700f8ecddb1a927813c81166ade=1656175393; QN271=54c488bd-9232-483e-8903-2c525a049d7d; JSESSIONID=809DFA07E4B69D79B722468A40BEC9ED; __qt=v1%7CVTJGc2RHVmtYMSs0KytYWlhaYnZ6dzkweGYxcDVUeFJDYlVWQVZIRDl4L3NsRUFySlFyWURkTUhXN2NkMTNPNGl3RC94QzJ1UTRPRVdPbmlUNUJoTjFjcWFXZUFYeXBkR0RJUHl6UDF5Zk9WeXY0ckI0WndiSWt4dDN0c1RpeE8wVUc3MDJqb2lmc0lySHJveW90dUpvaWE3YmlhMnRVOHYxdlRpSUFTb2ljPQ%3D%3D%7C1656175433871%7CVTJGc2RHVmtYMStybk41QVlrVU54SE1vcVU0Tm9JV3NscDZlZUJJell2aUpHeUI5THVlQk5kTjNjdlVzZTV5eHl1ME9PenNKeDNuR0FoVlh2U2ZuMXc9PQ%3D%3D%7CVTJGc2RHVmtYMSs3M3FZcHI0cEhxR2RxVkRyMDlpQldoN05vYWlXK001MEN4NWJVTnZRWFJoOFVXWmZkcGQ4b3hVRmNLOUEwTDlLSFBZNFJhQkZIM2JLaTNPR2VseVo4Q21PWHhvUm8rY0ZFS0VBNXF5bnhsNnRGSUZlYjNPT1Z5UUZpNnIwSjJ5RlNpK0ZqTlgyNTBCSGErQkRZRGE3ZjVMZGY2ckwxRDFHVmpFSkJNaCtjWThqTUlnZkJQK250cDAwdmxBN2JyWEUyWk9hVE91TzBPa21URjdjOXlIU0VTb0ROalMybUQrcGdYVVE1SFFvaGw5M0ROQ3J2VWRvV2llaGRhdnNLN1ZvaFNlbEp6S21qdHQrRXZwOWpqZFBYRHZOSWVtT1VpTGY0VUFaajlodmtaVGp1Z0xXYXpESThscVhkdXhQNkcvWXZrRFlQVFZUNTI3WDE5YkxlMVl6MjNmWG1iWitYU1liSGpDdHUrZlUrU3U4WFc1TTlyc0liSGpBOENVUUxwbVF4bUIxV3l3UlU5MFRSTnNGNVhGeEpZQm10NXF4ZG9QdzlNSWtlODFHelJuVnF2MjVsUktaSHlWQnNiTWNsTmZLUjFDZVNZRE9DSlphaTl2UnJrUjNvSHo3V3ZJWHRBWExDZXhtZWtiZUJsTzM2N3FVMjRtRzFJTUN0dG9DUlIxbDMvbVF2QVlTOE95anRnN3ZzbW5SNlA1OURSQUZKNEk1MXBvTlc4RWtsVmwrbXNzY1JFSk5pQ3ZFWGlHNi9VMU5wY3Y0TGRqTFFjSk5EcFVZejVnZ09EbmkyRVR6cUI2SFlSMVdnZWk0elVmR1VKbkU0VzErM3hnQjY2WlZjcUdlUUIrYm5hZEtNbHAyMTJBd3VaZkF5N0R6eW90d2Q5MllrT0RscXFoS0Jod3hoNHVLZTcyOERCWTN4M1JsL3VwSGp4QTNkaFBBL3FzZ096T2RJNmEwdFBRMTF5U3FUVmszYnN5ZFZGanNtSGlCTUFtU1VXeXAxUHd2dEdxdWdHSVliUXp4OEhOZ1BCdnE3aSsvQ2tXdGZmQVZRc0p2UGtsWT0%3D'

    'cookie':'SECKEY_ABVK=gwdvvYFOIuaja04IjyvsPnGqs3me6f30SoUyDcu2FhM%3D; BMAP_SECKEY=gwdvvYFOIuaja04IjyvsPi2ZJcYDWS1Jkoc0rngvAKNwQmp1zcnowrl1c0yFEuIix222vaZI9MHHlb8LBmYQ_BuDiodKPPc_SvjG4Ij70viBhv7YwoqrBtwK4CY9LjKzcOnOLxrFuWqJi7JfyC3O0Iv85f822G3iJgr-0lk6EaZuQI1cEPjgulEkrCViqA0a; QN1=000087802eb443946740ea5e; _i=ueHd8LZNVnjXGS6Y-aC8bITDnuoX; QN57=16564897055030.7616148436862196; QN269=B8129470F78111EC9E2DFA163E03A4E8; fid=791acbe7-f40e-4e6e-941e-5b8544f0e570; QN300=s%3Dbaidu; QN99=5723; QunarGlobal=10.66.75.142_d32936_181b2a4d93f_-315c|1656560461496; QN601=208b57dd19a05a87a0feefd68135f8be; QN48=0000a3802f10439d0a70400c; QN63=%E5%8D%97%E4%BA%AC%7C%E5%8C%97%E4%BA%AC; QN205=s%3Dbaidu; QN277=s%3Dbaidu; QN71=MTIxLjIyNS4xMzUuMTU0OuWNl+S6rDox; QN67=11289%2C507956; qunar-assist={%22version%22:%2220211215173359.925%22%2C%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false%2C%22readscreen%22:false%2C%22theme%22:%22default%22}; csrfToken=T6zZtEnZ7aD7YTzN547KC5PGvf3E56gU; _vi=aK-EkTPdCdZBzKj0FGzMUX7pJTDzlIOg3ew6nb6F0Vh5l69tnWYg6pdsfp0G6x8iecvG2l60UHetKjBBpajeShnyZRsoXpL6vV-kLFz6tYlYxCVto-bPepJAUhoYkEp27qDcetOI3MmLx-OB-JLgQ6E05gEba4vLNSyWcPMl7WZM; QN163=0; Hm_lvt_15577700f8ecddb1a927813c81166ade=1656560468,1656811516,1657449745,1657505428; QN267=020785271696d903fd9; ariaDefaultTheme=undefined; QN58=1657505428165%7C1657505547575%7C5; Hm_lpvt_15577700f8ecddb1a927813c81166ade=1657505548; QN271=678b99c0-7c7b-43d2-bfb2-1d1166d2c4dd; JSESSIONID=C65F251B3FF873C55BD1ADDC76FBFFC1; __qt=v1%7CVTJGc2RHVmtYMSs3RVFMSW5RdlFaN2wyNnhGMjFiZHl1VFZENCtpUVZtSUN0UkM4R3dyWFp5LzgvQWZmTDIrNFNSdVZwSTlHOEJJNlYxVjk3ZHk2OUtNRFA3Y2lLZUR0MjNxMjA0L00zd0d1UG9XK1NpSHB1ZjRVUFp1UmxkWVVxS3VxVVQ1ZzNwVERmc2VQMkNkYTJBPT0%3D%7C1657505556172%7CVTJGc2RHVmtYMTh6U1BqT1M1cU1IaHJ6MFg3MXFhTml5em1yQ1RwQnZXUHNva0xXdDF5aTM0YTJHM2xia3phbnN5dmNzbU5MaXd3Ulp4alBYdW5kQ2c9PQ%3D%3D%7CVTJGc2RHVmtYMStXUVhTU3FObXFMODIxZHdFQjYvZGJoU3MyNHRaeE5iM2l3TXp5R2cvMHg0dlA2L1U0TWMzNG5tR1NVdDBSaDRJR2hPVVdtZ01WbkJFcGdpNiswUnZSbzhBeVBZblo4RURoZHQyV2htVC8yRERKRDFnZGg3M29yWGt4ekNNQnplYVF5NFdmQS9xb2R5OWZnK1p5ejhtQWg5cEtHekFZUFRsOVBwRlFkOE9lRm9ZZEs5b3hQSWJsM05mZVNxVjBQRXBQUnNkZjAxeTNuWkdVUWxsbmpUaEY3NTZMTkx6ZUhGSVZ5ZGlZT0prRXJtME4wQncvWFp5cVVvcmE5VjhRZjI5R2lndnVLT2tYVlBTY1A1NXJJYzRRMk9mc0FuSE1NbW91YU44N1d4VWVCZS9QeHNkMitkdUswOXFlRmZEUEduUm0xUDduWmRoUndEYmRjODNZbXN4QzNZREJvcnpWNlZ1OFpiT3V6cSt1ek0zcGgrV25hZndGYm5wMWFCWjJucGV0b1I0enNGbTFTVnZub2ZjNkFSdzJPa2ZZOTNXdjlWMFJEMlMrNFl5U0twejVWb2lNekEvbys4YWVKMklOWllTWE04YmppeWhVOGswVG9vdGQ0Nm1od0JSL2pLNzM3TkZaeWRIWHNub3oreW5ZZEtRNjU2QndtTlI5dkI2T3BPMzlTMWVnZnd3eUJ1UVZWUVY5bFp4MG92NVdhSFM0bGkwMW0yYWVPUlp4VWh4S0p2RHRLbXdVdmgvaGJvU3pDOGJrVzBGV1hubUw3VFdjQ2Y4aEljdWNKUnBxRTVzNlR2QW41SXV6aXpaR0dUQWJiVnl6dXkyY1ZGK3AzRDNFZ2dOU0dPem9NVXRnWTVWYkkvUHM2L1JORnZBYkZFSzBGbGNhbGJMYzVYbXJnYXJyTGQ2Rk42RnZkMHhJUFcxQlBBcHQrUXFEVVIxNmtYckJQOHo4aGRpeDJlZ2lZNjkzQ2p0K2NMazBpbTJvTk1WVXF4VlVNR295NVlhMnZTRzRYdVk2YnEveGQ0MlFFVEI5djhKVGxORkV2b3BDdlhlUHVaZnBHUmZZdzU2MVV4ck1rMWtTbEwvSw%3D%3D'
}


def crawl_tickets():
    i = 1

    while i < 2:
        # 通过网页分析找到数据接口
       # url = 'https://piao.qunar.com/ticket/list.json?from=mps_search_suggest_h&keyword=%E5%8D%97%E4%BA%AC&page=2'
        url = 'https://piao.qunar.com/ticket/list.json?from=mpshouye_hotdest_more&keyword=%E5%8D%97%E4%BA%AC&page=2'
        # 请求对应url的数据，并且把成功返回的数据存储在response中
        response = requests.get(url=url, headers=headers)

        # response.text 返回的是一个 unicode 型的文本数据
        html = response.text       # 对返回的文本使用text的方式进行解析,此时 得到的就是一个json字符串
        print(html)
        # 解析有效的JSON字符串并将其转换为Python字典,并获取data键对应的值
        # 对json字符串进行解析，就需要使用json.loads()，并获取打他键对应的值
        content = json.loads(html).get('data')
        print(content)      # 得到的是一个字典

        # # 获取景点列表
        sightList = content.get('sightList')
        # 遍历景点列表
        for s in sightList:
            sightName = s.get('sightName')  # 获取景点名称
            star = s.get('star')  # 获取星级
            score = s.get('score')  # 获取星级

            # 创建空字典存储我们想要的数据
            dict = {}
            dict['sightName'] = sightName
            dict['star'] = star
            dict['score'] = score
            print(dict)

            with open('tickets.txt', 'a', encoding='utf-8') as f:
                # f.write(json.dumps(dict).encode('utf-8').decode('unicode_escape') + '\n')
                f.write(str(dict)+'\n')

        i += 1
        time.sleep(random.randint(10, 20))


crawl_tickets()

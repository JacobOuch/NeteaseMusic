import requests
import js2py
from copyheaders import headers_raw_to_dict

def params_and_Seckey():
    result = {}

    return result

headers = headers_raw_to_dict(b'''
# :authority: music.163.com
# :method: POST
# :path: /weapi/playlist/manipulate/tracks?csrf_token=bc5475e560cb2023ad355da57937c2f3
# :scheme: https
accept: */*
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9,en;q=0.8
content-length: 576
content-type: application/x-www-form-urlencoded
cookie: _ga=GA1.1.1048729511.1629103325; Qs_lvt_382223=1629103325; Qs_pv_382223=459897220871502800; _ntes_nnid=cd03c58fb5fcdff26dca50bfad3dbc5e,1629103325602; _ntes_nuid=cd03c58fb5fcdff26dca50bfad3dbc5e; _clck=155jmxr|1|etx; _ga_C6TGHFPQ1H=GS1.1.1629103325.1.0.1629103332.0; vinfo_n_f_l_n3=7f460ce273df2509.1.0.1630494303935.0.1630494603171; _iuqxldmzr_=32; NMTID=00OelitiKEzgGo2a0t8iXe3XiUquxkAAAF-0l68vA; WEVNSM=1.0.0; WNMCID=spenol.1644206933788.01.0; WM_TID=4RYz%2FUdEY09AUEFUABY%2FoO1Koi2axpK9; WM_NI=trtJFdDrEbgS9gh4t6imeCY9%2BNJgRH2GEPuISkQzDvwAHgc4QMeu95%2BK5pRkYXA9J9wLNsrOtiVT%2B1I7fW6rvdB25DfN52gkO4GyrcNFH1E0dozwk%2BRmiWtEIu8QpVIYREo%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee89d87df48882d0cc3f81ef8ea3d44f969e9fafaa7b89bc82aff162f386a5d7ef2af0fea7c3b92ab8aebcabc57088ae8b83e659fbb9a8d5f73eabb3aba4dc33e9928688d144f2998bb1f84391b59f9bc77eb59f8888e2409393ab96bc3fe995fb91d1619b888fdac933b5948294f145b8b79ab5aa3b8be9aab8b57ab6bc8ed3b850a692fbd3e6618dec899af1698e9a88d2c83ca8b1b698ea2192b3a7b8f74f8babf8b2f35e8b879ea6ee37e2a3; MUSIC_U=f189b537ee5001b24663937178cbfd7995148c9f4bf89ca87ec550beffe3408e519e07624a9f0053d78b6050a17a35e705925a4e6992f61dfe3f0151024f9e31; __csrf=bc5475e560cb2023ad355da57937c2f3; ntes_kaola_ad=1; JSESSIONID-WYYY=Km%2Fy9AO%2B%2BVY9fpbTy%2F8qtnkZNpIAmnA2eMCk05rt3vKminzSfOpflJy%5CX3eznsZ%2FzuCIgK2%2Bbeoup%2FZZFf5SncsxKaquAvrAMp51YvQ28GexU1KIIZntHQ9RTn95GBrcuiQll6YhK5Tz%2Fi8gkvTQFh3nScwp2DA%2FDekh4TAYyGZ5uPZK%3A1644224619057
nm-gcore-status: 1
origin: https://music.163.com
referer: https://music.163.com/my/
sec-ch-ua: " Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
sec-fetch-dest: empty
sec-fetch-mode: cors
sec-fetch-site: same-origin
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36
''')

data = {
    'params': "/04CNL9p6kzvWaQ+waPEIRfwZAGZHRYc8ipI/xtTWRcGnjqhDL+/GHuktox/v2wwYN4K3q94DnDqHgngYNNK32E1vINS7CQEVaExj8vr9CBw38jQcL/EKPL+ND1zEYvSs8G/Yhp8QD021xSWr/1ZdXtFjgLhkXtt/1WCzcAoZsQWIHkCjGxf9+mH3/6ECJdu6QZTn8j9RiHo6VtGp9LHBA9R8WKH8GACSqgLBp71HpjCQ/OwQasAEj6PPgrfnOCDhOVMu2060qzD1L4VpCPMvQ==",
    'encSecKey': "d2dc89feb96ae7cd403acc9c949a3120d07c99158b2395caf2e2336861461d1298ea3649a7bd6ed4a1dea1359310d4c3fe08a3f73da123a472fb07d7a50ceb504a65b04cd5e0ef35add7f3ac59d3273c3861590978832e5393caa66043aa8b249e33e6e157c15ca84b88a7c90458712823b1aefa7bc900f8426fc285f7155bda",
    'referer': "https://music.163.com/my/",
    'cookie': "_ga=GA1.1.1048729511.1629103325; Qs_lvt_382223=1629103325; Qs_pv_382223=459897220871502800; _ntes_nnid=cd03c58fb5fcdff26dca50bfad3dbc5e,1629103325602; _ntes_nuid=cd03c58fb5fcdff26dca50bfad3dbc5e; _clck=155jmxr|1|etx; _ga_C6TGHFPQ1H=GS1.1.1629103325.1.0.1629103332.0; vinfo_n_f_l_n3=7f460ce273df2509.1.0.1630494303935.0.1630494603171; _iuqxldmzr_=32; NMTID=00OelitiKEzgGo2a0t8iXe3XiUquxkAAAF-0l68vA; WEVNSM=1.0.0; WNMCID=spenol.1644206933788.01.0; WM_TID=4RYz%2FUdEY09AUEFUABY%2FoO1Koi2axpK9; WM_NI=trtJFdDrEbgS9gh4t6imeCY9%2BNJgRH2GEPuISkQzDvwAHgc4QMeu95%2BK5pRkYXA9J9wLNsrOtiVT%2B1I7fW6rvdB25DfN52gkO4GyrcNFH1E0dozwk%2BRmiWtEIu8QpVIYREo%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee89d87df48882d0cc3f81ef8ea3d44f969e9fafaa7b89bc82aff162f386a5d7ef2af0fea7c3b92ab8aebcabc57088ae8b83e659fbb9a8d5f73eabb3aba4dc33e9928688d144f2998bb1f84391b59f9bc77eb59f8888e2409393ab96bc3fe995fb91d1619b888fdac933b5948294f145b8b79ab5aa3b8be9aab8b57ab6bc8ed3b850a692fbd3e6618dec899af1698e9a88d2c83ca8b1b698ea2192b3a7b8f74f8babf8b2f35e8b879ea6ee37e2a3; MUSIC_U=f189b537ee5001b24663937178cbfd7995148c9f4bf89ca87ec550beffe3408e519e07624a9f0053d78b6050a17a35e705925a4e6992f61dfe3f0151024f9e31; __csrf=bc5475e560cb2023ad355da57937c2f3; ntes_kaola_ad=1; JSESSIONID-WYYY=dyJh1du3%2FdHQ9DdG%2BwJUAdhtETkBac6zaYRTX37naqfAa9Pjtfo3JYfQWIviyyU3K8hqFGQ3Bv%2F1cknhPayU3x%2F8U0oCrn%2Fvp6gfAAt7iDPCfW%2FGd55I1W34rTqd6oqmTSPGFR%2FNz5rcNGa1QZ7SgkSvtzET3qQVS5b7d9XCG4HBowrX%3A1644219178627",
}
url = "https://music.163.com/weapi/playlist/manipulate/tracks?csrf_token=bc5475e560cb2023ad355da57937c2f3"

response = requests.post(url=url, data=data, headers=headers)
print(response.json())

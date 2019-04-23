"""
curl
'https://www.skelbiu.lt/index.php?mod=ajax&action=blockComment'
-H 'origin: https://www.skelbiu.lt'
-H 'accept-encoding: gzip, deflate, br'
-H 'accept-language: en-US,en;q=0.9,lt;q=0.8'
-H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'
-H 'content-type: application/x-www-form-urlencoded'
-H 'accept: */*'
-H 'referer: https://www.skelbiu.lt/skelbimai/saldytuvas-candy-su-defektu-40265827.html'
-H 'authority: www.skelbiu.lt'
-H 'cookie: __gfp_64b=FyjRDmUPT7gB3pkKOA_KTWTrRJykmbo2pshuu2E0Q0H.17; _ga=GA1.2.483995729.1474046446; PHPSESSID=nhembbqt59r77vq14bnbmse0du; _gid=GA1.2.840082006.1556031888; rememberMe=79052995cbf291ddc8901.81470885; __gads=ID=d4135f616f6f28c6:T=1556031779:S=ALNI_MZV1T43KWTva9PmzuSIMHb4F5AwMQ; fbShareShow40265827=1; _gat=1; _gat_master=1' --data 'blockComment=16494739' --compressed
"""

import requests


def block_comment(comment_id):
    headers = {
        'origin': 'https://www.skelbiu.lt',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9,lt;q=0.8',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'referer': 'https://www.skelbiu.lt/skelbimai/saldytuvas-candy-su-defektu-40265827.html',
        'authority': 'www.skelbiu.lt',
        'cookie': '__gfp_64b=FyjRDmUPT7gB3pkKOA_KTWTrRJykmbo2pshuu2E0Q0H.17; _ga=GA1.2.483995729.1474046446; PHPSESSID=nhembbqt59r77vq14bnbmse0du; _gid=GA1.2.840082006.1556031888; rememberMe=79052995cbf291ddc8901.81470885; __gads=ID=d4135f616f6f28c6:T=1556031779:S=ALNI_MZV1T43KWTva9PmzuSIMHb4F5AwMQ; fbShareShow40265827=1; _gat=1; _gat_master=1',
    }

    data = {"blockComment": comment_id}

    response = requests.post('https://hooks.slack.com/services/asdfasdfasdf', headers=headers, data=data)

    # print(response.status_code)

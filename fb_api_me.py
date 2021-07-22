import sys
import urllib.request
import json

# 240263402699918

if __name__ == '__main__':
    
    page_name = "jtbcnews"
    token = '토큰값을 넣어주세요'
    
    # https://graph.facebook.com/v11.0/?fields=id%2Cname&access_token=

    base = "https://graph.facebook.com/v11.0/?fields=id%2Cname&access_token="
    url = base + token

    print(url)
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            data = json.loads(response.read().decode('utf-8'))
            print(data)
            
    except Exception as e:
        print (e)

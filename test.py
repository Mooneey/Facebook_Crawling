import sys
import urllib.request
import json

# 240263402699918

if __name__ == '__main__':
    # [CODE 1]
    page_name = "jtbcnews"
    token = ''

    # [CODE 2]
    # https://graph.facebook.com/v2.8/[page_id]/?access+token=[App_ID]|[Secret_Key]
    # 형식의 문자열을 만들어 낸다

    base = "https://graph.facebook.com/v11.0/?fields=id%2Cname&access_token="
    # node = "/" + page_name
    # parameters = "/?access_token=%s" % token
    url = base + token

    print(url)

    # [CODE 3]
    req = urllib.request.Request(url)

    # [CODE 4]
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            data = json.loads(response.read().decode('utf-8'))
            print(data)
            #page_id = data['id']
            #print ("%s Facebook Numeric ID : %s" % (page_name, page_id))
    except Exception as e:
        print (e)
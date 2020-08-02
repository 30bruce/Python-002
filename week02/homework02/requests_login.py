import time
import requests
from fake_useragent import UserAgent


ua = UserAgent(verify_ssl=False)
headers = {
    'User-Agent' : ua.random,
    'Referer' : 'https://shimo.im/login?from=home'
}


def login():
    s = requests.Session()
    # post数据前获取cookie
    pre_login = 'https://shimo.im/login?from=home'
    pre_resp = s.get(pre_login, headers=headers)
    print(pre_resp)
    login_url = 'https://shimo.im/lizard-api/auth/password/login'
    form_data = {
        'email':'test@111.com',
        'mobile':'+86undefined',
        'password':'test123test456',
    }
    response = s.post(login_url, data=form_data, headers=headers, cookies=s.cookies)
    print(response)

if __name__ == "__main__":
    login()
import requests
from bs4 import BeautifulSoup
from env_utils import user_data



def keyzard_get_keyword():
    keyzard_id, keyzard_password = user_data('C:\\Users\\slaye\\PycharmProjects\\personal-data-analysis\\blog\\env\\keyzard_user.txt')

    session = requests.Session()

    login_data = {
        'id': keyzard_id,
        'pw': keyzard_password
    }

    url = 'https://keyzard.org/login/login'

    r = session.post(url, json=login_data)

    if r.status_code == 200:
        print('Logged in')
    else:
        print('Failed to login')
        print(r.status_code)

    r = session.get('https://keyzard.org/realtimekeyword')
    bs = BeautifulSoup(r.text, 'html.parser')

    result_list = []
    # 클래스명이 ellipsis100인 모든 td 태그를 찾아서 그 안에 있는 텍스트를 출력
    for td in bs.find_all('td', {'class': 'ellipsis100'}):
        result_list.append(td.text)

    return result_list

print(keyzard_get_keyword())
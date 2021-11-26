import requests
import os
import re
from dotenv import load_dotenv

load_dotenv()


def login():
    payload = {'log': os.getenv('LOGIN'), 'pwd': os.getenv('PASSWORD')}
    s = requests.Session()
    s.post(os.getenv('LOGIN_URL'), data=payload)
    return s


def download_artifacts(session, series_major, series_minor):
    series = f'{series_major}.{series_minor if series_minor == 10 else f"0{series_minor}"}'
    response = session.get(f'{os.getenv("SER_URL")}{series}')
    if not response.ok:
        return False

    urls = re.findall(r'href=[\'"]?(.*\.pdf)', response.text)
    if not urls or len(urls) != 2:
        return False

    for url, title in zip(urls, ['Условие', 'Решение']):
        file = f'{os.getenv("OUTPUT_DIR")}\\Серия {series}. {title}.pdf'
        print(file)
        response = session.get(f'{os.getenv("BASE_URL")}{url}')
        with open(file, 'wb+') as f:
            f.write(response.content)

    return True


def main():
    session = login()
    done = False
    for major in range(1, 4):
        if done:
            break

        for minor in range(1, 11):
            result = download_artifacts(session, major, minor)
            if not result:
                done = True
                break

    print('Done!')


if __name__ == '__main__':
    main()

import requests


class HttpMethods:
    headers = {'Content-type': 'application/json'}
    cookies = ''

    @staticmethod
    def get(url):
        result = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookies)
        return result

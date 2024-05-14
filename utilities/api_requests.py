from utilities.http_methods import HttpMethods


class ApiRequests:

    @staticmethod
    def get_request(url):
        """Отправка запроса GET и вывод на печать URL запроса"""
        get_response = HttpMethods.get(url)
        print(f'GET request URL: {url}')
        return get_response

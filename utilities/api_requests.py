from utilities.http_methods import HttpMethods


class ApiRequests:

    @staticmethod
    def get_request(url):
        get_response = HttpMethods.get(url)
        print(f'GET request URL: {url}')
        return get_response


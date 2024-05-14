from jsonschema import validate
from jsonschema.exceptions import ValidationError


class BaseMethods:

    @staticmethod
    def check_status_code(url, expected_status, response):
        """Сравнение ожидаемого статус-кода с фактическим. Если неуспешно - отображается ошибка"""
        try:
            assert expected_status == response.status_code
            print(f'{url} - status code is the same as expected - {response}')
        except AssertionError:
            print(f'Error! Current {url} status code: {response}')

    @staticmethod
    def check_response(url, response, schema):
        """Вызов валидатора и проверка ответа в соответствии со схемой (см validation_schemes.py). Если
        валидация неуспешна - отображается ошибка"""
        try:
            validate(response, schema)
            print(f'{url} - response checked and its equal to expected validation schema')
        except ValidationError as error:
            print(f'Error! {url} - response is not equal to expected')
            print(error)

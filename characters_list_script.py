from utilities.base_methods import BaseMethods
from utilities.api_requests import ApiRequests
from utilities.validation_schemes import Validation

base_url = 'https://swapi.dev/api/'


class CharactersList:
    base_url = 'https://swapi.dev/api/'
    vader_films_urls = []
    vader_films_all_chars_urls = []
    vader_films_all_chars_names = []

    @staticmethod
    def get_vader_url():
        """Отправка запроса на получение информации о персонаже, сохранение
        списка фильмов, где присутствовал персонаж, в переменную vader_films"""
        darth_vader_url = base_url + 'people/4'
        validation_schema = Validation.response_character()
        response = ApiRequests.get_request(darth_vader_url)
        response_json = response.json()
        vader_films = response_json.get('films')
        """Проверка статус-кода ответа и тела ответа"""
        BaseMethods.check_status_code(darth_vader_url, 200, response)
        BaseMethods.check_response(darth_vader_url, response_json, validation_schema)
        """Запуск цикла для добавления ссылок на фильмы из массива films в 
        массив vader_films_urls"""
        for i in vader_films:
            CharactersList.vader_films_urls.append(i)
        print('List of films with Darth Vader received and saved', '\n')

    @staticmethod
    def get_vader_films_urls():
        """Отправка запросов на получение информации о каждом фильме,
         где присутствовал персонаж, сохранение списка персонажей из каждого фильма
          в переменную vader_films_all_chars"""
        for i in CharactersList.vader_films_urls:
            response = ApiRequests.get_request(i)
            validation_schema = Validation.response_character()
            response_json = response.json()
            vader_films_all_chars = response_json.get('characters')
            """Проверка статус-кода ответа и тела ответа для каждого запроса фильма"""
            BaseMethods.check_status_code(i, 200, response)
            BaseMethods.check_response(i, response_json, validation_schema)
            """Запуск цикла для добавления ссылок на профили всех персонажей
             из всех полученных фильмов в массив vader_films_all_chars_urls"""
            for k in vader_films_all_chars:
                CharactersList.vader_films_all_chars_urls.append(k)
        print('List of all characters from films with Darth Vader received and saved', '\n')

    @staticmethod
    def get_vader_films_character_names():
        """Удаление из массива vader_films_all_chars_urls всех неуникальных ссылок"""
        unique_char_urls = list(dict.fromkeys(CharactersList.vader_films_all_chars_urls))
        print('Start receiving and saving characters names to unique names list')
        for i in unique_char_urls:
            """Отправка запросов на все URL в массиве unique_char_urls, сохранение
            имени каждого персонажа в переменную char_name и добавление этого имени 
            в массив vader_films_all_chars_names"""
            response = ApiRequests.get_request(i)
            response_json = response.json()
            char_name = response_json.get('name')
            CharactersList.vader_films_all_chars_names.append(char_name)
            print(f'Character name "{char_name}" has been received and added to unique names list')
        print('All unique names has been saved', '\n')

    @staticmethod
    def write_names_to_file():
        """Запись уникальных имен отобранных персонажей в текстовый файл"""
        print('Writing all saved unique names to names.txt')
        names_list_convert = map(str, CharactersList.vader_films_all_chars_names)
        names_list = '\n'.join(names_list_convert)
        filename = 'names.txt'
        file = open(filename, 'w', encoding='utf-8')
        file.write(names_list)
        file.close()
        print('All unique names added to names.txt')

    @staticmethod
    def create_names_file():
        CharactersList.get_vader_url()
        CharactersList.get_vader_films_urls()
        CharactersList.get_vader_films_character_names()
        CharactersList.write_names_to_file()


CharactersList.create_names_file()

from utilities.base_methods import BaseMethods
from utilities.api_requests import ApiRequests

base_url = 'https://swapi.dev/api/'


class CharactersList:
    base_url = 'https://swapi.dev/api/'
    vader_films_urls = []
    vader_films_all_chars_urls = []
    vader_films_all_chars_names = []

    @staticmethod
    def get_vader_url():
        darth_vader_url = base_url + 'people/4'
        response = ApiRequests.get_request(darth_vader_url)
        response_json = response.json()
        vader_films = response_json.get('films')
        BaseMethods.check_status_code(darth_vader_url, 200, response)
        for i in vader_films:
            CharactersList.vader_films_urls.append(i)
        print(CharactersList.vader_films_urls)

    @staticmethod
    def get_vader_films_urls():
        for i in CharactersList.vader_films_urls:
            response = ApiRequests.get_request(i)
            response_json = response.json()
            vader_films_all_chars = response_json.get('characters')
            BaseMethods.check_status_code(i, 200, response)
            for k in vader_films_all_chars:
                CharactersList.vader_films_all_chars_urls.append(k)

    @staticmethod
    def get_vader_films_character_names():
        unique_char_urls = list(dict.fromkeys(CharactersList.vader_films_all_chars_urls))
        for i in unique_char_urls:
            response = ApiRequests.get_request(i)
            response_json = response.json()
            char_name = response_json.get('name')
            CharactersList.vader_films_all_chars_names.append(char_name)

    @staticmethod
    def write_names_to_file():
        names_list_convert = map(str, CharactersList.vader_films_all_chars_names)
        names_list = '\n'.join(names_list_convert)
        filename = 'names.txt'
        file = open(filename, 'w', encoding='utf-8')
        file.write(names_list)

    @staticmethod
    def create_names_file():
        CharactersList.get_vader_url()
        CharactersList.get_vader_films_urls()
        CharactersList.get_vader_films_character_names()
        CharactersList.write_names_to_file()


CharactersList.create_names_file()

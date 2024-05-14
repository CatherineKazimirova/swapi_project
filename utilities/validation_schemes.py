class Validation:

    @staticmethod
    def response_character():
        """Схема для проверки ответа на GET запрос получения персонажа фильма"""
        schema = {"type": "object",
                  "properties": {"name": {"type": "string"},
                                 "height": {"type": "string"},
                                 "mass": {"type": "string"},
                                 "hair_color": {"type": "string"},
                                 "skin_color": {"type": "string"},
                                 "eye_color": {"type": "string"},
                                 "birth_year": {"type": "string"},
                                 "gender": {"type": "string"},
                                 "homeworld": {"type": "string", "format": "uri"},
                                 "films": {"type": "array", "items": {"type": "string", "format": "uri"}},
                                 "species": {"type": "array", "items": {"type": "string", "format": "uri"}},
                                 "vehicles": {"type": "array", "items": {"type": "string", "format": "uri"}},
                                 "starships": {"type": "array", "items": {"type": "string", "format": "uri"}},
                                 "created": {"type": "string", "format": "date-time"},
                                 "edited": {"type": "string", "format": "date-time"},
                                 "url": {"type": "string", "format": "uri"}}}
        return schema

    @staticmethod
    def response_film():
        """Схема для проверки ответа на GET запрос получения фильма"""
        schema = {"type": "object",
                  "properties": {"title": {"type": "string",
                                           "enum": ["A New Hope", "The Empire Strikes Back",
                                                    "Return of the Jedi", "The Phantom Menace",
                                                    "Attack of the Clones", "Revenge of the Sith"]},
                                 "episode_id": {"type": "number", "minimum": 1, "maximum": 6},
                                 "opening_crawl": {"type": "string"}, "director": {"type": "string"},
                                 "producer": {"type": "string"},
                                 "release_date": {"type": "string", "format": "date"},
                                 "characters": {"type": "array",
                                                "items": {"type": "string", "format": "uri"}},
                                 "planets": {"type": "array",
                                             "items": {"type": "string", "format": "uri"}},
                                 "starships": {"type": "array",
                                               "items": {"type": "string", "format": "uri"}},
                                 "vehicles": {"type": "array",
                                              "items": {"type": "string", "format": "uri"}},
                                 "species": {"type": "array",
                                             "items": {"type": "string", "format": "uri"}},
                                 "created": {"type": "string", "format": "date-time"},
                                 "edited": {"type": "string", "format": "date-time"},
                                 "url": {"type": "string", "format": "uri"}}}
        return schema

class Person:
    def __init__(self, **details):
        self.__personal_details = dict()
        self.__personal_details["name"] = details["name"]
        self.__personal_details["age"] = details["age"]

    def get_personal_details(self):
        return self.__personal_details

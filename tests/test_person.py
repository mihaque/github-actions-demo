from person import Person


class TestPerson:
    def __int__(self):
        pass

    def test_get_personal_details(self):
        p1 = Person(name="mih", age=29)
        personal_details = p1.get_personal_details()
        assert personal_details["name"] == "mih"
        assert personal_details["age"] == 29
        
    def test_day(self):
        import os
        assert os.environ['DAY_OF_WEEK'] == 'TUE'

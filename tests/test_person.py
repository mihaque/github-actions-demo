from person import Person
import os

class TestPerson:
    def __int__(self):
        pass

    def test_get_personal_details(self):
        p1 = Person(name="mih", age=29)
        personal_details = p1.get_personal_details()
        assert personal_details["name"] == "mih"
        assert personal_details["age"] == 29
        
    def test_day(self):
        
        assert os.environ['DAY_OF_WEEK'] == 'TUE'
    
    @staticmethod
    def get_modified_files():
        
        commit_msg = os.environ['PR_BODY']
        return commit_msg.split(',')
    
    @pytest.mark.parameterize('file', get_modified_files())
    def test_pr_content(file):
        assert 'success' in file

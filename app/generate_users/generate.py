from app.base.provider import Provider
import names
import random

class Processor:
    def __init__(self):
        self.db = Provider('sql')

    def generate_female(self):
        params = {
            'avatar': [],
            'name': [],
            'description': [],
            'id': [],
            'sex': False
        }
        for i in range(1000):
            params.get('avatar').append(random.choice(names.URLS_FEMALE))
            params.get('name').append(random.choice(names.FEMALE))
            params.get('description').append(random.choice(names.DESCRIPTION))
            params.get('id').append(f'9b91e226-41e1-4350-8afe-91f9f4c0{i}')
        return self.db.exec_by_file('generate.sql', params)

    def generate_male(self):
        params = {
            'avatar': [],
            'name': [],
            'description': [],
            'id': [],
            'sex': True
        }
        for i in range(1000, 2000):
            params.get('avatar').append(random.choice(names.URLS_MALE))
            params.get('name').append(random.choice(names.MALE))
            params.get('description').append(random.choice(names.DESCRIPTION))
            params.get('id').append(f'9b91e226-41e1-4350-8afe-91f9f4c0{i}')
        return self.db.exec_by_file('generate.sql', params)


#Processor().generate_female()
#Processor().generate_male()

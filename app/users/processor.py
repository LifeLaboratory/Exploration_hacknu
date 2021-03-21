from app.base.provider import Provider
import datetime


class Processor:
    def __init__(self):
        self.db = Provider('users/sql')

    def login(self, data):
        params = {
            'id': data.get('id'),
            'avatar': data.get('avatar'),
            'description': data.get('description'),
            'name': data.get('name'),
            'lastname': data.get('lastname'),
            'avatarThumb': data.get('avatarThumb'),
            'phone': data.get('phone'),
            'latitude': data.get('latitude'),
            'longitude': data.get('longitude'),
            'sex': data.get('sex'),
            'sex_find': data.get('sex_find'),
        }
        user = self.db.exec_by_file('select_user.sql', params)
        if not user:
            self.db.exec_by_file('insert_user.sql', params)
            return {'status': 'profile'}
        if self.get_meeting(params):
            return {'status': 'meeting'}
        self.db.exec_by_file('update_lat_log.sql', params)
        return {'status': 'search'}

    def get_meeting(self, data):
        params = {
            'id': data.get('id'),
        }
        meeting = self.db.exec_by_file('get_meeting.sql', params)
        if meeting:
            return meeting[0].get('meeting_info')

    def swipe(self, data):
        params = {
            'id_first': data.get('id'),
            'id_second': data.get('id_second'),
            'status': data.get('status'),
        }
        self.db.exec_by_file('swipe.sql', params)

        if params.get('status') is True:
            params = {
                'id_first': data.get('id_second'),
                'id_second': data.get('id'),
            }
            status = self.db.exec_by_file('check_swipe.sql', params)

            if status:
                place_info = self.db.exec_by_file('get_place.sql', {})[0]
                time_meeting = datetime.datetime.now()
                time_meeting = time_meeting.replace(hour=time_meeting.hour + 4, minute=0, second=0, microsecond=0)
                params = {
                    'id_first': data.get('id'),
                    'id_second': data.get('id_second'),
                    'id_place': place_info.get('id_place'),
                    'time_meeting': time_meeting,
                }
                self.db.exec_by_file('insert_meeting.sql', params)

                return self.get_meeting({'id': data.get('id')})

        params = {
            'id': data.get('id'),
            'sex_find': [data.get('sex_find')] if data.get('sex_find') is not None else [True, False]
        }
        selected = self.db.exec_by_file('get_next_user.sql', params)
        if selected:
            return selected[0]

    def get_next_user(self, data):
        params = {
            'id': data.get('id'),
            'limit': data.get('limit'),
            'sex_find': [data.get('sex_find')] if data.get('sex_find') is not None else [True, False]
        }
        selected = self.db.exec_by_file('get_next_user.sql', params)

        ids_likes = [select.get('id') for select in selected]
        params = {
            'ids': [data.get('id')] * len(ids_likes),
            'ids_likes': ids_likes,

        }
        self.db.exec_by_file('insert_5_likes.sql', params)
        return selected

    def get_profile(self, data):
        params = {
            'id': data.get('id')
        }
        return self.db.exec_by_file('select_user.sql', params)

    def update_profile(self, data):
        params = {
            'id': data.get('id'),
            'avatar': data.get('avatar'),
            'description': data.get('description'),
            'name': data.get('name'),
            'lastname': data.get('lastname'),
            'avatarThumb': data.get('avatarThumb'),
            'phone': data.get('phone'),
            'latitude': data.get('latitude'),
            'longitude': data.get('longitude'),
            'sex': data.get('sex'),
            'sex_find': data.get('sex_find'),
        }
        self.db.exec_by_file('update_user.sql', params)
        return self.get_profile(params)

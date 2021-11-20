import json
import logging
import tidalapi

class TidalBackend:
    def __init__(self):
        self._session = None

    def oauth_session(self):
        print('Log in started')
        self._session = tidalapi.Session()
        oauth_file = 'tidal_oauth_file.json'
        try:
            with open(oauth_file, 'r') as session_file:
                print('Trying to log from previous logs')
                data = json.load(session_file)
                self._session.load_oauth_session(
                    data['session_id']['data'],
                    data['token_type']['data'],
                    data['access_token']['data'],
                    data['refresh_token']['data']
                )
                session_file.close()
        except: 
            print('Could not load previous logs or they dont exist')

        if not self._session.check_login():
            print('Creating a new session')
            self.create_new_oauth_session(oauth_file)

        if self._session.check_login():
            print('Log In OK')
        else:
            print('Log In not OK')


    def create_new_oauth_session(self, oauth_file):
        self._session.login_oauth_simple(function=print)

        if self._session.check_login():
            data = {}
            data['token_type'] = {'data': self._session.token_type}
            data['session_id'] = {'data': self._session.session_id}
            data['access_token'] = {'data': self._session.access_token}
            data['refresh_token'] = {'data': self._session.refresh_token}
            
            with open(oauth_file, 'w') as session_file:
                json.dump(data, session_file)
                session_file.close()


import requests, json, httplib2, datetime, os

from urllib.parse import urlencode
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run_flow
from googleapiclient import discovery

class Goco:
    '''
    # [Goco](https://github.com/elmoiv/goco):

    ### Stupidly user-friendly Google API services Authenticator

    - `client_secret_path`:  Path to your `client_secret.json` file
    
    
    '''
    def __init__(self, client_secret_path):

        self.csecp = client_secret_path
        self.csrgp = 'credentials.storage'

        if not os.path.exists(self.csecp):
            raise FileNotFoundError('client_secret.json')

    def authorize_credentials(self, scope):

        STORAGE = Storage(self.csrgp)
        credentials = STORAGE.get()

        if credentials is None or credentials.invalid:
            flow = flow_from_clientsecrets(self.csecp, scope='https://www.googleapis.com/auth/' + scope)
            http = httplib2.Http()
            credentials = run_flow(flow, STORAGE, http=http)

        return credentials

    def refresh_access_token(self):

        data = json.loads(open(self.csecp).read())['installed']

        client_id = data['client_id']
        client_secret = data['client_secret']
        refresh_token = json.loads(open(self.csrgp).read())['refresh_token']

        # Getting new "access_token"
        request = requests.post(
            'https://accounts.google.com/o/oauth2/token',

            data=urlencode({
                'grant_type':    'refresh_token',
                'client_id':     client_id,
                'client_secret': client_secret,
                'refresh_token': refresh_token
                }),

            headers={
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept':       'application/json'
                }
            )

        response = json.loads(request.content)
        return response['access_token']

    def update_credentials(self, access_token):

        creds = json.loads(open(self.csrgp).read())

        date = str(datetime.datetime.now()).split(' ')

        # Token expiry is in RFC 3339 date-time format
        # YYYY-MM-DDTHH:MM:SSZ
        token_expiry = '{}T{}Z'.format(date[0], date[1][:8])

        creds["token_expiry"] = token_expiry
        creds["access_token"] = access_token
        creds["token_response"]["access_token"] = access_token

        with open(self.csrgp, 'w') as creds_new:
            json.dump(creds, creds_new)
        
        return Storage(self.csrgp).get()


    def connect(self, scope, service_name, version):

        # Checks for "credentials.storage" and generates one if not found
        self.authorize_credentials(scope)

        # Gets new "access_token" using refresh token
        access_token = self.refresh_access_token()

        # Updates "credentials.storage" with the new "access_token" and "token_expiry"
        cerds = self.update_credentials(access_token)
        
        # Connecting to chosen google service
        http_auth = cerds.authorize(httplib2.Http())

        service = discovery.build(
            service_name,
            version,
            http=http_auth
            )

        return service

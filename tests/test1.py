import goco

GoogleApi = goco.Goco('client_secret.json', 'credentials.storage')

MyDrive = GoogleApi.connect(scope='drive.readonly', service_name='drive', version='v3')

Files = MyDrive.files().list()

print(Files.execute())

input()
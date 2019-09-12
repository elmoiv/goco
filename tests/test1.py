from goco import Goco

GoogleApi = Goco('client_secret.json')

MyDrive = GoogleApi.connect(scope='drive.readonly', service_name='drive', version='v3')

Files = MyDrive.files().list()

print(Files.execute())

input()

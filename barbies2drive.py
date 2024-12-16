from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account

# Configura las credenciales de servicio
SCOPES = ['https://www.googleapis.com/auth/drive.file']
SERVICE_ACCOUNT_FILE = 'metal-contact-444917-e3-e54dd3b95be4.json'

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('drive', 'v3', credentials=credentials)

# Sube un archivo
file_metadata = {'name': 'foto.png', 'parents': ['1JHu30KTBZAx1hHJCk7Oq8rwqOkE2KcJz']}
media = MediaFileUpload('ruta_a_tu_foto.png', mimetype='image/png')

file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
print('Archivo subido:', file.get('id'))

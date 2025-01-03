from flask import Flask, request
from flask_cors import CORS  # Necesario para solicitudes desde otros dominios
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account

app = Flask(__name__)
CORS(app)  # Permite solicitudes CORS

# Rutas para las credenciales y permisos de Google Drive
SERVICE_ACCOUNT_FILE = 'metal-contact-444917-e3-e54dd3b95be4.json'
SCOPES = ['https://www.googleapis.com/auth/drive']

# Configura las credenciales de Google
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
drive_service = build('drive', 'v3', credentials=credentials)

@app.route('/upload', methods=['POST'])
def upload_file():
    # Obtener el archivo de la solicitud
    file = request.files['file']
    
    # Guardar el archivo en el servidor temporalmente
    file.save(file.filename)
    
    # Subir el archivo a Google Drive
    file_metadata = {'name': file.filename, 'parents': ['1JHu30KTBZAx1hHJCk7Oq8rwqOkE2KcJz']}
    media = MediaFileUpload(file.filename, mimetype=file.content_type)
    file_drive = drive_service.files().create(
        body=file_metadata, media_body=media, fields='id').execute()

    return {'file_id': file_drive.get('id')}, 200

if __name__ == '__main__':
    app.run(debug=True)


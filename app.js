// Seleccionar elementos del DOM
const fileInput = document.getElementById('fileInput');
const uploadButton = document.getElementById('uploadButton');
const statusText = document.getElementById('status');

// URL del servidor donde se subirán los archivos
const SERVER_URL = 'https://tu-servidor.com/upload';

// Manejador de eventos para el botón "Subir"
uploadButton.addEventListener('click', async () => {
  const file = fileInput.files[0]; // Obtener el archivo seleccionado

  if (!file) {
    statusText.textContent = 'Por favor, selecciona un archivo para subir.';
    return;
  }

  statusText.textContent = 'Subiendo archivo...';

  try {
    // Crear un FormData y agregar el archivo
    const formData = new FormData();
    formData.append('file', file);

    // Enviar el archivo al servidor usando fetch
    const response = await fetch(SERVER_URL, {
      method: 'POST',
      body: formData
    });

    if (response.ok) {
      const data = await response.json();
      statusText.textContent = `Archivo subido con éxito. ID en Drive: ${data.file_id}`;
    } else {
      statusText.textContent = 'Error al subir el archivo al servidor.';
      console.error('Error:', await response.text());
    }
  } catch (error) {
    statusText.textContent = 'Error al subir el archivo.';
    console.error('Error:', error);
  }
});

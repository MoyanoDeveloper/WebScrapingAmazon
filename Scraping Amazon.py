import sys
import requests
from bs4 import BeautifulSoup

# Forzar a Python a usar UTF-8 para la salida estándar
sys.stdout.reconfigure(encoding='utf-8')

# URL de la página que deseas scrapear
url = "https://www.amazon.com/s?k=comida+para+perros&crid=3FVWS747LPTOB&sprefix=%2Caps%2C177&ref=nb_sb_ss_recent_1_0_recent"

# Configurar el User-Agent para hacer que parezca que el request proviene de un navegador
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
    "Accept-Language": "en-US, en;q=0.5",
}

# Hacer la solicitud HTTP
response = requests.get(url, headers=headers)

# Comprobar si la solicitud fue exitosa
if response.status_code == 200:
    # Extraer el contenido HTML de la página
    html_content = response.content

    # Usar BeautifulSoup para hacer el parseo del HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Imprimir el HTML (opcional)
    print(soup.prettify())
else:
    print(f"Error al acceder a la página, código de estado: {response.status_code}")
import requests
import os



def download_file(url: str, path: str = "downloads"):
    try:

        os.makedirs(path, exist_ok=True)
        request = requests.get(url)

    except requests.exceptions.RequestException as e:
        print(f"Sem internet ou outro erro {e}")

    print("Dowload finalizado com sucesso")
    print(request.json())
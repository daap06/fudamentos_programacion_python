import requests
import json

def request_get(url):
        """
        request_get Obtiene respuesta de una api.

        Si la respuesta es positiva 2xx retorna un json.

        :param url: Api
        :return: json
        """
        response = requests.get(url)
        if response.status_code // 100 == 2:
                data = response.json()
                return data
        else:
                print(f'Error: Código de estado {response.status_code}')



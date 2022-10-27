import requests #pip3 install requests
import json

#vamos a crear una clase para NO LO SÉ LA VERDAD
class YT_Stats:
    #inicializar los atributos + metodos necesarios en la clase
    #los atributos los podemos llamar igual para que sea más facil
    #el método puede estar inicializado o no, en este caso no
    def __init__(self, api_key, channel_id):
        self.api_key = api_key
        self.channel_id = channel_id
        self.channel_statistics = None

    #creamos la funcion para recbir la información
    def get_channel_statistics(self):
        #esta es la URL de la web YT + añadimos channel id + la apikey
        url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={self.channel_id}&key={self.api_key}'
        #print(url)
        #vamos a la url y la cogemos en JSON y la guardamos en json_url
        json_url = requests.get(url)
        #NI PUTA IDEA
        data = json.loads(json_url.text)
        #print(data)
        #accedemos directamente a los datos que queremos del Json: statistics
        data = data["items"][0]["statistics"]

        return data
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
        self.video_data = None

    #creamos la funcion para recbir la información
    def get_channel_statistics(self):
        #esta es la URL de la web YT + añadimos channel id + la apikey
        url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={self.channel_id}&key={self.api_key}'
        #print(url)
        #vamos a la url y la cogemos en JSON y la guardamos en vble json_url
        json_url = requests.get(url)
        #Transforma lo que seria un json diccionario, en mas formsto texto
        data = json.loads(json_url.text)
        print(data)
        #accedemos directamente a los datos que queremos del Json: statistics
        data = data["items"][0]["statistics"]
        #asocia al atributo la información que obtenemos del json
        self.channel_statistics = data
        #devuelve el data
        return data
    
    def get_channel_video_data (self,limit=None):
        #conseguir video ids
        channel_videos = self._get_channel_videos(limit=50)
        

        #conseguir estadisticas videos
    
    def _get_channel_videos(self,limit=None):
        url = f'https://www.googleapis.com/youtube/v3/search?key={self.api_key}&channelId={self.channel_id}&part=id&order=date'
        
        if limit is not None and isinstance(limit, int):
            url += '&maxResults=' + str(limit)
        print(url)

    #CREAMOS UNA FUNCION PARA ALMACENAR EL JSON
    def dump(self):
        #si no hay json, entonces nada
        if self.channel_statistics is None:
            return
        

        channel_title = "CHANNEL" #TODO
        #cambiar espacios por barra baja
        channel_title = channel_title.replace(" ","_").lower()
        #guardamos el archivo con el titulo del canal en formato json
        file_name = channel_title + '.json'

        #creamos el archivo 
        with open(file_name,'w') as f:
            json.dump(self.channel_statistics,f, indent = 4)

        print('file dumped')

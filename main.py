from youtube_statistics import YT_Stats

#damos la información del canal que queremos analizar
channel_id = 'UCd-1T_9iqK7US0Bj9KjF_6A'
#damos la api que vamos a utilizar
api_key = 'AIzaSyDvTsuDlJI4soiYDTFWVD5_7w8tfo-vJyw'
#llamamos a la clase que hemos hecho antes con las dos variables
yt = YT_Stats(api_key,channel_id)

#ESTO NO SE PORQUE LO HACE
data = yt.get_channel_statistics()
#imprime por pantalla el valor del json
print(data)
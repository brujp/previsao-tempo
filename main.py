import requests
import json

r = requests.get('http://www.geoplugin.net/json.gp')

if(r.status_code != 200):
    print('Não foi possível obter a localização!')
else:
    localizacao = json.loads(r.text) #Resposta da requisição transformada em JSON
    latitude = localizacao['geoplugin_latitude']
    longitude = localizacao['geoplugin_longitude']
    print('lat:', latitude)
    print('long:', longitude)
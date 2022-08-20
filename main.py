import requests
import json
import pprint

accuweatherApiKey = 'f2MFsAFv1sDdmoj6S9VRqeMC2tGChW4R'

r = requests.get('http://www.geoplugin.net/json.gp')

if(r.status_code != 200):
    print('Não foi possível obter a localização!')
else:
    localizacao = json.loads(r.text) #Resposta da requisição transformada em JSON
    latitude = localizacao['geoplugin_latitude']
    longitude = localizacao['geoplugin_longitude']

    #Requisição para pegar o código do local
    locationApiUrl = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=" + accuweatherApiKey + "&q=" + latitude + "%2C" + longitude + "&language=pt-br"
    r2 = requests.get(locationApiUrl)

    if (r2.status_code != 200):
        print('Não foi possível obter o código do local!')
    else:
        locationResponse = json.loads(r2.text)
        nomeLocal = locationResponse['LocalizedName'] + ", " \
            + locationResponse['AdministrativeArea']['LocalizedName'] + ". " \
            + locationResponse['Country']['LocalizedName']

        codigoLocal = locationResponse['Key']

        print("Local: " + nomeLocal)
        print("Codigo: " + codigoLocal)


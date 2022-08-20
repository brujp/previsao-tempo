import requests
import json

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

        print('Obtendo clima do local: ' + nomeLocal)

        #API que retorna a temperatura e o texto do clima
        currentConditionsApiUrl = "http://dataservice.accuweather.com/currentconditions/v1/" + codigoLocal + "?apikey=" + accuweatherApiKey + "&language=pt-br"
        r3 = requests.get(currentConditionsApiUrl)

        if (r3.status_code != 200):
            print('Não foi possível obter a temperatura do local!')
        else:
            currentConditionsResponse = json.loads(r3.text)

        textoClima = currentConditionsResponse[0]['WeatherText']
        temperatura = currentConditionsResponse[0]['Temperature']['Metric']['Value']

        print('Clima no momento: ' + textoClima)
        print('Temperatura: ' + str(temperatura) + ' oC')
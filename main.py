import requests
import json
# import pprint

accuweatherApiKey = 'f2MFsAFv1sDdmoj6S9VRqeMC2tGChW4R'

def pegarCoordenadas():
    r = requests.get('http://www.geoplugin.net/json.gp')

    if (r.status_code != 200):
        print('Não foi possível obter a localização!')
        return None
    else:
        try:
            localizacao = json.loads(r.text)  # Resposta da requisição transformada em JSON
            coordenadas = {}
            coordenadas['latitude'] = localizacao['geoplugin_latitude']
            coordenadas['longitude'] = localizacao['geoplugin_longitude']
            return coordenadas  # Retorna um dicionário com a latitude e longitude
        except:
            return None

def pegarCodigoDoLocal(latitude, longitude):
    # API que retorna o código do local
    locationApiUrl = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=" + accuweatherApiKey + "&q=" + latitude + "%2C" + longitude + "&language=pt-br"
    r = requests.get(locationApiUrl)

    if (r.status_code != 200):
        print('Não foi possível obter o código do local!')
        return None
    else:
        try:
            locationResponse = json.loads(r.text)
            infoLocal = {}
            infoLocal['nomeLocal'] = locationResponse['LocalizedName'] + ", " \
                                 + locationResponse['AdministrativeArea']['LocalizedName'] + ". " \
                                 + locationResponse['Country']['LocalizedName']
            infoLocal['codigoLocal'] = locationResponse['Key']
            return infoLocal
        except:
            return None

def pegarTempoAgora(codigoLocal, nomeLocal):
    # API que retorna a temperatura e o texto do clima
    currentConditionsApiUrl = "http://dataservice.accuweather.com/currentconditions/v1/" + codigoLocal + "?apikey=" + accuweatherApiKey + "&language=pt-br"
    r = requests.get(currentConditionsApiUrl)

    if (r.status_code != 200):
        print('Não foi possível obter a temperatura do local!')
        return None
    else:
        try:
            currentConditionsResponse = json.loads(r.text)
            infoClima = {}
            infoClima['textoClima'] = currentConditionsResponse[0]['WeatherText']
            infoClima['temperatura'] = currentConditionsResponse[0]['Temperature']['Metric']['Value']
            infoClima['nomeLocal'] = nomeLocal
            return infoClima
        except:
            return None

# Inicio do programa
try:
    coordenadas = pegarCoordenadas()
    local = pegarCodigoDoLocal(coordenadas['latitude'], coordenadas['longitude'])
    climaAtual = pegarTempoAgora(local['codigoLocal'], local['nomeLocal'])
    print('Clima atual em: ' + climaAtual['nomeLocal'])
    print(climaAtual['textoClima'])
    print('Temperatura: ' + str(climaAtual['temperatura']) + ' oC')
except:
    print('Erro ao processar a solicitação')

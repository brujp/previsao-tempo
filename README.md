# App de previsão do tempo
App de previsão do tempo. Nele, foram utilizadas requisições HTTP para pegar informações de diferentes serviços meteorológicos e apresentar a previsão do tempo ao usuário.

Ao rodar a aplicação, ela já identificará o seu local a partir do seu IP e fornecerá informações sobre o clima do local.

## Exemplo de saída da aplicação:

Obtendo clima do local: Mauá, São Paulo. Brasil
Clima no momento: Nublado
Temperatura: 11.8 oC

## API's públicas utilizadas para o desenvolvimento do projeto

- GeoPlugin: https://www.geoplugin.com/

API que nos retorna a latitude e a longitude a partir do nosso IP:
http://www.geoplugin.net/json.gp

- AccuWeather: https://developer.accuweather.com/

API que nos retorna a temperatura e o texto do clima:
https://developer.accuweather.com/accuweather-current-conditions-api/apis/get/currentconditions/v1/%7BlocationKey%7D

API que nos retorna o código do local (necessária para a realização da requisição para a aplicação acima):
https://developer.accuweather.com/accuweather-locations-api/apis/get/locations/v1/cities/geoposition/search

## Tecnologias utilizadas

Python

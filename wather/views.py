from django.shortcuts import render
import requests
import json


def wather_fun(request):

    if request.method == 'POST':

            city=request.POST.get('city')

            url = f"https://api.weatherapi.com/v1/current.json?key=2eb3267f5eac4a318ce75553233007&q={city}"
            r = requests.get(url)
            res= json.loads(r.text)

            city_name=res['location']['name']
            date_time = res['location']['localtime']

            temp = res['current']['temp_c']
            condition=res['current']['condition']
            img = res['current']['condition']
            wind_kph=res['current']['wind_kph']
            p_mb = res['current']['pressure_mb']
            data = {
                'cu':res,
                'c_name':city_name,
                'temp':temp,
                'date_time':date_time,
                'cond':condition['text'],
                'img':img['icon'],
                'p_mb':p_mb,
                'wind':wind_kph,
            }
            return render(request,"wather.html",data)



 # curl --location --request GET 'http://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q=bulk' \
    # --header 'Content-Type: application/json' \
    # --data-raw '{
    #     "locations": [
    #         {
    #             "q": "53,-0.12",
    #             "custom_id": "my-id-1"
    #         },
    #         {
    #             "q": "London",
    #             "custom_id": "any-internal-id"
    #         },
    #         {
    #             "q": "90201",
    #             "custom_id": "us-zipcode-id-765"
    #         }
    #     ]
    # }'

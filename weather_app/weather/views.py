from django.shortcuts import render
import requests
import requests
from django.shortcuts import render

def weather_view(request):
    api_url = "http://api.weatherapi.com/v1/forecast.json"
    params = {
        "key": "9533d8063ffe47daa1460625252702",
        "q": "Ambala",  # You can change this to a dynamic input
        "days": 10     # Get 10 days forecast
    }
    
    response = requests.get(api_url, params=params)
    weather_data = response.json()
    
    return render(request, "weather.html", {"forecast": weather_data["forecast"]["forecastday"]})


def weather_view(request):
    city = request.GET.get('city', 'Ambala')  # Default city is Ambala if no input
    api_key = '9533d8063ffe47daa1460625252702'
    api_url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no'

    response = requests.get(api_url)
    weather_data = response.json()

    context = {}
    if "location" in weather_data:
        context = {
            'city': weather_data['location']['name'],
            'country': weather_data['location']['country'],
            'temperature_c': weather_data['current']['temp_c'],
            'temperature_f': weather_data['current']['temp_f'],
            'humidity': weather_data['current']['humidity'],
            'pressure': weather_data['current']['pressure_mb'],
            'icon': weather_data['current']['condition']['icon'],
            'condition': weather_data['current']['condition']['text'],
            'Date': weather_data['location']['localtime'],
            'feelslike_c':weather_data['current']['feelslike_c'],
            'feelslike_f':weather_data['current']['feelslike_f']
        }
    else:
        context['error'] = "City not found. Please try again."

    return render(request, 'weather/weather.html', context)

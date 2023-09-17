from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
import requests
from datetime import datetime


# Create your views here.

def index(request):
    return render(request, "index.html")


def weather(request):
    if request.method == 'POST':
        # Handle the form submission
        location = request.POST.get('location', '')  # Get the user's input
        api_key = settings.API_KEY

        if location:
            # Construct the API request URL
            url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}'

            response = requests.get(url)
            data = response.json()

            if data.get('cod') == 200:
                # Successfully retrieved weather data
                city_name = data.get('name')
                weather = data['weather'][0]['main']
                temperature = round(data['main']['temp'])
                description = data['weather'][0]['description']
                current_date = datetime.now().strftime("%A, %d %B %Y")

                context = {
                    'city': city_name,
                    'weather_condition': weather,
                    'temperature': temperature,
                    'description': description,
                    'current_date': current_date,
                }

                return render(request, 'weather.html', context)
            else:
                # Handle the case where the city is not found
                return render(request, 'weather.html', {'error_message': 'No City Found'})
        else:
            # Handle the case where the user didn't provide input
            return render(request, 'weather.html', {'error_message': 'Please enter a city name or pincode.'})
    else:
        # Render the initial weather input form
        return render(request, 'weather_form.html')

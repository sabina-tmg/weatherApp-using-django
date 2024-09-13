from django.shortcuts import render
import requests

def index(request):
    city = request.POST.get('city', 'kathmandu')  # Get city from POST, default to 'kathmandu'
    
    api_key = '376ff16eba1689cbe8a37244a102812b'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()  # Convert JSON response to Python dictionary

        # Extract temperature if the response is successful
        if data.get('cod') == 200:
            temp = data['main']['temp']
            desc=data['weather'][0]['description']
            wind_speed=data['wind']['speed']
            humidity=data['main']['humidity']
            
        else:
            temp = "City not found"
    except requests.exceptions.RequestException as e:
        temp = "Error: Unable to fetch data"
    
    return render(request, 'index.html', {'temp': temp,'city':city,'desc':desc,'wind_speed':wind_speed,'humidity':humidity})

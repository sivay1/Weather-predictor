from django.shortcuts import render
import json
import urllib.request
def IndexView(request):
	if request.method == 'POST':
		place = request.POST['place']
		result = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+place+'&appid=7f22fccfda442b9e83f9764c67ceef2e').read()
		json_data = json.loads(result)
		temperature_in_kelvin = float(json_data['main']['temp'])
		temperature_in_celsius = temperature_in_kelvin - 273.15
		temperature_in_celsius_str = f"{temperature_in_celsius:.2f}°C"

		data = {
			"country_code" : str(json_data['sys']['country']),
			"coordinate" : str(json_data['coord']['lon']) + ' ' +str(json_data['coord']['lat']),
			"temp" : temperature_in_celsius_str,
			"pressure" : str(json_data['main']['pressure']),
			"humidity" : str(json_data['main']['humidity']),
		}
	else:
		place = ''
		data = {}

	return render(request,'index.html',{'place':place,'data':data})


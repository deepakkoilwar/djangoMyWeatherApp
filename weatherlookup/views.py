from django.shortcuts import render

def home(request):
		import json
		import requests
		request.method == 'POST'
		CityName = request.POST['cityname']
		api_request = requests.get("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"+CityName+"?unitGroup=metric&key=9DJSBRXRLC97NMQC7KN83W6TF&contentType=json")
		try:
				api = json.loads(api_request.content)
		except Exception as e:
				api = "error"
		return render(request,'home.html',{'api' : api})

def about(request):
	return render(request,'about.html',{})	
	
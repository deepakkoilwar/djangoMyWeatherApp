from django.shortcuts import render

def home(request):
	import json
	import requests
	api_request = requests.get("http://dataservice.accuweather.com/currentconditions/v1/202396?apikey=LCCUpMujoA3AHLTxAlFA6DK0gIOBEhjB")
	try:
		api = json.loads(api_request.content)
	except Exception as e:
		api = "error"
	return render(request,'home.html',{'api' : api})

def about(request):
	return render(request,'about.html',{})	
	
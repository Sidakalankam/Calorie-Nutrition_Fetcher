from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    import requests
    import json

    if request.method == 'POST':
        query = request.POST.get('query')
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(api_url + query, headers={'X-Api-Key': 'Fxue3LKgKllpGVLmK3DvDw==RVolCBLnwgzcDfxw'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "oops! there was an error"
            print(e)
        return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'home.html', {'query': 'Enter a valid query'})



    


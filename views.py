from django.shortcuts import render
import requests

def index(request):
    if request.method == 'POST':
        Nationality = request.POST.get("Nationality")
        Name = request.POST.get("Name")
        api_url = f'http://127.0.0.1:8000//players/{Nationality}/{Name}'  # Replace with your API endpoint URL
        response = requests.get(api_url)
        playerdata = response.json()
        if response.status_code == 200:
            playerdata = response.json()
            return render(request, 'results.html', {'playerdata': playerdata})
        else:
            return render(request, 'index.html', {'message': 'Failed to fetch player results. Check Again!'})
    
        
    return render(request, 'index.html')




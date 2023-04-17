from django.shortcuts import render
from django.http import JsonResponse
from sql_functions import get_companies, get_prediction_short, get_prediction_medium, get_prediction_long
import json


def index(request):
    print("index")
    return render(request, 'earnings_data/index.html')

def home(request):
    # Get the list of companies from the context
    companies = get_companies()
    companies = json.loads(companies)
    companies = companies["info"]
    buffer = []
    for company in companies:
        buffer.append(company[0])
    companies = buffer
    
    return render(request, 'earnings_data/home.html', {
        'companies': companies
    })



def search(request):
    time_period = request.GET.get('time_period')
    company = request.GET.get('company')
    if time_period == "short":
        prediction = get_prediction_short(company)
        
    if time_period == "medium":
        prediction = get_prediction_medium(company)
    else:
        prediction = get_prediction_long(company)
    
    prediction = json.loads(prediction)
    print(prediction["info"])
    return JsonResponse({'results': prediction["info"]})
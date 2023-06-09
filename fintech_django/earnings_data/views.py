from django.shortcuts import render
from django.http import JsonResponse
from sql_functions import get_companies, get_prediction_short, get_prediction_medium, get_prediction_long, get_current
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
    company = request.GET.get("company")
    current_price = get_current(company)
    if time_period == "short" or time_period == "s":
        prediction = get_prediction_short(company)
    elif time_period == "medium" or time_period == "m":
        prediction = get_prediction_medium(company)
    else:
        # TODO: Having a "catch-all" else statement gives me the heebie-jeebies. We should return an error response if time_period isn't short, medium or long, and handle that on our webpage.
        prediction = get_prediction_long(company)
    
    prediction = json.loads(prediction)
    try:
        prediction = prediction["info"][0][1]
    except:
        print("Unable to get data from database")
    return JsonResponse({'company': company, 'timePeriod': time_period, 'prediction': prediction, 'currentPrice': current_price})
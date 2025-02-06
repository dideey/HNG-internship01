from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
import requests
from .math import isPrime, isPerfect, digit_sum, check_number_properties
# Create your views here.

@api_view(['GET'])
def classify_number(request):
    if 'number' not in request.query_params or request.query_params.get('number').isalpha():
        return JsonResponse({"number": "alphabet", "error": "true"}, status=400)
    number = request.query_params.get('number')
    number = int(number)
    is_prime = isPrime(number)
    is_perfect = isPerfect(number)
    properties = check_number_properties(number)
    digit_sum_ = digit_sum(number)

    #Fetching fun fact about the number
    fun_fact_response = requests.get(f"http://numbersapi.com/{number}/math") # Fun fact about the number
    fun_fact = fun_fact_response.text
    response = {
        "number": number,
        "is_prime": is_prime,
        "is_perfect": is_perfect,
        "properties": properties,
        "digit_sum": digit_sum_,
        "fun_fact": fun_fact
    }
    return JsonResponse(response, status=200)
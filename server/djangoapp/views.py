# server/djangoapp/views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import csrf_exempt
from .restapis import get_request, analyze_review_sentiments, post_review
import json
import logging

logger = logging.getLogger(__name__)

# ---------------------- LOGIN ----------------------
@csrf_exempt
def login_user(request):
    data = json.loads(request.body)
    username = data.get('userName')
    password = data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        return JsonResponse({"userName": username, "status": "Authenticated"})
    else:
        return JsonResponse({"userName": username, "status": "Invalid Credentials"})


# ---------------------- LOGOUT ----------------------
def logout_request(request):
    logout(request)
    return JsonResponse({"userName": ""})


# ---------------------- REGISTRATION ----------------------
@csrf_exempt
def registration(request):
    data = json.loads(request.body)
    username = data.get('userName')
    password = data.get('password')
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    email = data.get('email')

    if User.objects.filter(username=username).exists():
        return JsonResponse({"userName": username, "error": "Already Registered"})

    user = User.objects.create_user(
        username=username, first_name=first_name,
        last_name=last_name, password=password, email=email
    )
    login(request, user)
    return JsonResponse({"userName": username, "status": "Authenticated"})


# ---------------------- GET DEALERSHIPS ----------------------
def get_dealerships(request, state="All"):
    if state == "All":
        endpoint = "/fetchDealers"
    else:
        endpoint = f"/fetchDealers/{state}"

    dealerships = get_request(endpoint)
    return JsonResponse({"status": 200, "dealers": dealerships})


# ---------------------- GET DEALER REVIEWS ----------------------
def get_dealer_reviews(request, dealer_id):
    endpoint = f"/fetchReviews/dealer/{dealer_id}"
    reviews = get_request(endpoint)
    for review in reviews:
        sentiment = analyze_review_sentiments(review.get('review', ''))
        review['sentiment'] = sentiment.get("sentiment", "unknown")
    return JsonResponse({"status": 200, "reviews": reviews})


# ---------------------- ADD REVIEW ----------------------
@csrf_exempt
def add_review(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request method"}, status=400)

    if request.user.is_anonymous:
        return JsonResponse({"status": 403, "message": "Unauthorized"})

    data = json.loads(request.body)
    try:
        response = post_review(data)
        return JsonResponse({"status": 200, "response": response})
    except Exception as e:
        print("Error posting review:", e)
        return JsonResponse({"status": 401, "message": "Error in posting review"})

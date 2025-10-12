# Uncomment the required imports before adding the code

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
import logging
import json
# from .populate import initiate

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.

# ---------------------- LOGIN ----------------------
@csrf_exempt
def login_user(request):
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']

    user = authenticate(username=username, password=password)
    data = {"userName": username}
    if user is not None:
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}
    else:
        data = {"userName": username, "status": "Invalid Credentials"}

    return JsonResponse(data)

# ---------------------- LOGOUT ----------------------
def logout_request(request):
   
    logout(request)
    data = {"userName": ""}
    return JsonResponse(data)

# ---------------------- REGISTRATION ----------------------
@csrf_exempt
def registration(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data['userName']
        password = data['password']
        first_name = data.get('firstName', '')
        last_name = data.get('lastName', '')

        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Username already exists"}, status=400)
        else:
            user = User.objects.create_user(username=username,
                                            password=password,
                                            first_name=first_name,
                                            last_name=last_name)
            login(request, user)
            return JsonResponse({"userName": username, "status": "Registered & Logged In"})
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)

# ---------------------- GET DEALERSHIPS ----------------------
def get_dealerships(request):
    # Example data (replace with API call or DB fetch later)
    dealerships = [
        {"id": 1, "name": "Galaxy Motors", "city": "Hyderabad"},
        {"id": 2, "name": "Starline Autos", "city": "Bangalore"},
    ]
    return render(request, 'index.html', {"dealership_list": dealerships})

# ---------------------- GET DEALER REVIEWS ----------------------
def get_dealer_reviews(request, dealer_id):
    # Example review data
    reviews = [
        {"dealer_id": dealer_id, "name": "Gayathri", "review": "Great service!", "rating": 5},
        {"dealer_id": dealer_id, "name": "Ravi", "review": "Good experience.", "rating": 4},
    ]
    return render(request, 'dealer_reviews.html', {"reviews": reviews, "dealer_id": dealer_id})

# ---------------------- GET DEALER DETAILS ----------------------
def get_dealer_details(request, dealer_id):
    dealer_details = {"id": dealer_id, "name": "Galaxy Motors", "city": "Hyderabad"}
    return render(request, 'dealer_details.html', {"dealer": dealer_details})

# ---------------------- ADD REVIEW ----------------------
@csrf_exempt
def add_review(request):
    if request.method == "POST":
        data = json.loads(request.body)
        dealer_id = data.get("dealer_id")
        review = data.get("review")
        name = data.get("name", "Anonymous")

        # Here you’d save review to DB or external API
        logger.info(f"New review added by {name} for dealer {dealer_id}")

        return JsonResponse({"status": "Review added successfully"})
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)

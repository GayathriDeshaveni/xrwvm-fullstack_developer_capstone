# server/djangoapp/restapis.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url',
    default="http://localhost:3030"
).rstrip('/')

sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/"
).rstrip('/')


def get_request(endpoint, **kwargs):
    """
    Make GET request to backend API.
    Automatically handles trailing slashes and optional query parameters.
    Returns JSON or empty list/dict on failure.
    """
    if not endpoint.startswith('/'):
        endpoint = '/' + endpoint

    params = "&".join(f"{k}={v}" for k, v in kwargs.items())
    request_url = backend_url + endpoint
    if params:
        request_url += "?" + params

    print(f"GET from: {request_url}")

    try:
        response = requests.get(request_url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return []


def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url + "/analyze/" + text
    try:
        response = requests.get(request_url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Sentiment API failed: {e}")
        return {"sentiment": "unknown"}


def post_review(data_dict):
    request_url = backend_url + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Post review failed: {e}")
        return {"status": "error"}

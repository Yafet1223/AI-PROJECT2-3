from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json
import os
import sys

# Add myproject to path to import AI agent
myproject_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'myproject')
if myproject_path not in sys.path:
    sys.path.append(myproject_path)

try:
    from main import transform_text, UNIVERSE_STYLES
except ImportError as e:
    # Fallback if AI agent can't be imported
    UNIVERSE_STYLES = {
        "wizard": "Speak like a mystical medieval wizard",
        "robot": "Speak like a futuristic robot",
        "medieval knight": "Speak like a brave knight",
        "king": "Speak like a royal king",
        "sci-fi": "Speak like a futuristic sci-fi character"
    }
    def transform_text(text: str, universe: str) -> str:
        return f"Error: AI agent not properly configured. Please check your .env file and API key. Original error: {str(e)}"

def index(request):
    if request.user.is_authenticated:
        return render(request, "Pages/chat.html", {
            "universe_styles": list(UNIVERSE_STYLES.keys())
        })
    return render(request, "Pages/login.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "Pages/login.html", {
                "message": "Invalid Username and password."
            })
    else:
        return render(request, "Pages/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def signup_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "Pages/signup.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "Pages/signup.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "Pages/signup.html")

@csrf_exempt
def chat_api(request):
    """API endpoint for AI chat transformation"""
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Authentication required"}, status=401)
    
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            text = data.get("text", "")
            universe = data.get("universe", "wizard")
            
            if not text:
                return JsonResponse({"error": "Text is required"}, status=400)
            
            # Transform text using AI agent
            response_text = transform_text(text, universe)
            
            return JsonResponse({
                "original": text,
                "universe": universe,
                "response": response_text
            })
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    
    return JsonResponse({"error": "Method not allowed"}, status=405)


from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Chat
from django.utils import timezone
import time
import os
import google.generativeai as genai

gemini_api_key = 'your-api-key'


def ask_openai(message):
    genai.configure(api_key=gemini_api_key)

    # Create the model
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
    )

    chat_session = model.start_chat(
    history=[]
    )

    response = chat_session.send_message(message)
    return response.text

    

def chatbot(request):
    if not request.user.is_authenticated:
        # Redirect to login page if the user is not authenticated
        return redirect('register')
    
    chats = Chat.objects.filter(user = request.user)

    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        chat = Chat(user = request.user,message = message,response=response,created_at=timezone.now())
        chat.save()

        return JsonResponse({'message':message,'response':response})
    return render(request,'chatbot.html',{'chats':chats})


def login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('chatbot')
        else:
            error_message = 'Invalid Username or Password'
            return render(request,'login.html',{'error_message':error_message})
    else:
        return render(request,'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            try:
                user = User.objects.create_user(username,email,password1)
                user.save()
                auth.login(request,user)
                return redirect('chatbot')
            except:
                error_message = 'Error Creating Account'
                return render(request,'register.html',{'error_message':error_message})
        else:
            error_message = 'Password dont match'
            return render(request,'register.html',{'error_message':error_message})
        return render(request,'register.html')

    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

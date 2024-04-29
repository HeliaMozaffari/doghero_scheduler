from django.shortcuts import render
from django.http import HttpResponse
from .models import dog, owner
from django.template import RequestContext
import os
import datetime
import json
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]
def registration(request):
    dogs = dog.objects.all()
    owners = owner.objects.all()
    if request.method == 'POST':
        owner_name = request.POST['owner_name']
        owner_email = request.POST['owner_email']
        owner_number = request.POST['owner_number']
        owner_address = request.POST['owner_address']
        owner_emergency_name = request.POST['owner_emergency_name']
        owner_emergency_relation = request.POST['owner_emergency_relationship']
        owner_emergency_number = request.POST['owner_emergency_number']

        dog_name = request.POST['dog_name']
        dog_age = request.POST['dog_age']
        dog_breed = request.POST['dog_breed']
        dog_medical_notes = request.POST['dog_medical_notes']
        
        new_owner = owner(owner_name = owner_name, owner_email = owner_email, owner_number = owner_number, owner_address = owner_address, owner_emergency_name = owner_emergency_name, owner_emergency_relation = owner_emergency_relation, owner_emergency_number = owner_emergency_number)
        new_dog = dog(owner_number = owner_number, dog_name = dog_name, dog_age = dog_age, dog_breed = dog_breed, dog_medical_notes = dog_medical_notes)
        new_owner.save()
        new_dog.save()
    return render(request, 'registration.html',{"dog":dogs, "owner":owners }) 

def booking(request):
    return render(request, 'booking.html') 

def schedule(request):
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json")
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("C:/Users/Helia/Downloads/client_secret.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("calendar", "v3", credentials=creds)
        now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
        events_result = (
            service.events()
            .list(
                calendarId="primary",
                timeMin=now,
                maxResults=10,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )
        events = events_result.get("items", [])
    except HttpError as error:
        print(error)
    return render(request, 'schedule.html',{"events":events }) 
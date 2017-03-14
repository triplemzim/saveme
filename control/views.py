from django.shortcuts import render
from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import *
import json


# Create your views here.


def index(request):
	return HttpResponse('<h1> Game Over!</h1>')

@csrf_exempt
def signup(request):
	if request.method == 'POST':
		data_byte = request.body.decode('utf-8')
		data = json.loads(data_byte)
		print(data)
		username = data['username']
		password = data['password']
		contactno = data['contact']
		print('watch: ',username,password,contactno)
		
		
		dict = {}
		dict['status']='fail'
		try:
			user = User.objects.create_user(username = username,password = password)
		except Exception as e:
			dict['status']='fail1'	
			return HttpResponse(json.dumps(dict))
		
		try:	
			profile = Profile()
			profile.user=user
			profile.contactno=contactno
		except Exception as e:
			print('cant create profile')
		
		
		try:
			profile.save()
		except Exception as e:
			user.delete()
			return HttpResponse(json.dumps(dict))
		
		
		user = authenticate(username = username,password = password)	
		if user is not None:
			login(request,user)
			dict['status']='success'
			data = json.dumps(dict)
			return HttpResponse(data)
		else: 
			print("no User found")
		
		dict['status']='fail'
		data = json.dumps(dict)
		return HttpResponse(data)
		
		
		

@csrf_exempt
def LOGIN(request):
	if request.method == 'POST':
		data_byte=request.body.decode('utf-8')
		data=json.loads(data_byte)
		print(data)
		dict = {}
		username = data['username']
		password = data['password']
		print(username,password)
		user = authenticate(username=username,password=password)
		if user is not None:
			login(request,user)
			print('success')
			dict['status']='success'
			data = json.dumps(dict)
			return HttpResponse(data)
		else:
			dict['status']='fail'
			return HttpResponse(json.dumps(dict))
		
		
@csrf_exempt
def save_data(request):
	if request.method == 'POST':
		data_byte = request.body.decode('utf-8')
		data=json.loads(data_byte)

		dict = {}

		print(data)
		user = data['username']
		message = data['message']
		contactno = data['contact']
		sendTime = data['time']
		
		print(sendTime)
		
		
		messageData = MessageData()
		messageData.user = User.objects.get(username = user)
		messageData.message = message
		messageData.contactno = contactno
		messageData.sendTime = sendTime
		
		print("messageData: ",messageData)

		try:
			messageData.save()
			dict['status']='success'
			data = json.dumps(dict)
			return HttpResponse(data)
		except Exception as e:
			print(sendTime)
			print("you failed me")
			dict['status']='fail'
			data = json.dumps(dict)
			return HttpResponse(data)
	
	
	
	
	

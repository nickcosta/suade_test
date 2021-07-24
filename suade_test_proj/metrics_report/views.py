from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return HttpResponse('<h1>Suade test home</h1>')

def report(request):
	return HttpResponse('<h1>Suade test report</h1>')

from django.shortcuts import render

def method(request):
	return render(request, 'index.html')
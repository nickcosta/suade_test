from django.shortcuts import render
from .models import Order
import json 


test_data = {
				'firstname' : 'Nick',
				'secondname' : 'Costa',
				'title' : 'Mr',
				'ammount' : '2000',
				'total' : '2352'
			}

json_object = json.dumps(test_data, indent = 4)  



def home(request):
	return render(request, 'metrics_report/home.html')

def report(request):
	context = {
		'json': Order.objects.all(),
		'title': 'Metrics Report Data'

	}
	return render(request, 'metrics_report/report.html', context)

from django.shortcuts import render 


test_data = [
	{
		'firstname' : 'Nick',
		'secondname' : 'Costa',
		'title' : 'Mr',
		'ammount' : '2000',
		'total' : '2352',
	},
	{
		'firstname' : 'Sarah',
		'secondname' : 'Tomms',
		'title' : 'Mrs',
		'ammount' : '1389',
		'total' : '67',
	}
]

def home(request):
	return render(request, 'metrics_report/home.html')

def report(request):
	context = {
		'posts': test_data,
		'title': 'Metrics Report Data'

	}
	return render(request, 'metrics_report/report.html', context)

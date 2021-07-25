from django.shortcuts import render
from .models import Order, OrderLine, VendorCommisions
from django.db.models import Sum, Avg
import json 

def home(request):
	return render(request, 'metrics_report/home.html')

def result(request, date):
	customer_count_data = Order.objects.filter(created_at=date).count()
	pk_list = list(Order.objects.filter(created_at=date).values_list('pk', flat=True))
	#sort out the below two
	order_vid_list = list(Order.objects.filter(created_at=date).values_list('vendor_id', flat=True))
	rate_list = VendorCommisions.objects.filter(vendor_id__in=order_vid_list).values_list('vendor_id')
	rate_list2 = VendorCommisions.objects.filter(vendor_id__in=order_vid_list)

	linked_day_vid_list = list(Order.objects.filter(vendor_id__in=order_vid_list).values_list('pk', flat=True))
	linked_day_vid_list2 = list(Order.objects.filter(pk__in=linked_day_vid_list, vendor_id__in=rate_list).values_list('pk', flat=True))

	items_count_data = list(OrderLine.objects.filter(order_id__in=pk_list).aggregate(Sum('quantity')).values())[0]
	dicounted_amount_data = list(OrderLine.objects.filter(order_id__in=pk_list).aggregate(Sum('dicounted_amount')).values())[0]
	average_discount_rate = list(OrderLine.objects.filter(order_id__in=pk_list).aggregate(Avg('discount_rate')).values())[0]
	average_order_total = list(OrderLine.objects.filter(order_id__in=pk_list).aggregate(Avg('total_amount')).values())[0]

	total_commisson = 0
	tcsum = 0
	for rate in rate_list2:
		for ordid in order_vid_list:
			if rate == ordid:
				for price in full_price_list:
					if rate.order_id == ordid:
							tcsum = rate.rate * price.full_price_amount
							total_commisson += tcsum
	print("total added = "+str(total_commisson))
	#from this I can get the correct rates
	
	#date
	#vendor_id
	#rate

	print(len(rate_list))

	#from this I can get the correct full prices
	full_price_list = OrderLine.objects.filter(order_id__in=linked_day_vid_list2).values_list('full_price_amount')
	#order_id
	#product_id
	#full_price

	print(len(full_price_list))


	context = {
		'customers': customer_count_data,
		'items': items_count_data,
		'discount': dicounted_amount_data,
		'avg_discount': average_discount_rate,
		'avg_ord_total': average_order_total,
		'full_price_list': full_price_list,
		'title': 'Metrics Report Data',
		'date': date
		}
	return render(request, 'metrics_report/report.html', context)

def report(request):
	context = {
		'json': Order.objects.values(),
		'title': 'Metrics Report Data'
		}
	return render(request, 'metrics_report/report.html', context)

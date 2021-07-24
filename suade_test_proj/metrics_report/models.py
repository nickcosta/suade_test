from django.db import models

class Order(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	vendor_id = models.IntegerField()
	customer_id = models.IntegerField()


class Product(models.Model):
	description = models.CharField(max_length=255)

class Promotion(models.Model):
	description = models.CharField(max_length=255)

class ProductPromotion(models.Model):
	date = models.DateTimeField()
	product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
	promotion_id = models.ForeignKey(Promotion, on_delete=models.CASCADE)

class VendorCommisions(models.Model):
	date = models.DateTimeField()
	vendor_id = models.IntegerField()
	rate = models.DecimalField(max_digits=8, decimal_places=2)

class OrderLine(models.Model):
	order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
	product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
	product_description = models.CharField(max_length=255)
	product_price = models.DecimalField(max_digits=8, decimal_places=2)
	product_vat_rate = models.DecimalField(max_digits=3, decimal_places=2)
	discount_rate = models.IntegerField()
	quantity = models.IntegerField()
	full_price_amount = models.DecimalField(max_digits=8, decimal_places=2)
	dicounted_amount = models.DecimalField(max_digits=8, decimal_places=2)
	vat_amount = models.IntegerField()
	total_amount = models.IntegerField()
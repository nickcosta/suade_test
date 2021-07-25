from django.db import models

class Order(models.Model):
	created_at = models.DateField()
	vendor_id = models.IntegerField()
	customer_id = models.IntegerField()

	def __str__(self):
		return f'{self.created_at} {self.vendor_id} {self.customer_id}'
		

class Product(models.Model):
	description = models.CharField(max_length=255)

	def __str__(self):
		return f'{self.description}'

class Promotion(models.Model):
	description = models.CharField(max_length=255)

	def __str__(self):
		return f'{self.description}'
class ProductPromotion(models.Model):
	date = models.DateField()
	product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
	promotion_id = models.ForeignKey(Promotion, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.date} {self.product_id} {self.promotion_id}'

class VendorCommisions(models.Model):
	date = models.DateTimeField(blank=False)
	vendor_id = models.IntegerField()
	rate = models.DecimalField(max_digits=8, decimal_places=2)

	def __str__(self):
		return f'{self.date} {self.vendor_id} {self.rate}'

class OrderLine(models.Model):
	order_id = models.IntegerField()
	product_id = models.IntegerField()
	product_description = models.CharField(max_length=255)
	product_price = models.DecimalField(max_digits=16, decimal_places=2)
	product_vat_rate = models.DecimalField(max_digits=3, decimal_places=2)
	discount_rate = models.IntegerField()
	quantity = models.IntegerField()
	full_price_amount = models.DecimalField(max_digits=16, decimal_places=2)
	dicounted_amount = models.DecimalField(max_digits=16, decimal_places=2)
	vat_amount = models.IntegerField()
	total_amount = models.IntegerField()

	def __str__(self):
		return f'''{self.order_id} {self.product_id} {self.product_description} {self.product_price} {self.product_vat_rate} {self.discount_rate}'''
		f'''{self.quantity} {self.full_price_amount} {self.dicounted_amount} {self.vat_amount} {self.total_amount}'''

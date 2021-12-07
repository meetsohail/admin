from django.db import models


CHOICES_LIST = (('daily', 'Daily'), ('twiceaday', 'Twice a Day'), ('hourly', 'Hourly'), ('sixhours', 'Six Hours'))  
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_description = models.TextField(null=True, blank=True)
    product_price = models.FloatField()
    product_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    product_stripe_id = models.CharField(max_length=300, blank=True, null=True)
    product_stripe_price_id = models.CharField(max_length=300, blank=True, null=True)
    featured = models.BooleanField(default=False, null=True, blank=True)
    max_keywords = models.IntegerField(default=0)
    max_results = models.IntegerField(default=0)
    max_countries = models.IntegerField(default=0)
    check_interval = models.CharField(max_length=20, choices=CHOICES_LIST, default='daily')
    realtime_checks = models.IntegerField(default=0)
    multiple_devices = models.BooleanField(default=False)
    
    def __str__(self):
        return self.product_name

from django.db import models
from apps.order.models import Order
from apps.product.models import Product

class Order_items(models.Model):
    order_item_id = models.IntegerField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)  
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
   
    
    class Meta:
        db_table = "order_items"
        
    def __str__(self):
        return self.name

from django.db import models
from apps.clients.models import Customer

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  
    order_date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
   
    
    class Meta:
        db_table = "order"
        
    def __str__(self):
        return f"Order{self.order_id}" 

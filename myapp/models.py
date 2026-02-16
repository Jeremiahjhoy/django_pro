from django.db import models

class InventoryItem(models.Model):
    name = models.CharField(max_length=200)               # Item name
    description = models.TextField(blank=True, null=True) # Item description
    quantity = models.PositiveIntegerField(default=0)     # Number of items in stock
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Item price
    created_at = models.DateTimeField(auto_now_add=True)  # Auto timestamp when added
    updated_at = models.DateTimeField(auto_now=True)      # Auto timestamp when updated
    is_active = models.BooleanField(default=True)        # If item is active/available

    def __str__(self):
        return self.name

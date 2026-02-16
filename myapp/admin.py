from django.contrib import admin
from .models import InventoryItem  # import your Task model 

# Register the model
admin.site.register(InventoryItem)
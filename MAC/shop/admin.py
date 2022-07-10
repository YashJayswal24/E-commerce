from django.contrib import admin
from. models import product
from .models import Contact
from .models import Orders
from .models import OrderUpdate
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "pub_date", "price","image")
admin.site.register(product,ProductAdmin)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)



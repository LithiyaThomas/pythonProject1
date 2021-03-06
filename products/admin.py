from django.contrib import admin
from .models import Dealer
from .models import Employee
from .models import Customer
from .models import Medicine
from .models import Purchase
from .models import Stock
from .models import Sale
# Register your models here.p
class DealerAdmin(admin.ModelAdmin):
    list_display = ('dname', 'address', 'phn_no', 'email')
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'address', 'email', 'sal', 'phn_no')
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'address', 'phn_no', 'email')
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('mname', 'm_id', 'dname', 'desc', 'price', 'stock1', 'manu', 'expir')
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('pname', 'fname', 'phn_no', 'price', 'qty')
class StockAdmin(admin.ModelAdmin):
    list_display = ('medicine', 'sto_qty')
class SaleAdmin(admin.ModelAdmin):
    list_display = ('medicine', 'customer', 'saledate', 'saqty', 'saprice')


admin.site.register(Dealer, DealerAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Medicine, MedicineAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Sale, SaleAdmin)

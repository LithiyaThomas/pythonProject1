from django.contrib import admin
from .models import Dealer
from .models import Employee
from .models import Customer
from .models import Medicine
from .models import Purchase

# Register your models here.
class DealerAdmin(admin.ModelAdmin):
    list_display = ('dname', 'address', 'phn_no', 'email')
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('fname', 'address', 'sal', 'phn_no')
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('fname','address','phn_no')
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('mname','dname','desc','price','stock')
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('pname','fname','price','qty')
admin.site.register(Dealer,DealerAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Medicine,MedicineAdmin)
admin.site.register(Purchase,PurchaseAdmin)
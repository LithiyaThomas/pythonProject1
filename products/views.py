from .models import Dealer
from .models import Employee
from .models import Customer
from .models import Medicine
from .models import Purchase
from .models import Stock
from django.shortcuts import render
from django.db import IntegrityError



def home(request):
    return render(request, 'products/index.html')


def dealerform(request):
    dict = {'add': True, }
    return render(request, 'products/dealer.html', dict)


def dealerforminsert(request):
    try:
        dealer = Dealer()
        dealer.dname = request.POST['dname']
        dealer.address = request.POST['address']
        dealer.phn_no = request.POST['pno']
        dealer.email = request.POST['email']
        dealer.save()

    except IntegrityError:
        return render(request, "products/new.html")
    return render(request, 'products/index.html')


def dealerformupdate(request, foo):
    try:
        dealer = Dealer.objects.get(pk=foo)
        dealer.dname = request.POST['dname']
        dealer.address = request.POST['address']
        dealer.phn_no = request.POST['pno']
        dealer.email = request.POST['email']
        dealer.save()
    except IntegrityError:
        return render(request, "products/new.html")
    return render(request, 'products/index.html')


def dealerformview(request, foo):
    dealer = Dealer.objects.get(pk=foo)
    dict = {'dealer': dealer}
    return render(request, 'products/dealer.html', dict)


def dealerformdelete(request, foo):
    dealer = Dealer.objects.get(pk=foo)
    dealer.delete()
    return render(request, 'products/index.html')


def dealertable(request):
    dealer = Dealer.objects.all()
    dict = {"dealer": dealer}
    return render(request, 'products/dealertable.html', dict)


def empform(request):
    dict = {'add': True}
    return render(request, 'products/emp.html', dict)


def empforminsert(request):
    try:
        emp = Employee()
        emp.e_id = request.POST['eid']
        emp.fname = request.POST['fname']
        emp.lname = request.POST['lname']
        emp.address = request.POST['address']
        emp.phn_no = request.POST['pno']
        emp.email = request.POST['email']
        emp.sal = request.POST['sal']

        emp.save()
    except IntegrityError:
        return render(request, "products/new.html")
    return render(request, 'products/index.html')


def empformupdate(request, foo):
    try:
        emp = Employee.objects.get(pk=foo)
        emp.e_id = request.POST['eid']
        emp.fname = request.POST['fname']
        emp.lname = request.POST['lname']
        emp.address = request.POST['address']
        emp.phn_no = request.POST['pno']
        emp.email = request.POST['email']
        emp.sal = request.POST['sal']

        emp.save()
    except IntegrityError:
        return render(request, "products/new.html")
    return render(request, 'products/index.html')


def empformview(request, foo):
    emp = Employee.objects.get(pk=foo)
    dict = {'emp': emp}
    return render(request, 'products/emp.html', dict)


def empformdelete(request, foo):
    emp = Employee.objects.get(pk=foo)
    emp.delete()
    return render(request, 'products/index.html')


def emptable(request):
    emp = Employee.objects.all()
    dict = {"emp": emp}
    return render(request, 'products/emptable.html', dict)


def custform(request):
    dict = {'add': True}
    return render(request, 'products/cust.html', dict)


def custforminsert(request):
    try:
        cust = Customer()
        cust.fname = request.POST['fname']
        cust.lname = request.POST['lname']
        cust.address = request.POST['address']
        cust.phn_no = request.POST['pno']
        cust.email = request.POST['email']
        cust.save()
    except IntegrityError:
        return render(request, "products/new.html")
    return render(request, 'products/index.html')


def custformupdate(request, foo):
    try:
        cust = Customer.objects.get(pk=foo)
        cust.fname = request.POST['fname']
        cust.lname = request.POST['lname']
        cust.address = request.POST['address']
        cust.phn_no = request.POST['pno']
        cust.email = request.POST['email']
        cust.save()
    except IntegrityError:
        return render(request, "products/new.html")
    return render(request, 'products/index.html')


def custformview(request, foo):
    cust = Customer.objects.get(pk=foo)
    dict = {'cust': cust}
    return render(request, 'products/cust.html', dict)


def custformdelete(request, foo):
    cust = Customer.objects.get(pk=foo)
    cust.delete()
    return render(request, 'products/index.html')


def custtable(request):
    cust = Customer.objects.all()
    dict = {"cust": cust}
    return render(request, 'products/custtable.html', dict)


def medform(request):
    dict = {'add': True}
    return render(request, 'products/med.html', dict)


def medforminsert(request):
    try:
        med = Medicine()
        med.mname = request.POST['mname']
        med.m_id = request.POST['mid']
        med.dname = request.POST['dname']
        med.desc = request.POST['desc']
        med.price = request.POST['price']
        med.stock1 = request.POST['stock1']
        med.manu = request.POST['manu']
        med.expir = request.POST['expir']
        med.save()
    except IntegrityError:
        return render(request, "products/new.html")
    return render(request, 'products/index.html')


def medformupdate(request, foo):
    try:
        med = Medicine.objects.get(pk=foo)
        med.m_id = request.POST['mid']
        med.mname = request.POST['mname']
        med.dname = request.POST['dname']

        med.desc = request.POST['desc']
        med.price = request.POST['price']
        med.stock1 = request.POST['stock1']
        med.save()
    except IntegrityError:
        return render(request, "products/new.html")
    return render(request, 'products/index.html')


def medformview(request, foo):
    med = Medicine.objects.get(pk=foo)
    dict = {'med': med}
    return render(request, 'products/med.html', dict)


def medformdelete(request, foo):
    med = Medicine.objects.get(pk=foo)
    med.delete()
    return render(request, 'products/index.html')


def medtable(request):
    med = Medicine.objects.all()
    dict = {"med": med}
    return render(request, 'products/medtable.html', dict)


def purchaseform(request):
    dict = {'add': True}
    return render(request, 'products/purchase.html', dict)


def purchaseforminsert(request):
    try:
        purchase = Purchase()
        purchase.pname = request.POST['pname']
        purchase.fname = request.POST['fname']
        purchase.phn_no = request.POST['pno']
        purchase.qty = request.POST['qty']
        purchase.price = request.POST['price']
        purchase.save()
    except IntegrityError:
        return render(request, "products/new.html")
    return render(request, 'products/index.html')


def purchaseformupdate(request, foo):
    try:
        purchase = Purchase.objects.get(pk=foo)
        purchase.pname = request.POST['pname']
        purchase.fname = request.POST['fname']
        purchase.phn_no = request.POST['pno']
        purchase.qty = request.POST['qty']
        purchase.price = request.POST['price']
        purchase.save()
    except IntegrityError:
        return render(request, "products/new.html")
    return render(request, 'products/index.html')


def purchaseformview(request, foo):
    purchase = Purchase.objects.get(pk=foo)
    dict = {'purchase': purchase}
    return render(request, 'products/purchase.html', dict)


def purchaseformdelete(request, foo):
    purchase = Purchase.objects.get(pk=foo)
    purchase.delete()
    return render(request, 'products/index.html')


def purchasetable(request):
    purchase = Purchase.objects.all()
    dict = {"purchase": purchase}
    return render(request, 'products/purchasetable.html', dict)

def stockform(request):
    dict = {'add': True}
    return render(request, 'products/stock.html', dict)

def stockforminsert(request):
    try:
        stock = Stock()
        stock.mename = request.POST['mename']
        stock.sto_qty = request.POST['sto_qty']

        stock.save()
    except IntegrityError:
        return render(request, "products/new.html")
    return render(request, 'products/index.html')


def stockformupdate(request, foo):
    try:
        stock = Stock.objects.get(pk=foo)
        stock.mename = request.POST['mename']
        stock.save()
    except IntegrityError:
        return render(request, "products/new.html")
    return render(request, 'products/index.html')


def stockformview(request, foo):
    stock = Stock.objects.get(pk=foo)
    dict = {'stock': stock}
    return render(request, 'products/stock.html', dict)


def stockformdelete(request, foo):
    stock = Stock.objects.get(pk=foo)
    stock.delete()
    return render(request, 'products/index.html')


def stocktable(request):
    stock = Stock.objects.all()
    dict = {"stock": stock}
    return render(request, 'products/stocktable.html', dict)




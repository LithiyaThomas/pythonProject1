from django.db import models



# Create your models here.
class Dealer(models.Model):
    dname = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    phn_no = models.BigIntegerField(unique=True)
    email = models.EmailField(max_length=40)

    def __str__(self):
        return self.email


class Employee(models.Model):
    e_id = models.IntegerField(unique=True)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    sal = models.CharField(max_length=20)
    phn_no = models.BigIntegerField(unique=True)

    def __str__(self):
        return self.email


class Customer(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    phn_no = models.BigIntegerField()
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.email


class Medicine(models.Model):
    mname = models.CharField(max_length=100)
    m_id = models.CharField(max_length=30)
    dname = models.CharField(max_length=30)
    desc = models.CharField(max_length=50)

    price = models.CharField(max_length=30)
    stock1 = models.IntegerField()
    manu = models.DateField(auto_now_add=True)
    expir = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.mname


class Purchase(models.Model):
    pname = models.CharField(max_length=30)
    fname = models.CharField(max_length=30)
    phn_no = models.DateField()
    price = models.BigIntegerField()
    qty = models.BigIntegerField()

    def __str__(self):
        return self.pname

class Stock(models.Model):
    mename = models.ForeignKey(Medicine,on_delete=models.CASCADE)
    sto_qty = models.BigIntegerField()

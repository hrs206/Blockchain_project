from django.db import models
import datetime

class Accounts(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    is_customer = models.BooleanField()
    is_superuser = models.BooleanField()
    address = models.CharField(max_length=50, default="None")

class Transactions(models.Model):
    sender = models.ForeignKey(Accounts, on_delete=models.PROTECT)
    recipient = models.CharField(max_length=100)
    amount = models.CharField(max_length=30)
    date_time = models.DateTimeField(auto_now_add=True)

class Loyalty_Programs(models.Model):
    owner = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    program_name = models.CharField(max_length=50)
    program_desc = models.CharField(max_length=250)
    date = models.DateField(auto_now_add=True)
    price = models.CharField(max_length=50)

class LP_Map(models.Model):
    program = models.ForeignKey(Loyalty_Programs, on_delete=models.CASCADE)
    customer= models.ForeignKey(Accounts, on_delete=models.CASCADE)

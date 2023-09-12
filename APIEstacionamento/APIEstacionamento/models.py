from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=50)
    card_id = models.CharField(null=True, max_length=10)

class Vehicle(models.Model):
    plate = models.CharField(max_length=10)
    model = models.CharField(null=True, max_length=30)
    description = models.CharField(null=True, max_length=50)
    customer_id = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)

class Plan(models.Model):
    description = models.CharField(max_length=50)
    value = models.FloatField()

class Customer_Plan(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    plan_id = models.ForeignKey(Plan, on_delete=models.CASCADE)
    due_date = models.DateTimeField(auto_now_add=True)

class Contract(models.Model):
    description = models.CharField(max_length=50)
    max_value = models.FloatField(null=True)

class Contract_Rule(models.Model):
    contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE)
    until = models.IntegerField()
    until2 = models.IntegerField()
    max_value = models.FloatField(null=True)
    value = models.FloatField()

class ParkMovement(models.Model):
    entry_date = models.DateTimeField(auto_now_add=True, null=True)
    exit_date = models.DateTimeField(auto_now_add=True)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    value = models.FloatField()

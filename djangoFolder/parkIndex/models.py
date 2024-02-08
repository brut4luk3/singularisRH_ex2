import uuid
import random
import string
from django.db import models

def generate_random_alphanumeric(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_customer_id(name):
    random_part = generate_random_alphanumeric(10 - len(name))
    return name[:10-len(random_part)] + random_part

def generate_vehicle_id(model):
    model_part = model[:3]
    random_part = generate_random_alphanumeric(10 - len(model_part))
    return model_part + random_part

class Customer(models.Model):
    id = models.CharField(max_length=10, primary_key=True, default=generate_random_alphanumeric)
    cus_name = models.CharField(max_length=50)
    cus_card_id = models.CharField(max_length=10, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = generate_customer_id(self.name)
        super(Customer, self).save(*args, **kwargs)

    class Meta:
        db_table = 'tb_customer'

class Vehicle(models.Model):
    id = models.CharField(max_length=10, primary_key=True, default=generate_random_alphanumeric)
    vehicle_plate = models.CharField(max_length=10)
    vehicle_model = models.CharField(max_length=30, null=True, blank=True)
    vehicle_description = models.CharField(max_length=50, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = generate_vehicle_id(self.model)
        super(Vehicle, self).save(*args, **kwargs)

    class Meta:
        db_table = 'tb_vehicle'

class Plan(models.Model):
    plan_description = models.CharField(max_length=50)
    plan_value = models.FloatField()

    def __str__(self):
        return self.plan_description

    class Meta:
        db_table = 'tb_plan'

class CustomerPlan(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    due_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.plan

    class Meta:
        db_table = 'tb_customer_plan'

class Contract(models.Model):
    contract_description = models.CharField(max_length=50)
    contract_max_value = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.contract_description

    class Meta:
        db_table = 'tb_contract'

class ContractRule(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    until = models.IntegerField()
    value = models.FloatField()

    def __str__(self):
        return self.until

    class Meta:
        db_table = 'tb_contract_rule'

class ParkMovement(models.Model):
    entry_date = models.DateTimeField()
    exit_date = models.DateTimeField(null=True, blank=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    value = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.exit_date

    class Meta:
        db_table = 'tb_park_movement'
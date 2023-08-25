from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=128,editable=True,null=True)
    description = models.CharField(max_length=200,editable=True,blank=True,null=True)
    availability = models.BooleanField(default=True,editable=True)
    created = models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=True,null=True)
    deleted = models.BooleanField(default=False,editable=True)

    def __str__(self):
        return self.cat_name
    


    
class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    subcategory_name = models.CharField(max_length=128,editable=True)
    description = models.CharField(max_length=200,editable=True,null=True,blank=True)
    availability = models.BooleanField(default=True,editable=True, null=True)
    created = models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=True,null=True)
    deleted = models.BooleanField(default=False,editable=True)

    # def __str__(self):
    #     return self.subcat
    


class Inventory(models.Model):
    barcode = models.CharField(max_length=24,unique=True,editable=True)
    product_name = models.CharField(max_length=264,editable=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE) 
    description = models.CharField(max_length=200,blank=True, null=True,editable=True)
    gst = models.FloatField( null=True,editable=True)
    available = models.BooleanField(default=True,editable=True)
    min_level = models.IntegerField(null=True,editable=True)
    delivery_within = models.DateField(blank=True,null=True,editable=True)
    created = models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=True,null=True)
    deleted = models.BooleanField(default=False,editable=True)

    def __str__(self): 
        return self.product
    
class Addcart(models.Model):
    colour = models.CharField(max_length=264,editable=True)
    size = models.CharField(max_length=10, editable=True)
    quantity = models.IntegerField(null=True,editable=True)
    deleted = models.BooleanField(null = True, editable=True, default=False)
    
    def __str__(self): 
        return self.addcart
 
#one to onw relation    
class Ratings(models.Model):
    likes = models.IntegerField()
    dislikes = models.IntegerField()
# one to one relation  
class Dress(models.Model):
    cloth_name = models.CharField(max_length=20)
    quantity_sold = models.IntegerField()
    rates = models.OneToOneField(Ratings, on_delete=models.CASCADE)

class Spec(models.Model):
    model_name = models.CharField(max_length=50)
    color = models.CharField(max_length=50) 
    top_speed = models.IntegerField()
    fuel = models.CharField(max_length=50) 
    engine_cc = models.IntegerField()
    
class Bike(models.Model):
    details = models.ForeignKey(Spec, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50)
    launched_year = models.IntegerField()

class Students(models.Model):
    name = models.CharField(max_length=50)
    roll_num = models.IntegerField()
    
class User(models.Model):
    identity = models.IntegerField()
    qualification = models.CharField(max_length=50)
    experiance = models.IntegerField()

# models.py
from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField()

# serializers.py
from rest_framework import serializers

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField()
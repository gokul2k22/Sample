from .models import Category , SubCategory, Inventory, Addcart, Ratings, Dress, Spec, Bike, Students, User, Users
#, ProductDetails
from rest_framework import serializers

#Category

class Category_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'category_name', 'availability','description','created','updated','deleted')



#SubCategory 
class SubCategory_dataSerializer(serializers.ModelSerializer):
    #category_name = serializers.CharField(source='category.category_name', read_only=True)

    class Meta:
        model = SubCategory
        fields = ('id','category_id', 'subcategory_name','availability','description','created','updated','deleted')

#inventory
class Inventory_dataserializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('id','barcode','product_name','subcategory','description','gst','available','min_level','delivery_within','created','updated','deleted')


#add Cart
class Addcart_dataserializer(serializers.ModelSerializer):
    class Meta:
        model = Addcart
        fields = ('id','colour','size','quantity')
        
#ratings
#ONE TO ONE RELATION
class  Dress_seralizer(serializers.ModelSerializer):
    class Meta:
        model = Dress
        fields = ('id','cloth_name','quantity_sold','rates')

class Rating_serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ratings
        fields = ('id','likes','dislikes')
        
        
class Bike_serializer(serializers.ModelSerializer):
    class Meta:
        model = Bike
        fields = ('id','company_name','launched_year','details')

class BikeSpec_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Spec
        fields = ('id','color','top_speed','fuel','engine_cc','model_name')

class Student_serializer(serializers.ModelSerializer):
    class Meta:
        model= Students
        fields = ('id','name','roll_num')
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','identity','qualification','experiance')



class User_Serializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    
    def create(self, validated_data):
        return Users.objects.create(**validated_data)
     
    def get(self):
        return Users.objects.all()
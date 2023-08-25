from django.shortcuts import render
from django.views import View
import json
from django.http import JsonResponse
from .models import Category, SubCategory, Inventory, Addcart, Dress, Ratings, Spec, Bike, Students, User
from .serializer import Category_dataSerializer, SubCategory_dataSerializer, Inventory_dataserializer, Addcart_dataserializer,UserSerializer, Student_serializer, Rating_serializer,Bike_serializer,BikeSpec_Serializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAdminUser
# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class CategoryView(View):
    
    def get(self, request, *args, **kwargs):
        queryset = Category.objects.filter(deleted = False)
        serializer = Category_dataSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    def post(self, request, *args, **kwargs):
        
        response = self.create_category(json.loads(request.body))
        return JsonResponse({'message': response}, safe=False)
    
    
    @staticmethod
    def create_category(form):
        try:
            category_name = form.get('category_name')
            description = form.get('description')
            availability = form.get('availability')  # Set default value if availability is not provided
            
            if not category_name or not description or not availability:
               return 'Please enter valid information'
            
            else:
                category_name!=""
                category_obj = Category(category_name=category_name, description=description, availability=availability)
                category_obj.save()
                return 'Category created successfully'
            
            
        except Exception as e:
            return str(e)
        
    def put(self, request, *args, **kwargs):
        response = self.update_category(json.loads(request.body))
        return JsonResponse({'message': response}, safe=False)

    @staticmethod
    def update_category(form):
        category_id = form.get('category_id')
        category_name = form.get('category_name')
        description = form.get('description')
        availability = form.get('availability')
        
        if not category_name or not description or availability is None:
            return 'Please enter valid information'

        try:
            category_obj = Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            return 'Please enter valid category id'

        category_obj.category_name = category_name
        category_obj.availability = availability
        category_obj.description = description
        category_obj.save()
        return 'Successfully Updated'

    def delete(self, request, *args, **kwargs):
        data = self.delete_category(json.loads(request.body))
        return JsonResponse({'message':data}, safe=False)
        
    @staticmethod
    def delete_category(form):
        category_id = form.get('category_id')
        if not category_id:
            return 'send valid name'
            
        
        try:
            category_obj = Category.objects.get(pk=category_id)
            
            category_obj.deleted = True
            category_obj.save()
            return 'success'
        except Category.DoesNotExist:
            return 'Please enter valid category id'
        


#subcategory
@method_decorator(csrf_exempt, name='dispatch')
class SubCategoryView(View):
    def get(self, request, *args, **kwargs):
        data = SubCategory.objects.filter(deleted=False)
        serializer = SubCategory_dataSerializer(data, many=True)
        
        return JsonResponse(serializer.data, safe=False)
    
    def post(self, request, *args, **kwargs):
        
        data = self.create_subcat(json.loads(request.body))
        return JsonResponse({'message': data}, safe=False)
    
    @staticmethod
    def create_subcat(form):
        result = ''
        category_id = form.get('category_id')
        subcategory_name = form.get('subcategory_name')
        description = form.get('description')
        availability = form.get('availability')

        if not category_id or not subcategory_name or not description or availability is None:
            return 'Please send valid data'

        try:
            category = Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            return 'Category does not exist'

        if category.deleted:  # Check if the category is deleted
            return 'Cannot create subcategory for a deleted category'

        try:
            subcategory_obj = SubCategory(category_id=category_id, subcategory_name=subcategory_name, description=description, availability=availability)
            subcategory_obj.save()
            return 'SubCategory created successfully'

        except Exception as e:
            print(e.args)
            return 'Please check the data'

        
    
    def put(self, request, *args, **kwargs):
        data = self.update_subcat(json.loads(request.body))
        return JsonResponse({'message': data}, safe=False) 

                
    @staticmethod
    def update_subcat(form):
        subcategory_id = form.get('subcategory_id')
        subcategory_name = form.get('subcategory_name')
        description= form.get('description')
        availability= form.get('availability')
       

        if not subcategory_id:
            return 'Please send  valid name'
        try:
            if not subcategory_name:
                return 'please check name'
            elif not description:
                return 'pls check name'
            # if not subcategory_id or not subcategory_name or not description or not availability:
            #     return 'Please send a name'
            
            else:    # Get the subcategory object
                subcategory_obj = SubCategory.objects.get(pk=subcategory_id)

            # Update the subcategory details
                subcategory_obj.subcategory_name = form.get('subcategory_name',subcategory_obj.subcategory_name)
                subcategory_obj.description = form.get('description',subcategory_obj.description)
                subcategory_obj.availability = form.get('availability',subcategory_obj.availability)
                subcategory_obj.save()

                return 'Success'
        
        except SubCategory.DoesNotExist:
            return 'Subcategory id does not exist'
    def delete(self, request, *args, **kwargs):
        data = self.delete_subcategory(json.loads(request.body))
        return JsonResponse({'message':data}, safe=False)

    @staticmethod
    def delete_subcategory(form):
        subcategory_id = form.get('subcategory_id')
        
        if not subcategory_id:
            return "Please enter the valid name"
        
        try:
            
            sub_cat = SubCategory.objects.get(pk=subcategory_id)
            
            sub_cat.deleted = True
            sub_cat.save()
            return 'Success'
        except SubCategory.DoesNotExist:
            return 'Please enter valid category id'
            

class InventoryView(View):
    def get(self, request, *args, **kwargs):
        data = Inventory.objects.filter(deleted = False)
        serializer = Inventory_dataserializer(data, many = True)
        return JsonResponse(serializer.data, safe=False)    
    
    
@method_decorator(csrf_exempt, name='dispatch')

class AddCartView(View):
    def get(self, request, *args, **kwargs):
        data =   Addcart.objects.filter(deleted = False)
        serializer = Addcart_dataserializer(data, many = True)
        
        return JsonResponse(serializer.data, safe = False)
    
    def post(self, request, *args, **kwargs):
        data = self.create_cart(json.loads(request.body))
        return JsonResponse({'message':data}, safe = False)
    
    @staticmethod
    def create_cart(form):
        result = ''
        colour = form.get('colour')
        size = form.get('size')
        quantity = form.get('quantity')
        
      
        if not colour or not size or not quantity:
            return 'send the correct name'
        
        try:
            cart_obj = Addcart(colour = colour, quantity = quantity, size = size)
            cart_obj.save()
            return 'cart created successfully'
        except Exception as e:
            print(e.args)
            return 'please check data'
        
    def put(self, request, *args, **kwargs):
        data = self.update_cart(json.loads(request.body))
        return JsonResponse({'message':data}, safe=False)
    
    @staticmethod
    def update_cart(form):
        result = ''
        addcart_id = form.get('addcart_id')
        colour = form.get('colour')
        size = form.get('size')
        quantity = form.get('quantity')
        
        try:
            if not colour or not size or not quantity:
                return 'send the correct name'
            
            else:
                cart_obj = Addcart.objects.get(pk=addcart_id)
                
                cart_obj.colour = form.get('colour',cart_obj.colour)
                cart_obj.size = form.get('size',cart_obj.size)
                cart_obj.quantity = form.get('quantity',cart_obj.quantity)
                cart_obj.save()
                
                return 'Success'
        except Addcart.DoesNotExist:
            return 'id does not exist'
        
        
    def delete(self, request, *args, **kwargs):
        data = self.delete_cart(json.loads(request.body))
        return JsonResponse({'message':data}, safe = False)
    
    @staticmethod
    def delete_cart(form):
        addcart_id =  form.get('addcart_id')
        
        if not addcart_id:
            return 'check name'
        try:
            cart_obj = Addcart.objects.get(pk=addcart_id)
            
            cart_obj.deleted = True
            cart_obj.save()
            
            return 'deleted Success'
        
        except Addcart.DoesNotExist:
            return 'Please send valid id'

#Dress 
#ONE TO ONE RELATION 
@method_decorator(csrf_exempt, name='dispatch')
class DressDetailView(View):
    def get(self, request, *args, **kwargs):
        #try:
            dresses = Dress.objects.all()
           # ser = Dress_seralizer(dresses, many = True)
            dress_data = []

            for dress in dresses:
                dress_info = {
                    "dress_id":dress.id,
                    "cloth_name": dress.cloth_name,
                    "quantity_sold": dress.quantity_sold,
                    "rates": {
                        "likes": dress.rates.likes,
                        "dislikes": dress.rates.dislikes
                    }
                }
                dress_data.append(dress_info)

            return JsonResponse(dress_data, safe=False)
        
    def post(self, request):
        try:
            data = json.loads(request.body)
            cloth_name = data.get('cloth_name')
            quantity_sold = data.get('quantity_sold')
            likes = data.get('likes')
            dislikes = data.get('dislikes')

            if cloth_name is None or quantity_sold is None or likes is None or dislikes is None:
                return JsonResponse({"error": "Incomplete data provided"}, status=400)

            ratings = Ratings.objects.create(likes=likes, dislikes=dislikes)
            dress = Dress.objects.create(cloth_name=cloth_name, quantity_sold=quantity_sold, rates=ratings)

           
            return JsonResponse("Dress created successfully", safe=False)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    def put(self, request, *args, **kwargs): 
        try:      
            data = json.loads(request.body)
            # update using dress_id in primarykey(pk) 
           # dress_id = data.get('dress_id')
           # update using cloth_name also possible
            cloth_name = data.get('cloth_name')

            dress = Dress.objects.get(cloth_name=cloth_name)
            
            dress.cloth_name = data.get('cloth_name', dress.cloth_name)
            dress.quantity_sold = data.get('quantity_sold',dress.quantity_sold)
            dress.save()
            
            return JsonResponse("Sucess", safe=False)
        except Dress.DoesNotExist:
            return JsonResponse({"error": "Dress not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    def delete(self, request, *args, **kwargs): 
        try:
            data = json.loads(request.body)
            cloth_name = data.get('cloth_name')
           
            data_ser = Dress.objects.get(cloth_name=cloth_name)
            data_ser.delete()
            return JsonResponse({"message":'Deleted'}, safe=False)
        except Dress.DoesNotExist:
            return JsonResponse('Dress Does not exist', safe=False)
        except Exception as e:
            print(e.args)
            return JsonResponse ({"message":'Not deleted'},safe=False)
        
        
@method_decorator(csrf_exempt, name='dispatch')
class SpecView(View):
    #GET METHOD USING SPECIFIC NAME
    def get(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            model_name = data.get('model_name')
            if model_name == "":
                return JsonResponse({"error": "Please provide a model_name in the request body."}, status=400)

           
            if  model_name == "all":
                d = Spec.objects.all()
                seri = BikeSpec_Serializer(d, many = True)
                return JsonResponse(seri.data, safe=False) 
            else:
                datas = Spec.objects.filter(model_name=model_name)
                if not datas.exists():  # Check if no data matches the model_name
                    return JsonResponse({"error": f"No data found for model_name '{model_name}'"}, status=404)

                seri = BikeSpec_Serializer(datas, many = True)
                return JsonResponse(seri.data, safe=False) 
            
        except Spec.DoesNotExist:
            return JsonResponse("Spec Doesnot Exist", safe=False)
        
        except Exception as e:
            return JsonResponse({"error": "An error occurred while processing your request"}, status=500)
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            model_name = data.get('model_name')
            color = data.get('color')
            top_speed = data.get('top_speed')
            fuel = data.get('fuel')
            engine_cc = data.get('engine_cc')
            
            if model_name is None or color is None or top_speed is None or fuel is None or engine_cc is None:
                return JsonResponse({"message":"PLease enter valid data"}, safe=True)
            
            obj = Spec.objects.create(model_name=model_name,color=color,top_speed=top_speed,fuel=fuel,engine_cc=engine_cc)
            obj.save()
            return JsonResponse("Sucess", safe=False)
        except Exception as e:
            return JsonResponse({"error":str(e)},safe=False)

@method_decorator(csrf_exempt, name='dispatch')      
class BikeView(View):
    def get(self, request, *args, **kwargs):
        datas = Bike.objects.all()
        serializer = Bike_serializer(datas, many = True)
        return JsonResponse(serializer.data, safe=False)
    
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            company_name = data.get('company_name')
            launched_year = data.get('launched_year')
            details = data.get('details')
           
            if company_name !="":
                com_obj = Bike(company_name=company_name,launched_year=launched_year,details=details)
                com_obj.save()
                return JsonResponse("created Sucessfully", safe=False)
            else:
                return JsonResponse('company_name cannot be empty', safe=False)
        except Exception as e:
            print("Error saving data", e)
            return JsonResponse({"error":"error"}, safe=False)
from rest_framework.decorators import api_view   
@method_decorator(csrf_exempt, name='dispatch')      
@api_view(['GET', 'POST','PUT','DELETE'])
def student_api(request):
    if request.method =="GET":
        data = Students.objects.all()
        ser = Student_serializer(data, many = True)
        return JsonResponse(ser.data, safe=False)
    
    if request.method == 'POST':
        serializer = Student_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):  # Add raise_exception=True to trigger validation errors as exceptions
            name = serializer.validated_data.get('name')
            if not name:
                return JsonResponse({"name": "This field is required."}, safe=False)
            
            serializer.save()
            return JsonResponse({'message': 'Successfully created'}, safe=False)
        return JsonResponse(serializer.errors, safe=False)
    if request.method == 'PUT':
    
        student_id = request.data.get('student_id')  # Extract the student ID from the request data
        if not student_id:
            return JsonResponse({'message': 'Please provide a valid student ID'}, safe=False)
       
        try:
             student_instance = Students.objects.get(id=student_id)
        except Students.DoesNotExist:
            return JsonResponse({"message": "Student not found."}, safe=False) 

        serializer = Student_serializer(student_instance, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse({'message': 'Successfully updated'}, safe=False)
        return JsonResponse(serializer.errors, safe=False)
    
    if request.method == 'DELETE':
        student_id = request.data.get('student_id')
        if not student_id:
            return JsonResponse("Please enter valid student id")
        
        try:
            std = Students.objects.get(pk=student_id)
            std.delete()
            return JsonResponse("Deleted Sucessfully", )
        except Students.DoesNotExist:
            return JsonResponse("Id Does not exist", safe=False)
        
     
# Generic based views 
class GetAllUsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer    
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]  
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)


# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Users
from .serializer import User_Serializer

@api_view(['GET', 'POST','PUT'])
def user_list(request):
    if request.method == 'GET':
        users = Users.objects.all().order_by('id')
        serializer = User_Serializer(users, many=True)
        return JsonResponse(serializer.data, safe = False)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'POST':
        data = json.loads(request.body)

       # id = data.get('id')
        username = data.get('username')
        email = data.get('email')

        if not username or not email:
            return JsonResponse({'message': 'Please provide valid data'}, status=400)

        try:
            cart_obj = Users(username=username, email=email)
            cart_obj.save()
            return JsonResponse({'message': 'Cart created successfully'}, status=201)
        except Exception as e:
            print(e.args)
            return JsonResponse({'message': 'Error creating cart'}, status=500)
    if request.method == 'PUT':
        data = json.loads(request.body)
        user_id = data.get('id')
        username = data.get('username')
        email = data.get('email')

        if not user_id:
            return Response({'message': 'Please provide user ID'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user_obj = Users.objects.get(pk=user_id)
            user_obj.username = username
            user_obj.email = email
            user_obj.save()
            return Response({'message': 'User updated successfully'}, status=status.HTTP_200_OK)
        except Users.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e.args)
            return Response({'message': 'Error updating user'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        # serializer = User_Serializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    try:
        user = Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = User_Serializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = User_Serializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

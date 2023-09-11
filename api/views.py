from django.shortcuts import render
import io
from .serializers import StudentSerializer
from .models import *
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def studentApi(request):
  if request.method == 'GET':
    json_data = request.body
    stream = io.BytesIO(json_data)
    print(stream)
    pythondata = JSONParser().parse(stream)
    print(pythondata)
    id = pythondata.get('id', None)
    print(id)
    if id is not None :
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='appliction/json')
    
    stu = Student.objects.all()
    serializer = StudentSerializer(stu,many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='appliction/json')
  
  if request.method == 'POST':
    json_data = request.body
    stream = io.BytesIO(json_data)
    pythondata = JSONParser().parse(stream)
    serializer = StudentSerializer(data = pythondata)
    if serializer.is_valid():
        Student.objects.create(
          name = serializer.validated_data.get('name'),
          roll = serializer.validated_data.get('roll'),
          city = serializer.validated_data.get('city')
        )
        res = { 'msg': 'Data is Created'}
        json_data = JSONRenderer().render(res)
    else :
        json_data = JSONRenderer().render(serializer.errors)
    return HttpResponse(json_data , content_type='application/json')
  
  if request.method == 'PUT':
    json_data = request.body
    print(json_data)
    stream = io.BytesIO(json_data)
    pythondata = JSONParser().parse(stream)
    id = pythondata.get('id')
    print(id)
    stu = Student.objects.get(id=id)
    print(stu)
    serializer = StudentSerializer(stu, data=pythondata)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
        res = {'msg': 'data is Updated'}
        json_data = JSONRenderer().render(res)
        print(json_data)
        print(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
    print(serializer.errors)
    json_data = JSONRenderer().render(serializer.errors)
    return HttpResponse(json_data , content_type='application/json') 
  
  if request.method == 'DELETE':
    json_data = request.body
    stream = io.BytesIO(json_data)
    pythondata = JSONParser().parse(stream)
    id = pythondata.get('id')
    stu = Student.objects.get(id=id)
    stu.delete()
    res = {'msg': 'Data Deleted '}
    json_data = JSONRenderer().render(res)
    return HttpResponse(json_data, content_type='application/json')
   
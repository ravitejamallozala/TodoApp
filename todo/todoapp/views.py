# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from django.template import loader
from .models import *

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics


from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from todoapp.serializer import *


# Create your views here.

def index(request):
    return HttpResponse("<h1>Yoo its Working Fine</h1>")


def getlist(request):
    temp=loader.get_template("todoapp/listdata.html")
    datalists=Todolist.objects.all()
    context={
        'todolists':datalists ,
    }

    return HttpResponse(temp.render(context,request))


def getdata(request,list_id):
    temp=loader.get_template("todoapp/alldata.html")
    itemlists=Todoitem.objects.filter(todolist__id = list_id)

    n=Todolist.objects.filter(id = list_id)


    context={
        'todoitems':itemlists ,
        'listname':n[0].name,
    }

    return HttpResponse(temp.render(context,request))


def getHome(request) :
    rtemp = loader.get_template("registration/todo_home.html")
    context = {}
    return HttpResponse(rtemp.render(context, request))
# @csrf_exempt

# Class based views RestApi uses ./serilizer to convert to Json format the response


# class GetLists(LoginRequiredMixin,APIView): #NOrmal class based views returns onlu JSONResponse as needed
#     """
#     List all Todilists , or create a new Todolist.
#     """
#
#     def perform_create(self, serializer):
#         serializer.save(user = self.request.user)
#
#     def get(self, request, format=None):
#         lists = Todolist.objects.all()
#         serializer = TodolistSerializer(lists, many=True)
#         return JsonResponse(serializer.data,safe=False)
#
#     def post(self, request, format=None):
#         serializer = TodolistSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=status.HTTP_201_CREATED,safe=False)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST,safe=False)

# class AlterList(LoginRequiredMixin, APIView):
#
#     def get_object(self, pk):
#         try:
#             return Todolist.objects.get(pk=pk)
#         except Todolist.DoesNotExist:
#             raise Http404
#
#     def put(self, request, pk, format=None):
#         newitem = self.get_object(pk)
#         serializer = TodolistSerializer(newitem, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, safe=False)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)
#
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return JsonResponse(status=status.HTTP_204_NO_CONTENT, safe=False)


class GetLists(LoginRequiredMixin, generics.ListCreateAPIView): # Generic Class based Views  Auto get and post  methods implemented
    def perform_create(self, serializer):
       serializer.save(user = self.request.user)

    def get_queryset(self):
        self.queryset = Todolist.objects.filter(user = self.request.user)
        return super(GetLists, self).get_queryset()

    serializer_class = TodolistSerializer

class AlterList(LoginRequiredMixin,generics.RetrieveUpdateDestroyAPIView):

    def perform_create(self, serializer):
       serializer.save(user = self.request.user)

    def get_queryset(self):
        self.queryset = Todolist.objects.filter(user = self.request.user)
        return super(AlterList, self).get_queryset()

    serializer_class = TodolistSerializer

# @csrf_exempt
# def Getitems(LoginRequiredMixin , request, pk):
#
#     if request.method == 'GET':
#         items = Todoitem.objects.all().filter(todolist_id=pk)
#         serializer = TodoitemSerializer(items, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         print data
#
#         serializer = TodoitemSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

class Itemgetpost(LoginRequiredMixin,generics.ListCreateAPIView): #generic class based views sending info along with JSON
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    def get_queryset(self):
        temp=Todolist.objects.filter(id=self.kwargs['pk'])
        print self.kwargs['pk']
        self.queryset = Todoitem.objects.filter(todolist=temp)
        return super(Itemgetpost, self).get_queryset()

    serializer_class = TodoitemSerializer



# class Getitems(LoginRequiredMixin,APIView): #NOrmal class based views returns onlu JSONResponse as needed
#     """
#     List all Toditems in a list , or create a new TodoItem
#     """
#
#     def perform_create(self, serializer):
#         serializer.save(user = self.request.user)
#
#     def get(self, request, format=None):
#         lists = Todolist.objects.all()
#         serializer = TodolistSerializer(lists, many=True)
#         return JsonResponse(serializer.data,safe=False)
#
#     def post(self, request, format=None):
#         serializer = TodolistSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=status.HTTP_201_CREATED,safe=False)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST,safe=False)


class Alteritem(LoginRequiredMixin,APIView):


    def get_object(self, pk):
        try:
            return Todoitem.objects.get(pk=pk)
        except Todoitem.DoesNotExist:
            raise Http404
    def put(self, request, pk, format=None):
        newitem = self.get_object(pk)
        serializer = TodoitemSerializer(newitem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST,safe=False)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT,safe=False)
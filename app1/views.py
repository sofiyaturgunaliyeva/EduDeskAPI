from django.shortcuts import render
from rest_framework.decorators import action

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status, filters

from rest_framework.viewsets import ModelViewSet




# Vazifa:
#
# 1. Hamma tolovlarni get qiluvchi, yangi tolov post qiluvchi viewlar yozing.
#
# 2. Hamma oquvchilarni get qilish, yangi oquvchi qo'shish uchun APIView yozing.
#
# 3. Hamma davomatlarni get qiluvchi, yangi davomat qo'shuvchi viewlar yozing.
#
# 4. Loyiha uchun swagger-dokumentatsiya yozing.
#
# Hamma jadvallarga ma'lumot qo'shib kelishga harakat qiling.

class TolovlarAPIView(APIView):
    def get(self,request):
        tolovlar = Tolov.objects.all()
        serializer = TolovSerializer(tolovlar, many=True)
        return Response(serializer.data)

    def post(self, request):
        malumot = request.data
        serializer = TolovSerializer(data=malumot)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OquvchilarAPIView(APIView):
    def get(self,request):
        oquvchilar = Oquvchi.objects.all()
        serializer = OquvchiSerializer(oquvchilar, many=True)
        return Response(serializer.data)

    def post(self, request):
        malumot = request.data
        serializer = OquvchiSerializer(data=malumot)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DavomatlarAPIView(APIView):
    def get(self,request):
        davomatlar = Davomat.objects.all()
        serializer = DavomatSerializer(davomatlar, many=True)
        return Response(serializer.data)

    def post(self, request):
        malumot = request.data
        serializer = DavomatSerializer(data=malumot)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





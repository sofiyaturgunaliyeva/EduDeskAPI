from rest_framework import serializers

from .models import *


class KursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kurs
        fields = '__all__'


class XonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xona
        fields = '__all__'


class OquvchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oquvchi
        fields = '__all__'


class UstozSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ustoz
        fields = '__all__'


class GuruhSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guruh
        fields = '__all__'


class DavomatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Davomat
        fields = '__all__'


class TolovSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tolov
        fields = '__all__'


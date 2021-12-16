from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Reciepts, User


class allReceiptSerializer(serializers.ModelSerializer):
     
     class Meta:
          model = Reciepts
          fields = [
               "file_id",
               "receipt",
               "get_receipt_url",
               "date_created"
          ]
          
class userSerializer(serializers.ModelSerializer):
     
     class Meta:
          model = User
          fields = "__all__"
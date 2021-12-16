from django.db.models import fields
from rest_framework import serializers
from .models import Reciepts


class allReceiptSerializer(serializers.ModelSerializer):
     
     class Meta:
          model = Reciepts
          fields = [
               "file_id",
               "receipt",
               "get_receipt_url",
               "date_created"
          ]
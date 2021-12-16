from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .generate_receipt_func import Generate
from .serializers import allReceiptSerializer
from .models import Reciepts

report = Generate()



@permission_classes([IsAuthenticated])
class GenerateReceipt(APIView):
     def post(self, request):
          data = request.data
          customer_name = data.get('customerName', '')
          customer_address = data.get('customerAddress', '')
          customer_mobile_no = data.get('customerMobile', '')
          description = data.get('productDesc', '')
          unit = data.get('productUnit', '')
          price_per_unit = data.get('pricePerUnit', '')
          response = report.generate_receipt(request, customer_name, customer_address, customer_mobile_no, description, unit, price_per_unit)
          return response
     
     def get(self, request):
          return report.all_receipt(request)
     


# Filter Reciept View   
@permission_classes([IsAuthenticated])
class FilterReceipt(APIView):
     def get(self, request, receiptId):
          return report.filter_receipt(receiptId)

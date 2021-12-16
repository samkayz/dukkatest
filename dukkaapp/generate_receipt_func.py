# imports module
from rest_framework.pagination import PageNumberPagination
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
import random
import string
from rest_framework.response import Response
from rest_framework import status
from .models import Reciepts
from datetime import datetime
from .serializers import allReceiptSerializer
base_date_time = datetime.now()
now = (datetime.strftime(base_date_time, "%Y-%m-%d"))


class Generate:
     serializer_class = allReceiptSerializer
     # Pagination Function
     def serializeData(self, instance, serializeModel, request):
          paginator = PageNumberPagination()
          paginator.page_size = 5
          result_page = paginator.paginate_queryset(instance, request)
          serialize = serializeModel(instance=result_page, many=True)
          data = {
               "status": status.HTTP_200_OK,
               "data": serialize.data
               
          }
          return paginator.get_paginated_response(data)
     
     # data which we are going to display as tables
     def generate_receipt(self, request, customer_name, customer_address, customer_mobile_no, description, unit, price_per_unit):
          # Generate randon string to be use for naming each receipt generated
          res = ''.join(random.choices(string.digits, k=6))
          filename = str(res)
          
          # Calculate Total Price
          total = (float(unit) * float(price_per_unit))
          
          # Data to be displayed on the PDF
          NAME = [
               "NAME: {}\nADDRESS: {}\nMOBILE NO: {}".format(customer_name, customer_address, customer_mobile_no),
          ]
          DATA = [
	          [ "SN", "Date" , "Description", "Unit", "Price per Unit (NGN)", "Total (NGN)" ],
	          [ "1", "{}".format(now), "{}".format(description), "{}".format(unit), "{}".format(price_per_unit), "{}".format(total)],
               [ "", "", "", "", "", ""],
               [ "", "", "", "", "", ""],
               [ "", "", "", "", "", ""],
	          [ "", "", "", "", "Total Amount Payable", "{}".format(total)],
               NAME
          ]
          

          # creating a Base Document Template of page size A4
          pdf = SimpleDocTemplate( "media/{}.pdf".format(filename) , pagesize = A4 )

          # standard stylesheet defined within reportlab itself
          styles = getSampleStyleSheet()

          # fetching the style of Top level heading (Heading1)
          title_style = styles[ "Heading1" ]

          # 0: left, 1: center, 2: right
          title_style.alignment = 1

          # creating the paragraph with
          # the heading text and passing the styles of it
          title = Paragraph( "Dukka Product Receipt" , title_style )

          # creates a Table Style object and in it,
          # defines the styles row wise
          # the tuples which look like coordinates
          # are nothing but rows and columns
          style = TableStyle(
	          [
		          ( "BOX" , ( 0, 1 ), ( 1, -2 ), 1 , colors.black ),
		          ( "GRID" , ( 0, 0 ), ( 5 , 5 ), 1 , colors.black ),
		          ( "BACKGROUND" , ( 0, 0 ), ( 5, 0 ), colors.gray ),
		          ( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.whitesmoke ),
		          ( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ),
		          ( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -2 ), colors.beige ),
	          ]
          )

          # creates a table object and passes the style to it
          table = Table( DATA , style = style )

          # final step which builds the
          # actual pdf putting together all the elements
          pdf.build([ title , table ])
          
          # Save it into the DB for referencing
          save_pdf = Reciepts(creator=request.user.id, file_id=filename, receipt="{}.pdf".format(filename))
          save_pdf.save()
          response = {
               "code": status.HTTP_200_OK,
               "status": "success",
               "receiptId": filename,
               "receiptUrl": save_pdf.get_receipt_url()
          }
          return Response(data=response, status=status.HTTP_200_OK)
     
     
     # Function to Serialize all the Receipt and display them with Paginations
     def all_receipt(self, request):
          instance = Reciepts.objects.filter()
          return self.serializeData(instance, allReceiptSerializer, request)
     
     #filter the Receipt
     def filter_receipt(self, receipt_id):
          instance = Reciepts.objects.filter(file_id=receipt_id)
          serialize = allReceiptSerializer(instance=instance, many=True)
          
          data = {
               "code": status.HTTP_200_OK,
               "status": "success",
               "response": serialize.data
          }
          return Response(data, status=status.HTTP_200_OK)
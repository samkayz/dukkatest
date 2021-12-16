from rest_framework.response import Response
from rest_framework import status
from .models import User
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes



@permission_classes([])
class UsersManager(APIView):
     def post(self, request):
          data = request.data
          fullname = data.get('fullname','')
          email = data.get('email','')
          password = data.get('password','')
          if User.objects.filter(email=email).exists():
               response = {
                    "code": status.HTTP_400_BAD_REQUEST,
                    "status": "fail",
                    "message": "Email already exist"
               }
               return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
          else:
               print("Here")
               user = User.objects.create_user(email=email, fullname=fullname, password=password)
               user.save()
               resp = {
                   "code": status.HTTP_200_OK,
                   "status": "success",
                   "name": user.fullname,
                   "email": user.email 
               }
               return Response(data=resp, status=status.HTTP_200_OK)
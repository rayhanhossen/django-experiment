from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from helper.response_helper import SuccessResponse, ErrorResponse
from user.serializers import NewUserSerializer, NewSuperUserSerializer


class NewUserCreateView(APIView):
    def post(self, request):
        try:
            serializer = NewUserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                response = SuccessResponse(message="User data saved Successfully!", data=serializer.data)
                return Response(response.to_json(), status=status.HTTP_201_CREATED)
            response = ErrorResponse(message="User data saved Successfully!", errors=serializer.errors)
            return Response(response.to_json(), status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            response = ErrorResponse(str(e))
            return Response(response.to_json(), status=status.HTTP_400_BAD_REQUEST)


class NewSuperUserCreateView(APIView):
    def post(self, request):
        try:
            serializer = NewSuperUserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                response = SuccessResponse(message="Super user data saved Successfully!", data=serializer.data)
                return Response(response.to_json(), status=status.HTTP_201_CREATED)
            response = ErrorResponse(message="Super user data saved Successfully!", errors=serializer.errors)
            return Response(response.to_json(), status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            response = ErrorResponse(str(e))
            return Response(response.to_json(), status=status.HTTP_400_BAD_REQUEST)

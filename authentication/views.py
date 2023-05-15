from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from authentication.serializers import UserLoginSerializer
from helper.response_helper import SuccessResponse, ErrorResponse


# Create your views here.
class UserLoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=email)
            if user.check_password(password) and user.is_active:
                serializer = UserLoginSerializer(user)
                # get refresh token
                refresh = RefreshToken.for_user(user)
                token = str(refresh.access_token)

                data = {
                    'token': token,
                    'user': serializer.data,
                }
                response = SuccessResponse(message="Log In Successful!", data=data)
                return Response(response.to_json(), status=status.HTTP_200_OK)
        except UserModel.DoesNotExist:
            response = ErrorResponse(message="Log In Failed!")
            return Response(response.to_json(), status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            response = ErrorResponse(str(e))
            return Response(response.to_json(), status=status.HTTP_400_BAD_REQUEST)

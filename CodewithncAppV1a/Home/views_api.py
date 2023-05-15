from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import Profile
from .others import *
from .views import *


def LogoutView(request):
    logout(request)
    return redirect('/access/')


class RegisterView(APIView):

    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'Failed to Register or Signup'

        try:
            data = request.data

            if data.get('username') is None:
                response['message'] = 'Username Missing ! Not entered'
                raise Exception('Username Missing')
            if data.get('password') is None:
                response['message'] = 'Password Missing ! Not entered'
                raise Exception('Password Missing')

            username_inp = User.objects.filter(username=data.get('username')).first()

            if username_inp:
                response['message'] = 'Username Already Exists.'
                raise Exception('User Already Exists')

            user_obj = User.objects.create(email=data.get('username'), username=data.get('username'))
            user_obj.set_password(data.get('password'))
            user_obj.save()
            response['status'] = 200
            response['message'] = 'User created Successfully.'

            token = generate_random_string(15)
            Profile.objects.create(user=user_obj, token=token)
            # send_varify_mail_to_user(data.get('username'), token)

            return Response(response)

        except Exception as e:
            print(e)

        return Response(response)


class LoginView(APIView):

    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'Failed to Login.'

        try:
            data = request.data

            if data.get('username') is None:
                response['message'] = 'No User Found ! Not entered'
                raise Exception('No Username found')
            if data.get('password') is None:
                response['message'] = 'Password Not Found'
                raise Exception('Password Missing')

            username_inp = User.objects.filter(username=data.get('username')).first()

            if username_inp is None:
                response['message'] = 'Invalid Username !'
                raise Exception('User not Found')

            if not Profile.objects.filter(user = username_inp).first().is_varified:
                response['message'] = 'Account not Verified !'
                raise Exception('Email or Profile not Verified.')


            # matching
            user_obj = authenticate(username=data.get('username'), password=data.get('password'))

            if user_obj:
                response['status'] = 200
                response['message'] = 'login successfull'
                login(request, user_obj)
            else:
                response['message'] = 'Login Unsuccessfull !'
                raise Exception('Authentication Failed')

            return Response(response)

        except Exception as e:
            print(e)

        return Response(response)


LoginView = LoginView.as_view()
RegisterView = RegisterView.as_view()

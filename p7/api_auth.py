import requests
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib.auth.hashers import check_password, make_password

from job.models import Company
from job.serializers import CompanySerializer
from p7.models import is_professional, is_company
from pro.models import Professional
from pro.serializers import ProfessionalSerializer, INACTIVE_USER

from p7.settings_dev import SIMPLE_JWT
from p7.settings_dev import DEVICE_ACCESS_TOKEN_LIFETIME
from p7.settings_dev import DEVICE_REFRESH_TOKEN_LIFETIME
from p7.settings_dev import WEB_ACCESS_TOKEN_LIFETIME
from p7.settings_dev import WEB_REFRESH_TOKEN_LIFETIME
from resources.strings_pro import INCORRECT_PASSWORD, NO_SUCH_USER, INACTIVE_COMPANY, INCORRECT_PASSWORD_COMPANY, \
    NO_SUCH_COMPANY


@api_view(["POST"])
@permission_classes(())
def professional_signin(request):
    email = request.data['email']
    password = request.data['password']

    try:
        user = User.objects.get(email=email)
        if not user.is_active :
            raise AuthenticationFailed(INACTIVE_USER)
        elif not check_password(password, user.password) :
            raise AuthenticationFailed(INCORRECT_PASSWORD)
        elif not is_professional(user):
            raise AuthenticationFailed()
    except User.DoesNotExist:
        raise AuthenticationFailed(NO_SUCH_USER)

    if 'device_id' in request.data and request.data['device_id']:
        RefreshToken.lifetime = DEVICE_REFRESH_TOKEN_LIFETIME
        AccessToken.lifetime = DEVICE_ACCESS_TOKEN_LIFETIME
    else:
        RefreshToken.lifetime = WEB_REFRESH_TOKEN_LIFETIME
        AccessToken.lifetime = WEB_ACCESS_TOKEN_LIFETIME

    token=RefreshToken.for_user(user)
    data= {}
    data['username'] = user.username
    data['access'] = str(token.access_token)
    data['refresh'] = str(token)

    pro = Professional.objects.get(user_id = user.id)
    data['user'] = {
        'id': user.id,
        'email': email,
        'type': 'professional'
    }
    data['pro'] = ProfessionalSerializer(pro, many=False).data
    data['token_lifetime'] = SIMPLE_JWT
    return Response(data)


@api_view(["POST"])
@permission_classes(())
def company_signin(request):
    email = request.data['email']
    password = request.data['password']

    try:
        user = User.objects.get(email=email)
        if not user.is_active :
            raise AuthenticationFailed(INACTIVE_COMPANY)
        elif not check_password(password, user.password) :
            raise AuthenticationFailed(INCORRECT_PASSWORD_COMPANY)
        elif not is_company(user):
            raise AuthenticationFailed()
    except User.DoesNotExist:
        raise AuthenticationFailed(NO_SUCH_COMPANY)

    if 'device_id' in request.data and request.data['device_id']:
        RefreshToken.lifetime = DEVICE_REFRESH_TOKEN_LIFETIME
        AccessToken.lifetime = DEVICE_ACCESS_TOKEN_LIFETIME
    else:
        RefreshToken.lifetime = WEB_REFRESH_TOKEN_LIFETIME
        AccessToken.lifetime = WEB_ACCESS_TOKEN_LIFETIME

    token = RefreshToken.for_user(user)
    data = {}
    data['username'] = user.username
    data['access'] = str(token.access_token)
    data['refresh'] = str(token)

    company = Company.objects.get(user_id=user.id)
    data['user'] = {
        'id': user.id,
        'email': email,
        'type': 'company'
    }
    data['company'] = CompanySerializer(company, many=False).data
    data['token_lifetime'] = SIMPLE_JWT
    return Response(data)


@api_view(["GET"])
@permission_classes(())
def verify_user(request):
    if request.user.is_anonymous:
        raise AuthenticationFailed()
    data = {
        'id': request.user.id,
        'email': request.user.email,
        'type': 'professional' if is_professional(request.user) else 'company'
    }
    response = Response(data)
    return response


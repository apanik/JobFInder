from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from p7.api import *
from testimonial.urls import *
from .api_auth import professional_signin, company_signin, verify_user
urlpatterns = [
    url(r'^staff/', admin.site.urls),
    path('api/', include('job.urls_api')),
    path('api/', include('messaging.urls_api')),
    path('api/', include('pro.urls_api')),
    path('api/', include('testimonial.urls')),
    path('api/', include('settings.urls')),
    path('api/', include('career_advice.urls_api')),

    path('api/send_email_to_admin_contact_us/', send_email_to_admin_contact_us), # Public API
    path('log/', isLoggedIn), # Public API
    path('api/pro/signin/', professional_signin), # Public API
    path('api/company/signin/', company_signin), # Public API

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/user/verify/', verify_user),

    path('api/pro/google/signin/', GoogleSigninProApi.as_view(), name='google_token_verify'),
    path('api/company/google/signin/', GoogleSigninCompanyApi.as_view(), name='google_token_verify'),

]


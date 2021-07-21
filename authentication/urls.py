# -*- encoding: utf-8 -*-
from django.conf.urls import url

from .views import login_view, user_registration,google_login,admin_login_view
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    url('authlogin/', login_view, name="authlogin"),
    url('registeruser/', user_registration, name="registeruser"),
    url("logout/", LogoutView.as_view(), name="logout"),
    url("google", google_login, name="google_login"),

    url('reset_password/',
         auth_views.PasswordResetView.as_view(),
         name="reset_password"),

    url('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(),
         name="password_reset_done"),

    url('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),

    url('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(),
         name="password_reset_complete"),
    # url('^', include('django.contrib.auth.urls')),

    # password reset.
    # url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    # url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     auth_views.password_reset_confirm, name='password_reset_confirm'),
    # url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
]

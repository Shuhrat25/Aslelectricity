from django.urls import path
from .views import admin_list, login_page, ishchilar_page, magazin_page, zakazchi_page

urlpatterns = [
    path('asilbek/', admin_list, name="asilbek"),
    path('shop/', magazin_page, name="shop"),
    path('user/', zakazchi_page, name="user"),
    path('ishchilar/', ishchilar_page, name="ishchilar"),
]

from django.conf.urls import url,include
from app01 import views

urlpatterns = [
    url(r'^home/', views.home, {"userman":"wd11"}),
    url(r'^news/(\d+)/(\d+)', views.news),
    url(r'^db_handle/', views.db_handle),
]
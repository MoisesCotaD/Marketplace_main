from django.urls import path

from .views import contact, detail

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('detail/<int:pj>/', detail, name= 'detail'),
]

from django.urls import path
from .import views

urlpatterns=[
    path('facebook',views.fb),
    path('validation',views.domvalidation),
    path('val',views.val),
    path('calculater',views.calculater),
    path('array',views.array),
    path('firstpush',views.firstpush),

]
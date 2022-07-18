
from django.urls import path
from .import views as v

urlpatterns = [
    path('', v.home),
    path('addemp1', v.add_emp1),
    path('addemp2', v.add_emp2),
    path('addacc', v.add_account),
]

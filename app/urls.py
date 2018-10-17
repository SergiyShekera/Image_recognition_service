from django.urls import path
from .views import Upload_File

app_name='app'

urlpatterns = [
    path('img-inf', Upload_File),

]
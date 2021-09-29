from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home")
]
#上記のurlpatternsは、{}ではなく[]で囲まないとエラーになる。
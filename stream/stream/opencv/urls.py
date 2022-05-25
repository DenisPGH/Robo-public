from django.urls import path

from stream.opencv.views import IndexView, openCam

urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    path('stream/',openCam,name='cam'),
]
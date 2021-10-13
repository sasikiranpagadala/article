from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home-page'),
    path('input/<int:pk>', views.input,name='input'),
    path('getuser/<int:pk>/<int:uid>',views.getuser,name='getuser'),
    path('up/<int:pk>',views.up,name='upcontent'),
    # path('delete/', views.delete,name='delete'),
    path('update/<int:pk>', views.update,name='update'),
    path('addcontent/<int:pk>', views.addcontent,name='addcontent'),
]
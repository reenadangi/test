from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="shows"),
    path('new/', views.new,name="new"),
    path('add_show/', views.add_show,name="add_show"),    
    path('showDetails/<show_id>/', views.showDetails,name="showDetails"),
    path('delete_show/<show_id>/', views.delete_show,name="delete_show"),
    path('editShow/<show_id>/', views.editShow,name="editShow"),
    path('update_show/', views.update_show,name="update_show"),
    
 
]
from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('shoes/', views.shoes_index, name='index'),
  path('shoes/<int:shoe_id>/', views.shoes_detail, name='detail'),
  path('shoes/create/', views.ShoeCreate.as_view(), name='shoes_create'),
  path('shoes/<int:pk>/update/', views.ShoeUpdate.as_view(), name='shoes_update'),
  path('shoes/<int:pk>/delete/', views.ShoeDelete.as_view(), name='shoes_delete'),
  path('shoes/<int:shoe_id>/add_wore/', views.add_wore, name='add_wore'),
  path('shoes/<int:shoe_id>/assoc_occasion/<int:occasion_id>/', views.assoc_occasion, name='assoc_occasion'),
  path('shoes/<int:shoe_id>/unassoc_occasion/<int:occasion_id>/', views.unassoc_occasion, name='unassoc_occasion'),
  # path('shoes/<int:shoe_id>/add_photo/', views.add_photo, name='add_photo'),
  path('occasions/', views.OccasionList.as_view(), name='occasions_index'),
  path('occasions/<int:pk>/', views.OccasionDetail.as_view(), name='occasions_detail'),
  path('occasions/create/', views.OccasionCreate.as_view(), name='occasions_create'),
  path('occasions/<int:pk>/update/', views.OccasionUpdate.as_view(), name='occasions_update'),
  path('occasions/<int:pk>/delete/', views.OccasionDelete.as_view(), name='occasions_delete'),
]
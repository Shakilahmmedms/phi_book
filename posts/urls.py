from django.urls import path
from .import views


urlpatterns = [
    path('add/',views.add_post, name='add_post'),
    path('details/<int:id>', views.DetailPostViews.as_view(),name='delails_post_view'),
    path('edit/<int:id>', views.edit_post, name='edit_post'),
    path('delete/<int:id>', views.delete_post, name='delete_post'),
   
     path('like/<int:post_id>/', views.like_post, name='like_post'),

]


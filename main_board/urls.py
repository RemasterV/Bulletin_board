from django.urls import path
from .views import Posts, OnePost, PostCreate, PostEdit, PostDelete, MessageCreate


urlpatterns = [

   path('', Posts.as_view(), name='main'),
   path('<int:pk>/', OnePost.as_view(), name='post_link'),
   path('create/', PostCreate.as_view()),
   path('<int:pk>/edit/', PostEdit.as_view()),
   path('<int:pk>/delete/', PostDelete.as_view()),
   path('<int:pk>/message/', MessageCreate.as_view()),

]
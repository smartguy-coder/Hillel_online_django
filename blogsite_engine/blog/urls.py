
from django.urls import path


from .views import *

# app_name = 'blog'

urlpatterns = [
    path('', index_view, name='posts'),
    path('detail/<int:pk>', PostAndAllComments.as_view(), name='post_details'),
    path('new_comment/', new_comment, name='new_comment'),
    path('new_post/', new_post, name='new_post'),
    path('new_category/', new_category, name='new_category'),
    path('new_user/', new_user, name='new_user'),
    ]
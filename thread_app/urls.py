from django.urls import path
from . import views

urlpatterns = [
    path('', views.top, name='top'),
    path('thread/<int:thread_id>', views.thread_detail, name='thread_detail'),
    path('thread/delete/<int:thread_id>', views.thread_delete, name='thread_delete')
]

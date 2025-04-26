
from django.urls import path
from status.views import (StatusViewer,StatusListView,StatusCreateView,StatusDetailView,StatusUpdateView,StatusDeleteView)


urlpatterns = [
   
    path('statuses/',StatusListView.as_view(),name='status_view'),
    path('status/create/',StatusCreateView.as_view(),name='status_list_view'),
    
    path('status/<pk>/',StatusUpdateView.as_view(),name=''),
    path('status/update/<pk>/',StatusUpdateView.as_view(),name=''),
    path('status/delete/<pk>/',StatusDeleteView.as_view(),name=''),
   
    
]

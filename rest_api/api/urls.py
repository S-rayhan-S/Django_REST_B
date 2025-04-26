
from django.urls import path
# from status.views import (StatusViewer,StatusListView,StatusCreateView,StatusDetailView,StatusUpdateView,StatusDeleteView)

from status.views import StatusListCreateApiView,StatusDetailDeleteUpdateView


urlpatterns = [
   
    path('status/',StatusListCreateApiView.as_view(),name='status_view'),
    path('status/<pk>/',StatusDetailDeleteUpdateView.as_view(),name=''),
    
    
]

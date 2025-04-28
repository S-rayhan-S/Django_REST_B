
from django.urls import path
# from status.views import (StatusViewer,StatusListView,StatusCreateView,StatusDetailView,StatusUpdateView,StatusDeleteView)

#Commneted for using routers
# from status.views import StatusListCreateApiView,StatusDetailDeleteUpdateView


from rest_framework import routers
from status.views import StatusViewSet
#Routers
router = routers.SimpleRouter()
router.register(r'status', StatusViewSet)
urlpatterns = [
    
]
urlpatterns += router.urls



#commented as now using routers, so don't need these routes
# urlpatterns = [   
#     path('status/',StatusListCreateApiView.as_view(),name='status_view'),
#     path('status/<pk>/',StatusDetailDeleteUpdateView.as_view(),name=''),   
# ]

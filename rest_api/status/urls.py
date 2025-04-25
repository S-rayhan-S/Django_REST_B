
from django.urls import path
from status.views import StatusViewer
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('status/',include('status.urls')),
    path('all/',StatusViewer.as_view(),name='status_view'),
]

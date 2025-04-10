from django.urls import include, path

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('rooms/', include('rooms.urls')),
    # Add other app URLs here
]

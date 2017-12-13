from django.urls import path, include

urlpatterns = [
    path('blogsite/', include('blogsite.urls')),
]

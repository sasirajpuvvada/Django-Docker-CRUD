from django.urls import path
from .views import EmployeeApi, EmployeeCreateApi, EmployeeDeleteApi, EmployeeUpdateApi


urlpatterns = [
    path('api/v1',EmployeeApi.as_view()),
    path('api/v1/create',EmployeeCreateApi.as_view()),
    path('api/v1/<int:pk>',EmployeeUpdateApi.as_view()),
    path('api/v1/<int:pk>/delete',EmployeeDeleteApi.as_view()),
]
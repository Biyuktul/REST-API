from django.urls import path
from . import views

urlpatterns = [
    path("", views.items),
    path("delete/<int:id>/", views.remove_item),
    path("update/<int:id>/", views.update_item),
]
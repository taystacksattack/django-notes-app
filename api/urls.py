from django.urls import path
from . import views

urlpatterns = [
    # path method species the route we need to go to
    #home page
    path('', views.getRoutes, name='routes'),
    path('notes/', views.getNotes, name='notes'),
    path('notes/<str:pk>/update/', views.updateNote, name='updated-note'),
    path('notes/<str:pk>/delete/', views.deleteNote, name='deleted-note'),
    path('notes/<str:pk>/', views.getNote, name='note'),
]

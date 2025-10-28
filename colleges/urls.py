# colleges/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('course/<int:course_id>/', views.course_detail_view, name='course_detail'),
    path('city/<int:city_id>/', views.city_colleges_view, name='city_colleges'),
    
    # --- ADD THESE TWO NEW URLS ---
    path('search/', views.search_view, name='search'),
    path('review/', views.review_view, name='add_review'),
    path('college/<int:college_id>/', views.college_detail_view, name='college_detail'),
]
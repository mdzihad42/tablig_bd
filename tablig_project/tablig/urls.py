from django.urls import path
from .views import (
    DashboardView, MemberListView, MemberCreateView, 
    AreaListView, AreaCreateView, GashtListView, GashtCreateView
)

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('members/', MemberListView.as_view(), name='member_list'),
    path('members/add/', MemberCreateView.as_view(), name='member_create'),
    path('areas/', AreaListView.as_view(), name='area_list'),
    path('areas/add/', AreaCreateView.as_view(), name='area_create'),
    path('gasht/', GashtListView.as_view(), name='gasht_list'),
    path('gasht/add/', GashtCreateView.as_view(), name='gasht_create'),
]

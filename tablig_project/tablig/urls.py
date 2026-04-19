from django.urls import path
from .views import (
    DashboardView, 
    MemberListView, MemberCreateView, MemberDetailView, MemberUpdateView, MemberDeleteView,
    AreaListView, AreaCreateView, AreaDetailView, AreaUpdateView, AreaDeleteView,
    GashtListView, GashtCreateView, GashtDetailView, GashtUpdateView, GashtDeleteView,
    TalimListView, TalimCreateView, TalimUpdateView, TalimDeleteView,
    FinanceListView, FinanceCreateView, FinanceUpdateView, FinanceDeleteView,
    JamatListView, JamatCreateView, JamatDetailView, JamatUpdateView, JamatDeleteView
)

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    
    # Member URLs
    path('members/', MemberListView.as_view(), name='member_list'),
    path('members/add/', MemberCreateView.as_view(), name='member_create'),
    path('members/<int:pk>/', MemberDetailView.as_view(), name='member_detail'),
    path('members/<int:pk>/edit/', MemberUpdateView.as_view(), name='member_update'),
    path('members/<int:pk>/delete/', MemberDeleteView.as_view(), name='member_delete'),

    # Area URLs
    path('areas/', AreaListView.as_view(), name='area_list'),
    path('areas/add/', AreaCreateView.as_view(), name='area_create'),
    path('areas/<int:pk>/', AreaDetailView.as_view(), name='area_detail'),
    path('areas/<int:pk>/edit/', AreaUpdateView.as_view(), name='area_update'),
    path('areas/<int:pk>/delete/', AreaDeleteView.as_view(), name='area_delete'),

    # Gasht URLs
    path('gasht/', GashtListView.as_view(), name='gasht_list'),
    path('gasht/add/', GashtCreateView.as_view(), name='gasht_create'),
    path('gasht/<int:pk>/', GashtDetailView.as_view(), name='gasht_detail'),
    path('gasht/<int:pk>/edit/', GashtUpdateView.as_view(), name='gasht_update'),
    path('gasht/<int:pk>/delete/', GashtDeleteView.as_view(), name='gasht_delete'),

    # Talim URLs
    path('talim/', TalimListView.as_view(), name='talim_list'),
    path('talim/add/', TalimCreateView.as_view(), name='talim_create'),
    path('talim/<int:pk>/edit/', TalimUpdateView.as_view(), name='talim_update'),
    path('talim/<int:pk>/delete/', TalimDeleteView.as_view(), name='talim_delete'),

    # Finance URLs
    path('finance/', FinanceListView.as_view(), name='finance_list'),
    path('finance/add/', FinanceCreateView.as_view(), name='finance_create'),
    path('finance/<int:pk>/edit/', FinanceUpdateView.as_view(), name='finance_update'),
    path('finance/<int:pk>/delete/', FinanceDeleteView.as_view(), name='finance_delete'),

    # Jamat URLs
    path('jamat/', JamatListView.as_view(), name='jamat_list'),
    path('jamat/add/', JamatCreateView.as_view(), name='jamat_create'),
    path('jamat/<int:pk>/', JamatDetailView.as_view(), name='jamat_detail'),
    path('jamat/<int:pk>/edit/', JamatUpdateView.as_view(), name='jamat_update'),
    path('jamat/<int:pk>/delete/', JamatDeleteView.as_view(), name='jamat_delete'),
]

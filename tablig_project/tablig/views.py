from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .models import Member, Area, Gasht

class DashboardView(TemplateView):
    template_name = 'tablig/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_members'] = Member.objects.count()
        context['total_areas'] = Area.objects.count()
        context['total_gashts'] = Gasht.objects.count()
        context['recent_members'] = Member.objects.order_by('-created_at')[:5]
        context['recent_gashts'] = Gasht.objects.order_by('-date')[:5]
        return context

class MemberListView(ListView):
    model = Member
    template_name = 'tablig/member_list.html'
    context_object_name = 'members'

class MemberCreateView(CreateView):
    model = Member
    template_name = 'tablig/member_form.html'
    fields = ['name', 'phone_number', 'area', 'address', 'status']
    success_url = reverse_lazy('member_list')

class AreaListView(ListView):
    model = Area
    template_name = 'tablig/area_list.html'
    context_object_name = 'areas'

class AreaCreateView(CreateView):
    model = Area
    template_name = 'tablig/area_form.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('area_list')

class GashtListView(ListView):
    model = Gasht
    template_name = 'tablig/gasht_list.html'
    context_object_name = 'gashts'

class GashtCreateView(CreateView):
    model = Gasht
    template_name = 'tablig/gasht_form.html'
    fields = ['date', 'gasht_type', 'area', 'amir', 'rahbar', 'mutakallim', 'participants', 'remarks']
    success_url = reverse_lazy('gasht_list')

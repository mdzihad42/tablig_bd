from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, Sum
from .models import Member, Area, Gasht, Talim, Finance, Jamat

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'tablig/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_members'] = Member.objects.count()
        context['total_areas'] = Area.objects.count()
        context['total_gashts'] = Gasht.objects.count()
        
        income = Finance.objects.filter(type='income').aggregate(Sum('amount'))['amount__sum'] or 0
        expense = Finance.objects.filter(type='expense').aggregate(Sum('amount'))['amount__sum'] or 0
        context['total_finance'] = income
        context['net_balance'] = income - expense

        # Jamat Distribution for Pie Chart
        jamat_types = dict(Jamat.TYPE_CHOICES)
        jamat_counts = []
        jamat_labels = []
        for key, val in jamat_types.items():
            jamat_labels.append(val)
            jamat_counts.append(Jamat.objects.filter(jamat_type=key).count())
        
        context['jamat_labels'] = jamat_labels
        context['jamat_counts'] = jamat_counts
        
        context['recent_members'] = Member.objects.order_by('-created_at')[:5]
        context['recent_gashts'] = Gasht.objects.order_by('-date')[:5]
        return context

# ... existing views ...

# Member Views
class MemberListView(LoginRequiredMixin, ListView):
    model = Member
    template_name = 'tablig/member_list.html'
    context_object_name = 'members'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Member.objects.filter(
                Q(name__icontains=query) | Q(phone_number__icontains=query) | Q(area__name__icontains=query)
            )
        return Member.objects.all()

class MemberCreateView(LoginRequiredMixin, CreateView):
    model = Member
    template_name = 'tablig/generic_form.html'
    fields = ['name', 'phone_number', 'area', 'address', 'status']
    success_url = reverse_lazy('member_list')

class MemberDetailView(LoginRequiredMixin, DetailView):
    model = Member
    template_name = 'tablig/member_detail.html'
    context_object_name = 'member'

class MemberUpdateView(LoginRequiredMixin, UpdateView):
    model = Member
    template_name = 'tablig/generic_form.html'
    fields = ['name', 'phone_number', 'area', 'address', 'status']
    success_url = reverse_lazy('member_list')

class MemberDeleteView(LoginRequiredMixin, DeleteView):
    model = Member
    template_name = 'tablig/confirm_delete.html'
    success_url = reverse_lazy('member_list')

# Area Views
class AreaListView(LoginRequiredMixin, ListView):
    model = Area
    template_name = 'tablig/area_list.html'
    context_object_name = 'areas'

class AreaCreateView(LoginRequiredMixin, CreateView):
    model = Area
    template_name = 'tablig/area_form.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('area_list')

class AreaDetailView(LoginRequiredMixin, DetailView):
    model = Area
    template_name = 'tablig/area_detail.html'
    context_object_name = 'area'

class AreaUpdateView(LoginRequiredMixin, UpdateView):
    model = Area
    template_name = 'tablig/generic_form.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('area_list')

class AreaDeleteView(LoginRequiredMixin, DeleteView):
    model = Area
    template_name = 'tablig/confirm_delete.html'
    success_url = reverse_lazy('area_list')

# Gasht Views
class GashtListView(LoginRequiredMixin, ListView):
    model = Gasht
    template_name = 'tablig/gasht_list.html'
    context_object_name = 'gashts'

class GashtCreateView(LoginRequiredMixin, CreateView):
    model = Gasht
    template_name = 'tablig/gasht_form.html'
    fields = ['date', 'gasht_type', 'area', 'amir', 'rahbar', 'mutakallim', 'participants', 'remarks']
    success_url = reverse_lazy('gasht_list')

class GashtDetailView(LoginRequiredMixin, DetailView):
    model = Gasht
    template_name = 'tablig/gasht_detail.html'
    context_object_name = 'gasht'

class GashtUpdateView(LoginRequiredMixin, UpdateView):
    model = Gasht
    template_name = 'tablig/generic_form.html'
    fields = ['date', 'gasht_type', 'area', 'amir', 'rahbar', 'mutakallim', 'participants', 'remarks']
    success_url = reverse_lazy('gasht_list')

class GashtDeleteView(LoginRequiredMixin, DeleteView):
    model = Gasht
    template_name = 'tablig/confirm_delete.html'
    success_url = reverse_lazy('gasht_list')

# Talim Views
class TalimListView(LoginRequiredMixin, ListView):
    model = Talim
    template_name = 'tablig/talim_list.html'
    context_object_name = 'talims'

class TalimCreateView(LoginRequiredMixin, CreateView):
    model = Talim
    template_name = 'tablig/generic_form.html'
    fields = ['date', 'book_name', 'topic', 'performed_by', 'participants', 'notes']
    success_url = reverse_lazy('talim_list')

class TalimUpdateView(LoginRequiredMixin, UpdateView):
    model = Talim
    template_name = 'tablig/generic_form.html'
    fields = ['date', 'book_name', 'topic', 'performed_by', 'participants', 'notes']
    success_url = reverse_lazy('talim_list')

class TalimDeleteView(LoginRequiredMixin, DeleteView):
    model = Talim
    template_name = 'tablig/confirm_delete.html'
    success_url = reverse_lazy('talim_list')

# Finance Views
class FinanceListView(LoginRequiredMixin, ListView):
    model = Finance
    template_name = 'tablig/finance_list.html'
    context_object_name = 'finances'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Finance.objects.filter(
                Q(category__icontains=query) | Q(member__name__icontains=query) | Q(description__icontains=query)
            )
        return Finance.objects.all()

class FinanceCreateView(LoginRequiredMixin, CreateView):
    model = Finance
    template_name = 'tablig/generic_form.html'
    fields = ['type', 'amount', 'category', 'date', 'description', 'member']
    success_url = reverse_lazy('finance_list')

class FinanceUpdateView(LoginRequiredMixin, UpdateView):
    model = Finance
    template_name = 'tablig/generic_form.html'
    fields = ['type', 'amount', 'category', 'date', 'description', 'member']
    success_url = reverse_lazy('finance_list')

class FinanceDeleteView(LoginRequiredMixin, DeleteView):
    model = Finance
    template_name = 'tablig/confirm_delete.html'
    success_url = reverse_lazy('finance_list')

# Jamat Views
class JamatListView(LoginRequiredMixin, ListView):
    model = Jamat
    template_name = 'tablig/jamat_list.html'
    context_object_name = 'jamats'

class JamatCreateView(LoginRequiredMixin, CreateView):
    model = Jamat
    template_name = 'tablig/generic_form.html'
    fields = ['member', 'jamat_type', 'start_date', 'end_date', 'status', 'location']
    success_url = reverse_lazy('jamat_list')

class JamatDetailView(LoginRequiredMixin, DetailView):
    model = Jamat
    template_name = 'tablig/jamat_detail.html'
    context_object_name = 'jamat'

class JamatUpdateView(LoginRequiredMixin, UpdateView):
    model = Jamat
    template_name = 'tablig/generic_form.html'
    fields = ['member', 'jamat_type', 'start_date', 'end_date', 'status', 'location']
    success_url = reverse_lazy('jamat_list')

class JamatDeleteView(LoginRequiredMixin, DeleteView):
    model = Jamat
    template_name = 'tablig/confirm_delete.html'
    success_url = reverse_lazy('jamat_list')

from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .models import Member, Area, Gasht, Talim, Finance, Jamat

class DashboardView(TemplateView):
    template_name = 'tablig/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_members'] = Member.objects.count()
        context['total_areas'] = Area.objects.count()
        context['total_gashts'] = Gasht.objects.count()
        context['total_finance'] = Finance.objects.filter(type='income').aggregate(models.Sum('amount'))['amount__sum'] or 0
        context['recent_members'] = Member.objects.order_by('-created_at')[:5]
        context['recent_gashts'] = Gasht.objects.order_by('-date')[:5]
        return context

# ... existing views ...

class TalimListView(ListView):
    model = Talim
    template_name = 'tablig/talim_list.html'
    context_object_name = 'talims'

class TalimCreateView(CreateView):
    model = Talim
    template_name = 'tablig/talim_form.html'
    fields = ['date', 'book_name', 'topic', 'performed_by', 'participants', 'notes']
    success_url = reverse_lazy('talim_list')

class FinanceListView(ListView):
    model = Finance
    template_name = 'tablig/finance_list.html'
    context_object_name = 'finances'

class FinanceCreateView(CreateView):
    model = Finance
    template_name = 'tablig/finance_form.html'
    fields = ['type', 'amount', 'category', 'date', 'description', 'member']
    success_url = reverse_lazy('finance_list')

class JamatListView(ListView):
    model = Jamat
    template_name = 'tablig/jamat_list.html'
    context_object_name = 'jamats'

class JamatCreateView(CreateView):
    model = Jamat
    template_name = 'tablig/jamat_form.html'
    fields = ['member', 'jamat_type', 'start_date', 'end_date', 'status', 'location']
    success_url = reverse_lazy('jamat_list')

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

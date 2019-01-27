from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from facilities.models import Message, Chemical
from facilities.forms import SearchForm


class IndexView(TemplateView):
    template_name = 'facilities/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
                
        context['messages'] = Message.objects.all().order_by('-created_at')

        return context


class ChemicalList(ListView):
    model = Chemical 
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        form = SearchForm(self.request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            context['object_list'] = Chemical.objects.filter(name__startswith=query)
            if not context['object_list']:
                context['object_list'] = Chemical.objects.filter(cas__startswith=query)
        context['form'] = form
        return context


class ChemicalCreate(CreateView):
    model = Chemical
    template_name_suffix = '_create_form'
    success_url = '/facilities/chemical_inventory/'

    fields = '__all__'
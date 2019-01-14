from django.shortcuts import render
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = 'facilities/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['name'] = user.first_name + " " + user.last_name 
        return context
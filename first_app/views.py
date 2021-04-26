from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView

from django.urls import reverse_lazy

from first_app import models
# Create your views here.


class IndexView(ListView):
    context_object_name = 'musician_list'
    model = models.Musician
    template_name = 'first_app/index.html'

class MusicianDetail(DetailView):
    context_object_name = 'musician'
    model = models.Musician
    template_name = 'first_app/musician_details.html'

class AddMusician(CreateView):
    fields = ('first_name','last_name','instrument')
    model = models.Musician
    template_name = 'first_app/musician_form.html'

class UpdateMusician(UpdateView):
    fields = ('first_name','instrument')
    model = models.Musician
    template_name = 'first_app/musician_form.html'

class DeleteMusician(DeleteView):
    context_object_name = 'musician'
    model = models.Musician
    success_url = reverse_lazy('first_app:index')
    template_name = 'first_app/delete_musician.html'


"""
class IndexView(TemplateView):

    template_name = 'first_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sample_text_1']='Fahim'
        context['sample_text_2']='Shakib'
        return context
"""
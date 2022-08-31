from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView
from django.template import loader
from .models import Person, Car



# Create your views here.
def index(req):
    return HttpResponse("I don't KNOW?!")

# def name(req, q_id):
#     person = get_object_or_404(Person, id=q_id)
#     return render(req, 'simple_view/name.html', {'person': person})

class NameView(DetailView):
    model = Person
    template_name = 'simple_view/name.html'


def age(req, q_id):
    person = get_object_or_404(Person, id=q_id)
    return HttpResponse(person.age)
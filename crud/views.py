from django.shortcuts import render
from crud.models import Key
from crud.serializers import KeySerializer
from rest_framework import viewsets
import string
import random
from .forms import Form

def index(request):
    rest_list = Key.objects.order_by('date')
    context = {'rest_list': rest_list}
    return render(request, 'index.html', context)


# Rest api end point
class KeyView(viewsets.ModelViewSet):
    serializer_class = KeySerializer
    queryset = Key.objects.all()


def form(request):
    form = Form(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            key_name= form.cleaned_data.get("key_name")
            key_description= form.cleaned_data.get("key_description")
        generated_key = ''.join(random.choices(string.ascii_letters+string.digits,k=15))
        key = Key(key_name=key_name, key_description=key_description, key=generated_key)
        key.save()
    return render(request,'form.html',{'form':form})
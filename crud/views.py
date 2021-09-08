from django.shortcuts import render
from crud.models import Key
from crud.serializers import KeySerializer
from rest_framework import viewsets

def index(request):
    rest_list = Key.objects.order_by('date')
    context = {'rest_list': rest_list}
    if request.method == "POST":
        return render(request,'form.html')
    return render(request, 'index.html', context)


# Rest api end point
class KeyView(viewsets.ModelViewSet):
    serializer_class = KeySerializer
    queryset = Key.objects.all()
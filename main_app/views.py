from django.shortcuts import render, redirect

from .models import Widget
from .forms import WidgetForm


# Create your views here.

def index(request):
    widgets = Widget.objects.all()
    form = WidgetForm()
    if request.method == 'POST':
        form = WidgetForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'widgets': widgets, 'form':form}
    return render(request, 'index.html', context)

def delete(request, pk):
    delete_widget = Widget.objects.get(id=pk).delete()
    return redirect('/')

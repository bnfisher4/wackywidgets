from django.shortcuts import render

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
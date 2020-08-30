from django.shortcuts import render

# Create your views here.
from .models import T1


def books_short(request):
    queryset = T1.objects.all()
    gt3_shorts = queryset.filter(**{'n_star__gt': 3})
    return render(request, 'index.html', locals())
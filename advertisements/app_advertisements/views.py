from django.shortcuts import render, redirect
from .models import Advertisement
from .forms import AdvertisementForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required

def index(request):
    advertisements = Advertisement.objects.all()
    context = {'advertisements' : advertisements}
    return render(request, 'app_advertisement/index.html', context)

def top_sellers(request):
    return render(request, 'app_advertisement/top-sellers.html')

@login_required(login_url=reverse_lazy('login'))
def advert_post(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            new_advertisement = form.save(commit=False)
            new_advertisement.user = request.user
            new_advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context= {'form' : form}
    return render(request, 'app_advertisement/advertisement-post.html', context)

def advertisement(request):
    return render(request, 'app_advertisement/advertisement.html')
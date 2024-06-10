from django.shortcuts import render, redirect
from .models import Listing # app level folder
from .forms import ListForm
# Create your views here.
def Listing_list(request):
    listings = Listing.objects.all()
    context = {
        "listings": listings
    }
    return render(request, "listings.html", context)

def listing_retrieve(request, pk):
    listing = Listing.objects.get(id=pk)
    context= {
        "listing": listing
    }
    return render(request, "listing.html", context)

def listing_create(request):
    form = ListForm()
    if request.method == "POST":
        form = ListForm(request.POST, request.FILE)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {
        "form": form
    }
    return render(request, "listing_create.html", context)

def listing_update(request, pk):
    listing = Listing.objects.get(id=pk)
    form = ListForm(request.POST, instance=listing)
    if request.method == "POST":
        form = ListForm(request.POST, instance=listing, file=request.FILE)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {
        "form": form
    }
    return render(request, "listing_update.html", context)

def listing_delete(request, pk):
    listing = Listing.objects.get(id=pk)
    listing.delete()
    return redirect("/")
from django.shortcuts import render
from .forms import UploadFileForm
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from serverImage import settings
# Create your views here.
def index(request):
    form = UploadFileForm(
        request.POST or None,
        request.FILES or None
        )
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/done')
    return render(request, "index.html", {"form": form})

def done(request):
    form = UploadFileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        data = settings.MEDIA_URL + str(form.instance.image)
        protocol = "http"
        if request.is_secure():
            protocol = "https"

        host = request.get_host()
        fullURL = protocol+"://"+host+data
        context = {
            "data" : data,
            "url" : fullURL
        }
        return render(request, "done.html", context)
    return render(request, "done.html")
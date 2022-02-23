import base64
from chat.forms import UploadForm
from django.shortcuts import redirect, render
from django.http import JsonResponse
import os
import boto as boto
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from chat.models import Thread
from myproject import settings


@login_required
def messages_page(request):
    threads = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread').order_by('timestamp')
    context = {
        'Threads': threads
    }
    return render(request, 'messages.html', context)


def save(request):
    if (request.method == "POST"):
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            formData = form.save()
            link = str("http://127.0.0.1:8001/download/" + formData.file.name)
            return JsonResponse({"link": link})

    return redirect("messages.html")


def download(request, file_name):
    file_exists = os.path.isfile(f"./uploads/{file_name}")
    return render(request, "messages.html",
                  {"file_exists": file_exists, "url": "/media/" + file_name, "file_name": file_name})

# def send_files(request):
#     if request.method == "POST":
#         name = request.POST.get("filename")
#         myfile = request.FILES.getlist("uploadfoles")
#
#         for f in myfile:
#             myuploadfile(f_name=name, myfiles=f).save()
#
#         return redirect("fileapp:index")

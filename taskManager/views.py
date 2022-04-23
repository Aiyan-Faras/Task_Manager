
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse


class creatNewForm(forms.Form):
    task = forms.CharField(label="Add new Task")

# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []   
    return render(request, "taskmanager/index.html",{
        "tasks" : request.session["tasks"]
    })

def addTask(request):
    if request.method == "POST":
        form = creatNewForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("taskManager:index"))
        else :
            return render(request, "taskManager/addTask.html", {
                "form" : form
            })


    return render(request, "taskManager/addTask.html",{
        "form" : creatNewForm()
    })


from django.shortcuts import render
from . import forms

# Create your views here.

def index(request):
    return render(request,'appThree/index.html')

def form_name_view(request):
    form=forms.FormName()

    if request.method=='post':
        form=forms.FormName(request.post)
        if form.is_valid():
            print("VALIDATION SUCCESS!")
            print("NAME : "+form.cleaned_data['name'])
            print("EMAIL : "+form.cleaned_data['email'])
            print("Text : "+form.cleaned_data['text'])

    return render(request,'appThree/form_page.html',{'form':form})

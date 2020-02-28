from django.shortcuts import render

# Create your views here.
def index(request):
    mydic={'text':'hello world','number':100}
    return render(request,'appThree/index.html',mydic)

def other(request):
    return render(request,'appThree/other.html')

def relative(request):
    return render(request,'appThree/relative_url_template.html')

from django.shortcuts import render
from ProjectTwoApp.models import User
from ProjectTwoApp.forms import NewUserForm
# Create your views here.

def index(request):
    return render(request,'ProjectTwoApp/index.html')


def users(request):

    user_list=User.objects.order_by('first_name')
    user_list={'users':user_list}
    return render(request,'ProjectTwoApp/users.html',context=user_list)


def basicForm(request):

    form=NewUserForm()
    if request.method =='POST':
        form=NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error Form Invalid')

    return render(request,'ProjectTwoApp/basicForm.html',{'form':form})

from django.shortcuts import render
from formapp.form import UserProfile
# Create your views here.
def index(request):
    form = UserProfile()
    if request.method == 'POST':
        form = UserProfile(request.POST)
        if form.is_valid():
            print('validation Success')
            # print(form.cleaned_data['name'])
            # print(form.cleaned_data['company'])
    context = {
        'heading' : 'User profile Form',
        'form' : form
    }
    return render(request,'index.html',context)
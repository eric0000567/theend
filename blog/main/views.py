from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls.base import reverse
from django.contrib.auth.decorators import login_required

@login_required
def main(request):
    '''
    Render the main page
    '''
    context = {'like':'Django 很棒'}
    return render(request, 'main/main.html', context)
@login_required
def about(request):
    '''
    Render the about page
    '''
    return render(request, 'main/about.html')

def admin_required(func):
    def auth(request, *args, **kwargs):
        if not request.user.is_superuser:
            messages.error(request, '請以管理者身份登入')
            return redirect(reverse('account:login') + '?next=' + request.get_full_path())
        return func(request, *args, **kwargs)
    return auth
# Create your views here.
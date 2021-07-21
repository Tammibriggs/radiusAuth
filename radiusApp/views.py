from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .config import loginradius

def register_n_login(request):
    return render(request, 'index.html')

def profile(request):

    if request.GET.get('token'):    
        try:
            user_data = loginradius.authentication.get_profile_by_access_token(request.GET.get('token'))
        except Exception as inst:
            return HttpResponse(inst)
    else:
        return redirect('access')

    return render(request, 'profile.html', {'user_data':user_data})
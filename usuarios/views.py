from dajax.core import Dajax
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django_ajax.decorators import ajax
import pythoncom
from usuarios import iSeries
from usuarios.models import SignUpForm

# Create your views here.

def signup(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = SignUpForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass

            # Process the data in form.cleaned_data
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            usuario_sico = form.cleaned_data["usuario_sico"]
            contrasenia_sico = form.cleaned_data["contrasenia_sico"]

            # At this point, user is a User object that has already been saved
            # to the database. You can continue to change its attributes
            # if you want to change other fields.
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.usuario_sico = usuario_sico
            user.contrasenia_sico = contrasenia_sico

            # Save new user attributes
            user.save()

            return HttpResponseRedirect(reverse('main'))  # Redirect after POST
    else:
        form = SignUpForm()

    data = {
        'form': form,
    }
    return render_to_response('signup.html', data, context_instance=RequestContext(request))



def main(request):
    #return render_to_response('main.html', {}, context_instance=RequestContext(request))
    return ingreso(request)

def ingreso(request):
    error = None
    try:
        logout(request)
    except:
        pass
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']


        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/home')
        elif username and password:
            error = 1

    return render_to_response('login.html', {'errors': error}, context_instance=RequestContext(request))

@login_required()
def home(request):
    pythoncom.CoInitialize()
    #conn = iSeries.ConnectionManager()
    print request.user.usuario_sico
    print request.user.contrasenia_sico
    #availableConnection = conn.getAvailableConnection()
    #conn.openSession(availableConnection, request.user.usuario_sico, request.user.contrasenia_sico)
    #conn.setActiveSession(availableConnection)
    return render_to_response('home.html', {'user': request.user, 'conn': None}, context_instance=RequestContext(request))

@ajax
def multiply(request):
    a = int(request.POST['a'])
    b = int(request.POST['b'])
    c = a * b
    dajax = Dajax()
    dajax.assign('#result', 'value', str(c))
    return dajax.calls
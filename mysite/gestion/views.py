from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Student, Teacher, Subject, Course, Career, Period, Grades, Registration, Person
from django.core.mail import send_mail

# Create your views here.
def index(request):
	return render(request, 'index.html', {'message': 'Bienvenido a Index'})

def home(request):
	return render(request, 'home.html')

def formContact(request):
	return render(request, 'form_contact.html')

def contactar(request):
	if request.method == 'POST':
		pass
		# envio de email de contacto
		# asunto = request.POST['txtAsunto']
		# mensaje = request.POST['txtMensaje'] + "/ Email: " + request.POST['txtEmail']
		# email_desde = settings.EMAIL_HOST_USER
		# email_para = [""]		#el email que guardamos en settings.py
		# send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)
		# return render(request, "contactoExitoso.html")
	return render(request, "contacto_exitoso.html")
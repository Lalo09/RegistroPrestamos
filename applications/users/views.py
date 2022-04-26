from django.shortcuts import render
from django.core.mail import send_mail
from django.views.generic import View,TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserRegisterForm,LoginForm,UpdatePasswordForm,VerificacionForm

from .models import User
from .functions import code_generate

class UserRegisterView(FormView):
    template_name = "users/register.html"
    form_class = UserRegisterForm
    success_url = '.'

    def form_valid(self,form):

        #Generar codigo de verificacion
        codigoRegistro = code_generate()

        usuario = User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password'],
            nombres = form.cleaned_data['nombres'],
            apellidos = form.cleaned_data['apellidos'],
            genero = form.cleaned_data['genero'],
            codigo = codigoRegistro
        )

        #Enviar codigo al email del usuario
        asunto = "Confirmacion de registro"
        mensaje = "Codigo de verificacion: "+codigoRegistro
        email_remitente = 'jose960808@gmail.com'
        print("============")
        print("Codigo de verificacion: "+codigoRegistro)

        send_mail(asunto,mensaje,email_remitente,[form.cleaned_data['email'],])

        #Reedirigir a pantalla de validacion, enviar parametro con el id del usuario registrado
        return HttpResponseRedirect(
            reverse(
                'users_app:verificacion',
                kwargs={'id':usuario.id}
            )
        )

#Pantalla para iniciar sesion
class LoginUser(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:index')

    def form_valid(self,form):

        #Iniciar proceso de autenticacion
        user = authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password']
        )

        login(self.request,user)

        return super(LoginUser,self).form_valid(form)

#Cerrar sesion con view- padre de todas las vistas
class LogoutView(View):

    def get(self,request,*args,**kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'users_app:login'
            )
        )

#Actualizar contraseña, recomendacion: crear dos views, una actualizar datos de
#usuario como nombre, email, etc y otro exclusivo para contraseña
class UpdatePasswordView(LoginRequiredMixin,FormView):
    template_name = 'users/update.html'
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('users_app:login')
    login_url = reverse_lazy('users_app:login')

    def form_valid(self,form):

        usuario = self.request.user

        ##Modificar para permitir loguearse solo a usuarios activos(is_active)

        user = authenticate(
            username=usuario.username,
            password = form.cleaned_data['password1']
        )

        if user:
            new_password = form.cleaned_data['password2']
            usuario.set_password(new_password)
            usuario.save()
        else:
            return HttpResponseRedirect(
                reverse(
                    'users_app:error'
                )
            )

        logout(self.request)
        return super(UpdatePasswordView,self).form_valid(form)

class ErrorView(LoginRequiredMixin,TemplateView):
    template_name = 'users/error_actualizar_clave.html'
    login_url = reverse_lazy('users_app:login')

class CodeVerificationView(FormView):
    template_name = 'users/verification.html'
    form_class = VerificacionForm
    success_url = reverse_lazy('users_app:login')

    #Enviar informacion al formulario
    def get_form_kwargs(self):
        kwargs =  super(CodeVerificationView,self).get_form_kwargs()
        kwargs.update(
            {
                'id':self.kwargs['id']
            }
        )

        return kwargs

    def form_valid(self,form):
        id_usuario = self.kwargs['id']

        #Actualizar estatus a activo cuandoe l codigo es correcto
        User.objects.filter(
            id=self.kwargs['id']
        ).update(
            is_active=True
        )
        
        return super(CodeVerificationView,self).form_valid(form)
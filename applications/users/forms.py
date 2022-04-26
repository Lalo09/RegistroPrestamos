from django import forms
from django.contrib.auth import authenticate
from .models import User

class UserRegisterForm(forms.ModelForm):

    #Campos extra
    password = forms.CharField(
        label = 'Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña'
            }
        )
    )

    passwordConfirmar = forms.CharField(
        label = 'Cofirmar contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Repetir contraseña'
            }
        )
    )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'nombres',
            'apellidos',
            'genero'
        )
    
    #Validacion propia
    def clean_passwordConfirmar(self):
        if self.cleaned_data['password'] != self.cleaned_data['passwordConfirmar']:
            self.add_error('passwordConfirmar','Las contraseñas no coinciden')

class LoginForm(forms.Form):
    
    username = forms.CharField(
        label = 'Usuario',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'username',
                'style': '{margin:10px}',
            }
        )
    )

    password = forms.CharField(
        label = 'Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña'
            }
        )
    )

    #En caso que los datos no sean correctos
    def clean(self):
        cleaned_data = super(LoginForm,self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not authenticate(username=username, password=password):
            raise forms.ValidationError('Datos de usuario o contraseña incorrecto')

        return self.cleaned_data

class UpdatePasswordForm(forms.Form):

    password1 = forms.CharField(
        label = 'Contraseña actual',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña actual'
            }
        )
    )

    password2 = forms.CharField(
        label = 'Contraseña nueva',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña nueva'
            }
        )
    )

class VerificacionForm(forms.Form):
    codRegistro = forms.CharField(required=True)

    #Cargar parametros 
    def __init__(self,id,*args,**kwargs):
        self.id_user = id
        super(VerificacionForm,self).__init__(*args,**kwargs)

    #Validacion de codigo
    def clean_codRegistro(self):
        codigo = self.cleaned_data['codRegistro']

        if len(codigo) == 6:
            #Verificar si el codigo del usuario y el id son validos
            activo = User.objects.cod_validation(
                self.id_user,
                codigo
            )
            if not activo:
                raise forms.ValidationError("Error en codigo")
        else:
            raise forms.ValidationError("Error en codigo")
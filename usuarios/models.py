# coding=utf-8
# Create your models here.
import datetime
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.db import models
from inventario.models import contrato
from django.utils.translation import ugettext, ugettext_lazy as _


class usuarioSico(models.Model):
    nombre = models.CharField(max_length=10, verbose_name='Nombre de Usuario en Sico')
    clave = models.CharField(max_length=10, verbose_name='Contraseña en Sico')
    contrato = models.ForeignKey('inventario.contrato')

    def __unicode__(self):
        return '%s - %s' % (self.nombre, self.contrato.num)

    class Meta:
        verbose_name='Usuario en Sico'
        verbose_name_plural='Usuarios en Sico'




#MODICANDO EL USUARIO DE MODELO USER
User.add_to_class('direccion', models.CharField(max_length=100, null=True, blank=True))
User.add_to_class('telefono', models.CharField(max_length=10, null=True, blank=True))
User.add_to_class('celular', models.CharField(max_length=10, null=True, blank=True))
User.add_to_class('sesion_sico', models.CharField(max_length=2, null=True, blank=True))
User.add_to_class('usuario_sico', models.ManyToManyField(usuarioSico, blank=True, null=True))
#User.add_to_class('amigos', models.ManyToManyField('self', symmetrical=True,  ))



#GEOLOCALIZACIÓN
class posicion(models.Model):
    fechaHora = models.DateTimeField(verbose_name='Fecha y Hora', auto_now=True, auto_now_add=True)
    latitud = models.CharField(max_length=25, verbose_name='Latitud')
    longitud = models.CharField(max_length=25, verbose_name='Longitud')
    altura = models.CharField(max_length=25, verbose_name='Longitud', null=True, blank=True, default='')
    usuario = models.ForeignKey(User)
    cuadrilla = models.ForeignKey('ingresos.cuadrilla', blank=True, null=True, default=None)



#FORMULARIOS
class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name',
                  #'usuario_sico', 'contrasenia_sico'
        ]
        widgets = {
            'password': forms.PasswordInput(),
            #'contrasenia_sico': forms.PasswordInput(),
        }


class LogIn(forms.Form):
    usuario = forms.CharField(
        max_length=10,
        required=True,
        label='Nombre de Usuario',
        widget=forms.TextInput(attrs={'placeholder': 'Escriba su nombre de usuario'})
    )
    clave = forms.CharField(
        max_length=10,
        required=True,
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'placeholder': ''})
    )
    sico = forms.ModelChoiceField(
        queryset=contrato.objects.filter(finalVigencia__gte=datetime.date.today()),
        #initial=contrato.objects.first().num,
        label='Contrato Nro.'
    )


class MyUserChangeForm(forms.ModelForm):
    username = forms.RegexField(
        label=_("Username"), max_length=30, regex=r"^[\w.@+-]+$",
        help_text=_("Required. 30 characters or fewer. Letters, digits and "
                      "@/./+/-/_ only."),
        error_messages={
            'invalid': _("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")})
    password = ReadOnlyPasswordHashField(label=_("Password"),
        help_text=_("Raw passwords are not stored, so there is no way to see "
                    "this user's password, but you can change the password "
                    "using <a href=\"password/\">this form</a>."))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'direccion', 'telefono', 'celular', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(MyUserChangeForm, self).__init__(*args, **kwargs)
        f = self.fields.get('user_permissions', None)
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.instance.password


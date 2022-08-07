from django import forms
from AppProyFinal.models import Habitacion, Reserva

#class HabitacionFormulario(forms.Form):
#    numero=forms.IntegerField()
#    piso=forms.IntegerField()
#    capacidad=forms.IntegerField()
#    descripcion=forms.CharField(max_length=150)
#    ocupada=forms.BooleanField()
#    precio= forms.IntegerField()
    #hotel = forms.ForeignKey(Hotel, on_delete=forms.CASCADE)

class HotelFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    fechaApertura=forms.DateField()
    abierto=forms.BooleanField()
    estrellas=forms.IntegerField()
    ciudad=forms.CharField(max_length=50)
    pais=forms.CharField(max_length=50)
    direccion=forms.CharField(max_length=100)

class HabitacionFormulario(forms.ModelForm):
    class Meta:
        model= Habitacion
        fields = '__all__' # Or a list of the fields that you want to include in your form

        
class ReservaFormulario(forms.ModelForm):
    class Meta:
        model= Reserva
        fields = '__all__' # Or a list of the fields that you want to include in your form
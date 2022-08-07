from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from AppProyFinal.models import Hotel, Habitacion, Reserva
from AppProyFinal.forms import HotelFormulario, HabitacionFormulario, ReservaFormulario

# Create your views here.
#def verFamiliares(request):

#    familiares = Hotel.objects.all()

#    template = loader.get_template('familiares.html')
    
 #   documento = template.render({'familiares': familiares})
 #   return HttpResponse(documento)

def inicio(request):
    return render(request, "AppProyFinal/inicio.html")

def hoteles(request):
    return render(request, "AppProyFinal/hoteles.html")

def habitaciones(request):
    return render(request, "AppProyFinal/habitaciones.html")

def reservas(request):
    return render(request, "AppProyFinal/reservas.html")

def contacto(request):
    return render(request, "AppProyFinal/contacto.html")

def habitacionesFormulario(request):
    


    if request.method == 'POST':
        miFormulario = HabitacionFormulario(request.POST) # acá llega la info del HTML

        print (miFormulario)
        if miFormulario.is_valid: #Si pasa la validación de Django:
            informacion = miFormulario.cleaned_data
            instHotel = Habitacion(numero=informacion['numero'], capacidad=informacion['capacidad'], descripcion=informacion['descripcion'], piso=informacion['piso'], precio=informacion['precio'], ocupada=False, hotel=informacion['hotel'])
            instHotel.save()
            return render(request, "AppProyFinal/inicio.html") #volvemos a la misma pantalla
    
    else:
        
        miFormulario = HabitacionFormulario() # Formulario vacio para construir el html
    
    return render(request, "AppProyFinal/habitacionesFormulario.html", {"miFormulario": miFormulario})





def hotelesFormulario(request):

    if request.method == 'POST':
        miFormulario = HotelFormulario(request.POST) # acá llega la info del HTML

        print (miFormulario)
        if miFormulario.is_valid: #Si pasa la validación de Django:
            informacion = miFormulario.cleaned_data
            instHotel = Hotel(nombre=informacion['nombre'], pais=informacion['pais'], ciudad=informacion['ciudad'], direccion=informacion['direccion'], estrellas=informacion['estrellas'], abierto=False, fechaApertura=informacion['fechaApertura'])
            instHotel.save()
            return render(request, "AppProyFinal/hotelesFormulario.html") #volvemos a la misma pantalla
    
    else:
        
        miFormulario = HotelFormulario() # Formulario vacio para construir el html
    
    
    return render(request, "AppProyFinal/hotelesFormulario.html", {"miFormulario": miFormulario})



def hotelesBusqueda(request):
    return render(request, "AppProyFinal/hotelesBusqueda.html")

def buscar(request):

    if request.GET["ciudad"]:
    #respuesta = f"Estoy buscando el Hotel: {request.GET['nombre'] }"
        ciudad = request.GET['ciudad']
        hoteles = Hotel.objects.filter(ciudad__icontains=ciudad)

        return render(request,"AppProyFinal/resultadosBusquedaHoteles.html", {"hoteles":hoteles, "ciudad": ciudad})

    else:
        respuesta= "No enviaste datos"

    #return HttpResponse(respuesta)
    return render(request, "AppProyFinal/resultadosBusquedaHoteles.html", {"respuesta":respuesta})



def reservasFormulario(request):

    if request.method == 'POST':
        miFormulario = ReservaFormulario(request.POST) # acá llega la info del HTML

        print (miFormulario)
        if miFormulario.is_valid: #Si pasa la validación de Django:
            informacion = miFormulario.cleaned_data
            instHotel = Reserva(nombre=informacion['nombre'], apellido=informacion['apellido'], fechaDesde=informacion['fechaDesde'], fechaHasta=informacion['fechaHasta'], cantPersonas=informacion['cantPersonas'], habitacion=informacion['habitacion'], comentarios=informacion['comentarios'], metodoPago=informacion['metodoPago'])
            instHotel.save()
            return render(request, "AppProyFinal/reservasFormulario.html") #volvemos a la misma pantalla
    
    else:
        
        miFormulario = ReservaFormulario() # Formulario vacio para construir el html
    
    
    return render(request, "AppProyFinal/reservasFormulario.html", {"miFormulario": miFormulario})
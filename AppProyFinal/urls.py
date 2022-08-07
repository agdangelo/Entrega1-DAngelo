from django.urls import path
from AppProyFinal.views import inicio, hoteles, habitaciones, reservas, contacto, habitacionesFormulario, hotelesFormulario, hotelesBusqueda, buscar, reservasFormulario


urlpatterns = [
    
    path('inicio', inicio, name ="Inicio"),
    path('hoteles', hoteles, name ="Hoteles"),
    path('habitaciones', habitaciones, name ="Habitaciones"),
    path('reservas', reservas, name ="Reservas"),
    path('contacto', contacto, name ="Contacto"),
    path('habFormulario', habitacionesFormulario, name ="HabitacionesFormulario"),
    path('reservasFormulario', reservasFormulario, name ="ReservasFormulario"),
    path('hotelesFormulario', hotelesFormulario, name ="HotelesFormulario"),
    path('hotelesBusqueda', hotelesBusqueda, name ="HotelesBusqueda"),
    path('buscar/', buscar),
    ]



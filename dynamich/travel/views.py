from django.shortcuts import render
from . import models
# Create your views here.

def index(request):
    dest1 = models.Destinations(name='Tehran', image="destination_1.jpg", price=400, desc='never sleep')
    dest2 = models.Destinations(name='Kerman', image="destination_2.jpg", price=250, desc='always hight')
    # dest1 = models.Destinations()
    # dest2 = models.Destinations()
    #
    # dest1.name = 'Tehran'
    # dest1.price = 700
    # dest1.img = 'destination_1.jpg'
    # dest1.desc = "never sleep"
    #
    # dest2.name = 'Ghomm'
    # dest2.price = 100
    # dest2.img = 'destination_2.jpg'
    # dest2.desc = "city of clergies"

    # dest1 = models.Destinations()
    # dest2 = models.Destinations()
    # dest1(name='Tehran', price=450, image="destination_1.jpg", description="A very crowded and polluted city...")
    # dest2(name="Sistan", image="destination_2.jpg", price=100, description="The most deprived province in Iran...")

    dests = [dest1, dest2]
    return render(request, 'index.html', {'dest': dests})

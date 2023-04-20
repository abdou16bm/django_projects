from django.shortcuts import render
from django.http import HttpResponse
from listing.models import Product

# Create your views here.

def hello(request):
    product = Product.objects.all()
    print(product[0].name)
#     return HttpResponse("<h1>test view content  </h1>")
    return HttpResponse(f"""
            <h1>Hello Django !</h1>
            <p>Mes groupes préférés sont :<p>
            <ul>
                <li>{product[0].name}</li>
                <li>{product[1].name}</li>
                <li>{product[2].name}</li>
            </ul>
    """)


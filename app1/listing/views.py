from django.shortcuts import render,redirect
from django.http import HttpResponse
from listing.models import Product
from listing.form import producAddForm

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



def helloPattern(request):
    product = Product.objects.all()
    return render(request,
                  'listing/hello.html',
                  {'products': product})




def productList(request):
    product = Product.objects.all().order_by('name')
    # product = Product.objects.all().order_by('-id')
    return render(request,
                  'listing/productList.html',
                  {'products': product})


def productDetail(request,id):
    product = Product.objects.get(id=id)
    return render(request,
                  'listing/productDetail.html',
                  {'product': product})


def productDelete(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('/product/list')


def productAdd(request):
    print('La méthode de requête est : ', request.method)
    print('Les données POST sont : ', request.POST)

    if request.method == "POST":
        form = producAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/product/list')
    else:
        form = producAddForm()

    return render(request,
                  'listing/productAdd.html',
                  {'form': form})



def productUpdate(request, id):
    product = Product.objects.get(id=id)
    print('test update')
    if request.method == "POST":
        print('POST update')
        form = producAddForm(request.POST,instance=product)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('/product/list')
    else:
        print('not valide')
        form = producAddForm(instance=product)

    return render(request,
                  'listing/productUpdate.html',
                  {'form': form})


def productAddSimple(request):
    print('La méthode de requête 2 est : ', request.method)
    print('Les données POST sont : ', request.POST)


    if request.method == "POST":
        print('POST add simple')
        print('Les données POST name : ', request.POST["name"])
        product = Product()
        product.name = request.POST["name"]
        product.date_in = request.POST["date_in"]

        product.save();

        return redirect('/product/list')
    else:
        return render(request,
                      'listing/productAddSimple.html')



# django_projects

### clone the repository
1. git clone https://github.com/abdou16bm/django_projects.git

### create virtual env
1. cd projectsDir 
2. python -m venv env

### activate env
1. cd env/Scripts 
2. source activate
Activate.ps1

3. deactivate (pour desactiver le venv)

### install django and create project (Global APP)
1. pip install django 
2. django-admin startproject app1 
3. python manage.py runserver (run global application)
4. python manage.py migrate

### create 'listing' APP (sub app)
1. python manage.py startapp listing 


### install 'listing' APP on Global project
1. open file : app1/settings.py
2. Add 'listing' to INSTALLED_APPS = []

	INSTALLED_APPS = [
		'django.contrib.admin',
		'django.contrib.auth',
		'django.contrib.contenttypes',
		'django.contrib.sessions',
		'django.contrib.messages',
		'django.contrib.staticfiles',
		'listing'
	]


### create views : open file listing/views.py
1. add this import : from django.http import HttpResponse 
2. add function : 

	hello(request):
	urn HttpResponse("<h1>test view content</h1>")

### create route (url) : open file app1/urls.py
1. add this import : from listing import views
2. Add 'hello' to urlpatterns = []

	urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
   ]




### create model : open file listing/models.py
1. add model class Product :
	
   class Product (models.Model):
	name = models.fields.CharFields(max_length=100)


2. use migrations commandes :
3. create migrations files : python manage.py makemigrations 
4. execute the migration to created on database : python manage.py migrate 

5. test model with django shell :

    python manage.py shell

    from listing.models import Product

    product = Product()
    product.name = "produit1"
    product.save();

    product = Product()
    product.name = "produit2"
    product.save();

    product = Product.objects.create(name = "produit3")

    product
    <Product: Product object (3)>


### create view template : create file listing/template/listing/hello.html and base.html
1. Add hello.html : 

 {% extends 'listing/base.html' %}
    {% block content %}
        <h1>Hello Django !</h1>
        <p>Mes produits sont :<p>
        <ul>
            <li>{{products.0.name}}</li>
            <li>{{products.1.name}}</li>
            <li>{{products.2.name}}</li>
        </ul>
        ....
        ....
        ....
        ...
        ..
    {% endblock %}


2. add base.html : 
       <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>app1</title>
        </head>
        <body>
        {% block content %}{% endblock %}
        </body>
        </html>


3. add views function : open file listing/views.py

    def helloPattern(request):
        product = Product.objects.all()
        return render(request,
                      'listing/hello.html',
                      {'products': product})



### add style CSS : create file listing/static/listing/style.css 
add this code to base.html : 

    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
        ....
        ....
        <link rel="stylesheet" href="{% static 'listing/style.css' %}" />
        ....
        ....
    </html>



# Activate Admin panel
1. execute : python manage.py createsuperuser
2. username : admin, password : admin
3. add this lines to : listings/admin.py

    from django.contrib import admin
    
    from listing.models import Product
    
    admin.site.register(Product)

4. connect to : http://127.0.0.1:8000/admin 


# custum Admin panel
1. add this class to : listings/admin.py

    class ProductAdmin(admin.ModelAdmin):
        list_display = ('name', 'category', 'date_in') # liste les champs a afficher
2. add this argument 'ProductAdmin' to : listings/admin.py
3. 
    admin.site.register(Product,ProductAdmin)


# add foreign key
1. add this class to model : 

    class Type (models.Model):
        name = models.fields.CharField(max_length=100)
    
2. add foregn key to class product with this line : 

     category = models.ForeignKey(Type, null=True, on_delete=models.SET_NULL)

3. add this to : : listings/admin.py
    
    from listing.models import Type

    admin.site.register(Type)




## postgresl using
1. pip install psycopg2
2. add to settings.py : 

       'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': 'root',
            'HOST': 'localhost',
            'PORT': '5432'
        }
3. create migrations files : python manage.py makemigrations 
4. execute the migration to created on database : python manage.py migrate 


### product detail page :
1. Add 'product/<int:id>/' to urlpatterns = [] in file : app1/urls.py

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('hello/', views.hello),
        path('hello/pattern', views.helloPattern),
        path('product/<int:id>/', views.product_detail),
    ]

2. Add 'productDetail' function to file : app1/listing/views.py

    def productDetail(request,id):
        product = Product.objects.get(id=id)
        return render(request,
                      'listing/productDetail.html',
                      {'product': product})

3. create page app1/listing/template/listing/productDetail.html

    
### form add product :
1. create file app1/listing/form.py :
    
    from django import forms
    from .models import Product
    
    class producAddForm(forms.ModelForm):
      class Meta:
        model = Product
        fields = ["name", "date_in",]
        labels = {'name': "Name", "date_in": "date",}
2. create template : productAdd.html
   
    {% extends 'listing/base.html' %}
    
    {% block content %}
    <form method="post">
        {% csrf_token %}
        {{ form.as_p  }}
        <input type="submit" value="AJOUTER">
    </form>
    
    {% endblock %}

3. add URL :   path('product/add', views.productAdd),
4. add view productAdd:

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


### form update product : edit (get data to form)
1. create file app1/listing/form.py :

   from django import forms
   from .models import Product

   class producAddForm(forms.ModelForm):
   class Meta:
   model = Product
   fields = ["name", "date_in",]
   labels = {'name': "Name", "date_in": "date",}
2. create template : productUpdate.html

   {% extends 'listing/base.html' %}

   {% block content %}
    <form method="post">
        {% csrf_token %}
        {{ form.as_p  }}
        <input type="submit" value="AJOUTER">
    </form>

   {% endblock %}

3. add URL :   path('product/<int:id>/edit', views.productUpdate),
4. add view productUpdate:
    
    def productUpdate(request, id):
        product = Product.objects.get(id=id)
        form = producAddForm(instance=product)
        return render(request,
        'listing/productUpdate.html',
        {'form': form})


### form update product : save data form
1. update view productUpdate:



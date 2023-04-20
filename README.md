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
		python manage.py makemigrations
		python manage.py migrate

3. test model with django shell :

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


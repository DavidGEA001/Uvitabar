from django.shortcuts import render, redirect
from blog.models import Article
from django.contrib.auth.decorators import login_required
from carritoapp.carrito import Carrito
# Create your views here.}


@login_required(login_url = "login" )
def pagina_carrito(request):
    article = Article.objects.all()
    return render(request, 'carrito2.html', {
        'articles': article})


@login_required(login_url = "login" )
def agregar_producto(request, article_id):
    carrito = Carrito(request)
    article = Article.objects.get(id=article_id)
    carrito.agregar(article)
    return redirect("carrito")

@login_required(login_url = "login" )
def eliminar_producto(request, article_id):
    carrito = Carrito(request)
    article = Article.objects.get(id=article_id)
    carrito.eliminar(article)
    return redirect("carrito")

@login_required(login_url = "login" )
def restar_producto(request, article_id):
    carrito = Carrito(request)
    article = Article.objects.get(id=article_id)
    carrito.restar(article)
    return redirect("carrito")

@login_required(login_url = "login" )
def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carrito")




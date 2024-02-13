from blog.models import Article

class Carrito:   
    
    def __init__(self, request):
        self.request = request 
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, Article):
        id = str(Article.id)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "article_id" : Article.id,
                "price": Article.price,
                "title": Article.title,
                "acumulado": Article.price,
                "cantidad": 1,
                
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += Article.price
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, Article):
        id = str(Article.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, Article):
        id = str(Article.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= Article.price
            if self.carrito[id]["cantidad"] <= 0:
                self.eliminar(Article)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True
from tornado.web import RequestHandler
from models.product_model import Product


class Index(RequestHandler):
    def get(self):
        products = Product.get_products()
        self.render('index.html', products=products)

class New(RequestHandler):
    def get(self):
        self.render('new.html')
        
    def post(self):
        name = self.get_argument('name', None)
        price = self.get_argument('price', None)
        product = Product(name=name, price=price)
        product.save()
        self.redirect('/')
        
class Update(RequestHandler):
    def get(self, id, status):
        product = Product.get_product(id=id)
        product.status = status
        product.update()
        self.redirect('/')

class Delete(RequestHandler):
    def get(self, id):
        product = Product.get_product(id=id)
        product.delete()
        self.redirect('/')

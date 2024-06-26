from tornado import ioloop, httpserver
from tornado.web import Application
from controllers.product_controller import Index, New, Update, Delete

class RunApp(Application):
    def __init__(self):
        handlers = [
            ('/', Index),
            ('/product/new', New),
            (r'/product/update/(\d+)/status/(\d+)', Update),
            (r'/product/delete/(\d+)', Delete)
        ]
        
        settings = dict(
            debug = True,
            template_path = 'views',
            static_path = 'static'
        )
        
        Application.__init__(self, handlers, **settings)
        
if __name__ == '__main__':
    http_server = httpserver.HTTPServer(RunApp())
    http_server.listen(5000)
    ioloop.IOLoop.instance().start()
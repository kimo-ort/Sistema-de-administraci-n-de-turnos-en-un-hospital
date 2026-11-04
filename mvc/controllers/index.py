import web

render = web.template.render('mvc/views', basa='templates')

class Index:
    def GET(self):
        return render.index()
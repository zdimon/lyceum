import web
        
urls = (
    '/', 'index',
    '/insert/(.*)', 'insert'
)
app = web.application(urls, globals())

db = web.database(dbn='mysql', user='root', pw='1q2w3e', db='mydb')

class index:        
    def GET(self):
        users = db.select('user')
        out = 'Hello '
        for u in users:
            out = out+' '+u.name
        return out

class insert:        
    def GET(self, name):
        n = db.insert('user', name=name)
        return 'Ok'


if __name__ == "__main__":
    app.run()

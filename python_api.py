import tornado.ioloop
import tornado.web
import sqlite3


class Who(tornado.web.RequestHandler):
    def get(self):
        """get请求"""
        ids = self.get_argument('id')
        hash = self.get_argument('hash')
        if hash == "7DFxxxxxxxxxxxxxxxxxxxx":
            con = sqlite3.connect('steemdatabase.db')
            cur = con.cursor()
            whois = 'select * from daili where name like "%s"' % ids
            cur.execute(whois)
            deleall = cur.fetchall()
            con.commit()
            data = []
            for i in deleall:
                d = {"name": i[0], "towho": i[1], "sp": i[2], "vesting": i[3], "time": i[4]}
                data.append(d)
            deleall = {"data": data}
            con.commit()
        else:
            deleall = {"data": "hash_error"}
        self.write(deleall)

class Towho(tornado.web.RequestHandler):
    def get(self):
        """get请求"""
        ids = self.get_argument('id')
        hash = self.get_argument('hash')
        if hash == "7DFC55A884A937A8AB81CD1EBAB3385E":
            con = sqlite3.connect('steemdatabase.db')
            cur = con.cursor()
            whois = 'select * from daili where towho like "%s"' % ids
            cur.execute(whois)
            deleall = cur.fetchall()
            con.commit()
            data = []
            for i in deleall:
                d = {"name": i[0], "towho": i[1], "sp": i[2], "vesting": i[3], "time": i[4]}
                data.append(d)
            deleall = {"data": data}
            con.commit()
        else:
            deleall = {"data": "hash_error"}
        self.write(deleall)

application = tornado.web.Application([(r"/who", Who),(r"/towho", Towho) ])

if __name__ == "__main__":
    application.listen(666)
    tornado.ioloop.IOLoop.instance().start()

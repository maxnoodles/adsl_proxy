# coding=utf-8
import json
import tornado.ioloop
import tornado.web
from tornado.web import RequestHandler, Application
from config import *
from db import RedisClient


class MainHandler(RequestHandler):

    redis = RedisClient()

    def get(self, api=''):
        if not api:
            links = ['random', 'proxies', 'names', 'all', 'count']
            self.write('<h4>Welcome to ADSL Proxy API</h4>')
            for link in links:
                self.write('<a href=' + link + '>' + link + '</a><br>')

        if api == 'random':
            result = self.redis.random()
            if result:
                self.write(result)

        if api == 'names':
            result = self.redis.names()
            if result:
                self.write(json.dumps(result))

        if api == 'proxies':
            result = self.redis.proxies()
            if result:
                self.write(json.dumps(result))

        if api == 'all':
            result = self.redis.all()
            if result:
                self.write(json.dumps(result))

        if api == 'count':
            self.write(str(self.redis.count()))


def run():
    application = Application([
        (r'/', MainHandler),
        (r'/(.*)', MainHandler),
    ])
    application.listen(API_PORT)
    print('ADSL API Listening on', API_PORT)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    run()
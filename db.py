# coding=utf-8
import redis
import random
from config import *


class RedisClient(object):
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, proxy_key=PROXY_KEY):
        """
        初始化Redis连接
        :param host: Redis 地址
        :param port: Redis 端口
        :param password: Redis 密码
        :param proxy_key: Redis 哈希表名
        """
        self.db = redis.StrictRedis(host=host, port=port, password=password, decode_responses=True)
        self.proxy_key = proxy_key

    def set(self, name, proxy):
        """
        设置代理
        :param name: 主机名称
        :param proxy: 代理
        :return: 设置结果
        """
        return self.db.hset(self.proxy_key, name, proxy)

    def get(self, name):
        """
        获取代理
        :param name: 主机名称
        :return: 代理
        """
        return self.db.hget(self.proxy_key, name)

    def count(self):
        """
        获取代理总数
        :return: 代理总数
        """
        return self.db.hlen(self.proxy_key)

    def exists(self, name):
        """
        判断代理是否存在
        :param name: 主机名称
        :return: True or False
        """
        return self.db.hexists(self.proxy_key, name)

    def remove(self, name):
        """
        删除代理
        :param name: 主机名称
        :return: 删除结果
        """
        return self.db.hdel(self.proxy_key, name)

    def names(self):
        """
        获取主机名称列表
        :return: 获取主机名称列表
        """
        return self.db.hkeys(self.proxy_key)

    def proxies(self):
        """
        获取代理列表
        :return: 代理列表
        """
        return self.db.hvals(self.proxy_key)

    def random(self):
        """
        随机获取代理
        :return:
        """
        proxies = self.proxies()
        if len(proxies):
            return random.choice(proxies)

    def all(self):
        """
        获取字典
        :return:
        """
        return self.db.hgetall(self.proxy_key)


if __name__ == '__main__':
    r = RedisClient()
    # a = r.set('adsl2', '192:11111')
    # print(a)
    # r.set('adsl2', '192:22222')
    # r.set('adsl3', '192:33333')
    # r.remove('adsl2')
    # print('get: ', r.get('adsl1'))
    # print('count: ', r.count())
    # print('random: ', r.random())
    # print('all: ', r.all())
    # print('name: ', r.names())
    # print('get: ', r.get('adsl2'))
    # print('exists: ', r.exists('adsl2'))
    # print('exists: ', r.exists('adsl1'))
    # print('proxies: ', r.proxies())
    # if r.exists('adsl3'):
    #     r.remove('删除成功')
    #     print('删除成功')
    proxy = '192:112222'
    a = r.set(CLIENT_NAME, proxy)
    if a:
        print('Successfully Set Proxy', proxy)


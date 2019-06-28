"""服务端配置"""
# Redis数据库IP
REDIS_HOST = '47.102.147.138'

# Redis数据库密码, 如无则填None
REDIS_PASSWORD = 'noodles'

# Redis数据库端口
REDIS_PORT = 6379

# 通信秘钥
TOKEN = 'noodles'

# 接收器运行端口
API_PORT = 8000

# 服务器地址
SERVER_URL = 'http://47.102.147.138:8000'


"""客户端配置"""

# 代理池键名
PROXY_KEY = 'adsl'

# 拨号网卡
ADSL_IFNAME = 'ppp0'

# 拨号命令
ADSL_BASH = 'adsl-stop;adsl-start'

# 拨号间隔
ADSL_CYCLE = 100

# 通信秘钥
TOKEN = 'noodles'

# 代理端口
PROXY_PORT = 3127

# 客户端唯一标识
CLIENT_NAME = 'adsl1'

# 拨号出错重试间隔
ADSL_ERROR_CYCLE = 8

# 验证URL
TEST_URL = 'http://www.baidu.com'

# 测试超时时间
TEST_TIMEOUT = 10

# 代理账号
PROXY_USER = 'd88'

# 代理密码
PROXY_PASSWORD = 'd88'

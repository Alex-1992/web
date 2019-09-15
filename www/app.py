from aiohttp import web
import asyncio
import logging
import kill_process
import handlers
import orm
logging.basicConfig(level=logging.INFO)

# 定义服务器响应请求的的返回为 "Awesome Website"


async def index(request):
    return web.Response(body=b'<h1>Awesome Website</h1>', content_type='text/html')

# 建立服务器应用，持续监听本地9000端口的http请求，对首页"/"进行响应


async def test(loop):
    await orm.create_pool(loop=loop, user='root', password='youyangfan', db='awesome')


def init():
    app = web.Application()
    app.router.add_get('/', handlers.index)
    # kill_process.killport(9000)
    try:
        web.run_app(app, host='127.0.0.1', port=9000)
    except OSError:
        kill_process.killport(9000)
        web.run_app(app, host='127.0.0.1', port=9000)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(test(loop))
    finally:
        loop.close()

    init()

    # u = User(name='yyf', email='1952889796@qq.com',
    #          passwd='1234567890', image='about:blank')
    # await u.save()
    # # 网友指出添加到数据库后需要关闭连接池，否则会报错 RuntimeError: Event loop is closed
    # orm.__pool.close()
    # await orm.__pool.wait_closed()
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(test(loop))
#     loop.close()

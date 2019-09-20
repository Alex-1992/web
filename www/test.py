import orm
import asyncio
from models import User, Blog, Comment


async def test(loop):
    await orm.create_pool(loop=loop, user='root', password='youyangfan', db='awesome')
    u = User(name='yyf', email='1952889796@qq.com',
             passwd='1234567890', image='about:blank')
    await u.save()
    # 网友指出添加到数据库后需要关闭连接池，否则会报错 RuntimeError: Event loop is closed
    orm.__pool.close()
    await orm.__pool.wait_closed()
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()
# "C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql" - uroot - pyouyangfan < C:\Users\Administrator\Desktop\awsome\schema.sql
# "C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql" - u root - p < C: \Users\Administrator\Desktop\awsome\schema.sql
# "C:\Program Files\MySQL\MySQL Server 8.0\bin"

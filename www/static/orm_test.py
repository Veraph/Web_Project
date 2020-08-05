#!usr/bin/env python3
# -*- coding: utf-8 -*-

'Test to add and get data from Mysql'

import orm, asyncio
from models import User, Blog, Comment

loop = asyncio.get_event_loop()
async def test():
    await orm.create_pool(user='www-data', password='www-data', db='test1', loop=loop)

    u = User(name='Test', email='text1@example.com', passwd='12345', image='about:blank')

    await u.save()

loop.run_until_complete(test())
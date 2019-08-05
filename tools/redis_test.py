# -*- coding:utf-8 -*-
# author:h
# datetime:2019-07-31 22:16

import redis

r = redis.Redis(host='localhost', port=6379, db=0, charset='utf8', decode_responses=True)

r.set('foo', 'bar')
# r.expire('foo', 1)

# import time
#
# time.sleep(1)
print(r.get('foo'))

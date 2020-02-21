# conda install -c anaconda redis-py
# https://github.com/andymccurdy/redis-py
# https://seanmcgary.com/posts/how-to-build-a-fault-tolerant-redis-cluster-with-sentinel/

import redis
from redis.sentinel import Sentinel

# r = redis.Redis(host='10.10.0.30', port=6381, password='wsiz#1234')


sentinel = Sentinel([('10.10.0.30', 16380),
                     ('10.10.0.30', 16381),
                     ('10.10.0.30', 16382)], socket_timeout=0.1, password='wsiz#1234')
r = sentinel.master_for('rrr')



r.set('s213', '121')
print(r.get('s213'))

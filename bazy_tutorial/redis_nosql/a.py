# conda install -c anaconda redis-py
# https://github.com/andymccurdy/redis-py
# https://seanmcgary.com/posts/how-to-build-a-fault-tolerant-redis-cluster-with-sentinel/

import redis
from redis.sentinel import Sentinel

# r = redis.Redis(host='10.10.0.30', port=6381, password='wsiz#1234')


sentinel = Sentinel([('10.10.0.30', 16380),
                     ('10.10.0.30', 16381),
                     ('10.10.0.30', 16382)], socket_timeout=0.1,
                    decode_responses=True,  # else: binary arrays as keys/fields
                    password='wsiz#1234')
r = sentinel.master_for('rrr')

r.set('s213', '121')
print(r.get('s213'))

r.hset('s111', 'name', 'Sofia')
res = r.hgetall('s111')
print(res['name'])

# Few examples:
# --- Sets:
# SADD aa 12
# SADD aa 11
# SMEMBERS aa
# SREM aa 11
# SINTER aa bb          #set intersection
#
# --- HashSet with fields:
# HSET key field val
# HGET key field
# HSET user12 pesel PL112233
# HGETALL key   # field1,val1,field2,val2,...
# KDEL key field
#
#
#

import dis

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return 3
        print('[CONSUMER]Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    test = c.send(None)
    print(test)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER]Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER]Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)
# dis.dis(produce)
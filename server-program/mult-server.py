import sys
import socket
import selectors
import types

sel = selectors.DefaultSelector()


def accept_wrapper(sock):
    conn, addr = sock.accept()  # Should be ready to read
    print("accepted connection from", addr)
    # 调用 sock.accept() 后立即再立即调 conn.setblocking(False) 来让 socket 进入非阻塞模式
    conn.setblocking(False)
    # 使用了 types.SimpleNamespace 类创建了一个对象用来保存我们想要的 socket 和数据
    data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)

def service_connection(key, mask):
    # key 包含了 socket 对象「fileobj」和数据对象；
    sock = key.fileobj
    data = key.data
    # mask 包含了就绪的事件
    if mask & selectors.EVENT_READ:
        '''
        如果 socket 就绪而且可以被读取，mask & selectors.EVENT_READ 就为真，sock.recv() 会被调用。
        所有读取到的数据都会被追加到 data.outb 里面
        '''
        recv_data = sock.recv(1024)  # Should be ready to read
        if recv_data:
            data.outb += recv_data
        else:
            print("closing connection to", data.addr)
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print("echoing", repr(data.outb), "to", data.addr)
            # 任何接收并被 data.outb 存储的数据都将使用 sock.send() 方法打印出来
            sent = sock.send(data.outb) 
            data.outb = data.outb[sent:]


if len(sys.argv) != 3:
    print("usage:", sys.argv[0], "<host> <port>")
    sys.exit(1)

host, port = sys.argv[1], int(sys.argv[2])
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((host, port))
lsock.listen()
print("listening on", (host, port))
lsock.setblocking(False)    # 配置 socket 为非阻塞模式
# data 来跟踪 socket 上发送或者接收的东西
sel.register(lsock, selectors.EVENT_READ, data=None)

try:
    while True:
        # 事件循环，不断请求 socket 状态，并调用对应的回调函数
        events = sel.select(timeout=None)   # 阻塞直到 socket I/O 就绪
        """
        sel.select(timeout=None)返回一个(key, events) 元组；
        key 包含了 socket 对象「fileobj」和数据对象；
        mask 包含了就绪的事件
        """
        for key, mask in events:
            # 新的客户端， 利用accept_wrapper()来接受新的 socket 对象并注册到 selector 上
            if key.data is None:
                accept_wrapper(key.fileobj) #key.fileobj=socket对象
            # 如果 key.data 不为空，旧的被接受的客户端，我们需要为它服务，接着 service_connection() 会传入 key 和 mask 参数并调用
            else:
                service_connection(key, mask)
except KeyboardInterrupt:
    print("caught keyboard interrupt, exiting")
finally:
    sel.close()
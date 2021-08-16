# Socket Programming in Python
Sockets and the socket API are used to send messages across a network. They provide a form of [inter-process communication (IPC)](https://en.wikipedia.org/wiki/Inter-process_communication). The network can be a logical, local network to the computer, or one that’s physically connected to an external network, with its own connections to other networks. The obvious example is the Internet, which you connect to via your ISP.

The server forms the listener socket while the client reaches out to the server.  
They are the real backbones behind web browsing. In simpler terms, there is a server and a client.  
Socket programming is started by importing the socket library and making a simple socket.

    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Here we made a socket instance and passed it two parameters. The first parameter is  **AF_INET**  and the second one is  **SOCK_STREAM**. AF_INET refers to the address-family ipv4. The SOCK_STREAM means connection-oriented TCP protocol.  
Now we can connect to a server using this socket.3

## Socket API Overview[](https://realpython.com/python-sockets/#socket-api-overview "Permanent link")

Python’s  [socket module](https://docs.python.org/3/library/socket.html)  provides an interface to the  [Berkeley sockets API](https://en.wikipedia.org/wiki/Berkeley_sockets). This is the module that we’ll use and discuss in this tutorial.

The primary socket API functions and methods in this module are:

-   `socket()`
-   `bind()`
-   `listen()`
-   `accept()`
-   `connect()`
-   `connect_ex()`
-   `send()`
-   `recv()`
-   `close()`

Python provides a convenient and consistent API that maps directly to these system calls, their C counterparts. We’ll look at how these are used together in the next section.

As part of its standard library, Python also has classes that make using these low-level socket functions easier. Although it’s not covered in this tutorial, see the  [socketserver module](https://docs.python.org/3/library/socketserver.html), a framework for network servers. There are also many modules available that implement higher-level Internet protocols like HTTP and SMTP. For an overview, see  [Internet Protocols and Support](https://docs.python.org/3/library/internet.html).

## TCP Sockets[](https://realpython.com/python-sockets/#tcp-sockets "Permanent link")

As you’ll see shortly, we’ll create a socket object using  `socket.socket()`  and specify the socket type as  `socket.SOCK_STREAM`. When you do that, the default protocol that’s used is the  [Transmission Control Protocol (TCP)](https://en.wikipedia.org/wiki/Transmission_Control_Protocol). This is a good default and probably what you want.

Why should you use TCP? The Transmission Control Protocol (TCP):

-   **Is reliable:**  packets dropped in the network are detected and retransmitted by the sender.
-   **Has in-order data delivery:**  data is read by your application in the order it was written by the sender.

In contrast,  [User Datagram Protocol (UDP)](https://en.wikipedia.org/wiki/User_Datagram_Protocol)  sockets created with  `socket.SOCK_DGRAM`  aren’t reliable, and data read by the receiver can be out-of-order from the sender’s writes.

Why is this important? Networks are a best-effort delivery system. There’s no guarantee that your data will reach its destination or that you’ll receive what’s been sent to you.

Network devices (for example, routers and switches), have finite bandwidth available and their own inherent system limitations. They have CPUs, memory, buses, and interface packet buffers, just like our clients and servers. TCP relieves you from having to worry about  [packet loss](https://en.wikipedia.org/wiki/Packet_loss), data arriving out-of-order, and many other things that invariably happen when you’re communicating across a network.
Starting in the top left-hand column, note the API calls the server makes to setup a “listening” socket:

-   `socket()`
-   `bind()`
-   `listen()`
-   `accept()`

A listening socket does just what it sounds like. It listens for connections from clients. When a client connects, the server calls  `accept()`  to accept, or complete, the connection.

The client calls  `connect()`  to establish a connection to the server and initiate the three-way handshake. The handshake step is important since it ensures that each side of the connection is reachable in the network, in other words that the client can reach the server and vice-versa. It may be that only one host, client or server, can reach the other.

In the middle is the round-trip section, where data is exchanged between the client and server using calls to  `send()`  and  `recv()`.

At the bottom, the client and server  `close()`  their respective sockets.


## Why Use Sockets to Send Data?

Internet-connected applications that need to operate in real time greatly benefit from the implementation of  **sockets**  in their  **networking code**. Some examples of apps that use socket programming are:

-   Web pages that show  [live notifications](https://www.pubnub.com/use-case/alerts-and-push-notifications/)  (Facebook, Twitch, eBay)
-   [Multiplayer online games](https://www.pubnub.com/industry/gaming/)  (League of Legends, WoW, Counter Strike)
-   [Chat apps](https://www.pubnub.com/use-case/in-app-chat/)  (WhatsApp, WeChat, Slack)
-   [Real-time data dashboards](https://www.pubnub.com/use-case/data-broadcasting-and-dashboards/)  (Robinhood, Coinbase)
-   [IoT devices](https://www.pubnub.com/use-case/iot-device-control/)  (Nest, August Locks)

Python, unlike JavaScript, is a language that executes  [synchronously](https://hackernoon.com/javascript-promises-and-why-async-await-wins-the-battle-4fc9d15d509f). This is why  **asyncio**  was developed – to make Python more robust, particularly for the nature of socket programming.

With streaming sockets, data can be sent or received at any time. In case your Python program is in the middle of executing some code, other **threads**  can handle the new socket data. Libraries like  [asyncio](https://docs.python.org/3/library/asyncio.html)  implement multiple threads, so your Python program can work in an asynchronous fashion.
# [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.")  — Python object serialization

The [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.") module implements binary protocols for serializing and de-serializing a Python object structure. _“Pickling”_ is the process whereby a Python object hierarchy is converted into a byte stream, and _“unpickling”_ is the inverse operation, whereby a byte stream (from a [binary file](https://docs.python.org/3/glossary.html#term-binary-file) or [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)) is converted back into an object hierarchy. Pickling (and unpickling) is alternatively known as “serialization”, “marshalling,” [1](https://docs.python.org/3/library/pickle.html#id7) or “flattening”; however, to avoid confusion, the terms used here are “pickling” and “unpickling”.

Python pickle module is used for serializing and de-serializing a Python object structure. Any object in Python can be pickled so that it can be saved on disk. What pickle does is that it “serializes” the object first before writing it to file. Pickling is a way to convert a python object (list, dict, etc.) into a character stream. The idea is that this character stream contains all the information necessary to reconstruct the object in another python script.


**Advantages of using Pickle Module:**  
  

1.  **Recursive objects (objects containing references to themselves):**  Pickle keeps track of the objects it has already serialized, so later references to the same object won’t be serialized again. (The marshal module breaks for this.)
2.  **Object sharing (references to the same object in different places):**  This is similar to self- referencing objects; pickle stores the object once, and ensures that all other references point to the master copy. Shared objects remain shared, which can be very important for mutable objects.
3.  **User-defined classes and their instances:**  Marshal does not support these at all, but pickle can save and restore class instances transparently. The class definition must be importable and live in the same module as when the object was stored.



# select – Wait for I/O Efficiently
The  [select](https://pymotw.com/2/select/#module-select "select: Wait for I/O Efficiently")  module provides access to platform-specific I/O monitoring functions. 

All socket methods are blocking. For example, when it reads from a socket or writes to it the program can't do anything else. One possible solution is to delegate working with clients to separate threads. However, creating threads and switching contexts between them is not really a cheap operation. To address this problem, there is a so-called asynchronous way of working with sockets. The main idea is to delegate maintaining the socket's state to an operating system and letting it notify the program when there is something to read from the socket or when it is ready for writing.

There are a bunch of interfaces for different operating systems:

-   poll, epoll (linux)
-   kqueue, kevent (BSD)
-   select (crossplatform)


## select()[](https://pymotw.com/2/select/#select "Permalink to this headline")

we call `select.select` to ask the OS to check given sockets whether they are ready to write, read, or if there is some exception respectively. That is why it passes three lists of sockets to specify which socket is expected to be writable, readable, and which should be checked for errors. This call will block the program (unless a timeout argument is passed) until some of the passed sockets are ready. In this moment, the call will return three lists with sockets for specified operations.

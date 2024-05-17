import threading
import queue
import time
import random

# Shared Queue
BUFFER_SIZE = 5
queue_buffer = queue.Queue(BUFFER_SIZE)

# Monitor for the buffer
class Monitor:
    def __init__(self):
        self.mutex = threading.Condition()

    def acquire(self):
        self.mutex.acquire()

    def release(self):
        self.mutex.notify()
        self.mutex.release()

    def wait(self):
        self.mutex.wait()

monitor = Monitor()

# Producer function
def producer():
    for _ in range(10):
        item = random.randint(1, 100)
        monitor.acquire()
        while queue_buffer.full():
            monitor.wait()
        queue_buffer.put(item)
        print(f"Produced item {item}. Queue size: {queue_buffer.qsize()}")
        monitor.release()
        time.sleep(random.random())  # Simulating some processing time

# Consumer function
def consumer():
    for _ in range(10):
        monitor.acquire()
        while queue_buffer.empty():
            monitor.wait()
        item = queue_buffer.get()
        print(f"Consumed item {item}. Queue size: {queue_buffer.qsize()}")
        monitor.release()
        time.sleep(random.random())  # Simulating some processing time

# Creating producer and consumer threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# Starting threads
producer_thread.start()
consumer_thread.start()

# Joining threads to main thread
producer_thread.join()
consumer_thread.join()

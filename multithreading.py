from threading import Thread
import time


class Hello:
    # Function to simulate a time-consuming task
    def hello(self):
        for i in range(5):
            print('Hello')
            time.sleep(1)


class Hi:
    # Function to simulate a time-consuming task
    def hi(self):
        for i in range(5):
            print('Hi')
            time.sleep(1)


he = Hello()
hi = Hi()

# Create two threads 
# Pass the function references without parentheses to Thread

t1 = Thread(target=he.hello)
t2 = Thread(target=hi.hi)

# Start the threads
t1.start()
time.sleep(0.2)
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()

print('All the threads have been completed')

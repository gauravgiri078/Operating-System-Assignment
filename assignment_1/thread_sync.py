import threading
import time

# Shared resource
counter = 0

# Lock (Mutex)
lock = threading.Lock()

# Function executed by threads
def increment_counter(thread_name):
    global counter

    for i in range(5):
        lock.acquire()          # Lock before critical section
        temp = counter
        time.sleep(0.5)         # Simulate processing delay
        counter = temp + 1
        print(f"{thread_name} updated counter to {counter}")
        lock.release()          # Unlock after critical section

# Create threads
thread1 = threading.Thread(target=increment_counter, args=("Thread-1",))
thread2 = threading.Thread(target=increment_counter, args=("Thread-2",))

print("Starting threads...\n")

# Start threads
thread1.start()
thread2.start()

# Wait for threads to finish
thread1.join()
thread2.join()

print("\nFinal Counter Value:", counter)
print("Main thread exiting")

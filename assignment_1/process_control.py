import os
import sys

print("Parent Process Started")
print(f"Parent PID: {os.getpid()}")

# Fork the process
pid = os.fork()

if pid == 0:
    # Child process
    print("\nChild Process")
    print(f"Child PID: {os.getpid()}")
    print(f"Parent PID (from child): {os.getppid()}")

    print("\nChild is executing a new program (ls command)...")
    
    # Replace child process with 'ls' command
    os.execlp("ls", "ls")

    # This line will not execute if exec is successful
    print("This will not be printed")

else:
    # Parent process
    print("\nParent is waiting for child to finish...")
    
    # Wait for child process to complete
    finished_pid, status = os.wait()

    print(f"\nChild process {finished_pid} finished execution")
    print("Parent Process Ended")

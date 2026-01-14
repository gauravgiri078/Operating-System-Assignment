# Operating Systems and Security – Assignment 1

**Student Name:** Gaurav Giri  
**Module Name:** Operating Systems and Security  
**Module Code:** ST5004CEM  
**Assignment Title:** Individual Coursework – OS-Level Practical Portfolio  
**Assignment Due:** 22nd January 2026 [11:55 PM]  

---

## Overview

This portfolio demonstrates practical examples of **core Operating System concepts**. The following OS-level functionalities are implemented using Python:

1. **Process Control** – creating, forking, executing, and waiting for processes  
2. **File Management** – creating, reading, writing, and deleting files  
3. **Threading and Synchronization** – creating threads and using locks/mutexes  
4. **Memory Management** – simulating allocation, paging, and fragmentation  
5. **Device Access** – listing mounted devices and reading system I/O  

---

---

## File Descriptions

### 1. `process_control.py`
- Demonstrates **process creation, execution, and termination**
- Uses Python’s `os` and `subprocess` modules to fork and run processes
- Example: create a child process, execute a command, and wait for completion

### 2. `filemanagement.py`
- Demonstrates **file operations** in Python
- Includes creating, reading, writing, and deleting files
- Example: open a file, write data, read contents, and remove file safely

### 3. `thread_sync.py`
- Demonstrates **thread creation and synchronization**
- Uses Python’s `threading` module and `Lock` objects
- Example: multiple threads incrementing a shared variable safely

### 4. `memory_management.py`
- Simulates **memory allocation and fragmentation**
- Implements simple memory blocks and paging concepts
- Example: allocate memory for processes, simulate paging, and deallocation

### 5. `device_acess.py`
- Demonstrates **device-level access**
- Reads system information and lists mounted devices
- Example: list all mounted drives, read system I/O files like `/proc` or `/sys`

---

## How to Run

1. Activate virtual environment:
```bash
source venv/bin/activate


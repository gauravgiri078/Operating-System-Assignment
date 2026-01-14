import os

print("DEVICE ACCESS DEMONSTRATION\n")

# 1. List mounted devices
print("1. LIST OF MOUNTED DEVICES:\n")

with open("/proc/mounts", "r") as mounts:
    for line in mounts.readlines()[:5]:  # show first 5 for clarity
        parts = line.split()
        device = parts[0]
        mount_point = parts[1]
        fs_type = parts[2]
        print(f"Device: {device} | Mounted on: {mount_point} | Type: {fs_type}")

# 2. Read disk I/O statistics
print("\n2. DISK I/O STATISTICS:\n")

with open("/proc/diskstats", "r") as diskstats:
    for line in diskstats.readlines()[:3]:  # show first 3 entries
        parts = line.split()
        device_name = parts[2]
        reads = parts[3]
        writes = parts[7]
        print(f"Device: {device_name} | Reads: {reads} | Writes: {writes}")

# 3. Access input/output device directory
print("\n3. LISTING /dev DIRECTORY (First 10 entries):\n")

devices = os.listdir("/dev")
for dev in devices[:10]:
    print(dev)

print("\nDevice Access Demonstration Completed")

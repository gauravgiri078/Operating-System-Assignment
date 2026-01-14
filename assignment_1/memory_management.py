import math

# Total memory and block size
TOTAL_MEMORY = 256      # in KB
BLOCK_SIZE = 32         # in KB

# Create memory blocks
memory_blocks = [BLOCK_SIZE] * (TOTAL_MEMORY // BLOCK_SIZE)

print("MEMORY MANAGEMENT SIMULATION\n")
print(f"Total Memory: {TOTAL_MEMORY} KB")
print(f"Block Size: {BLOCK_SIZE} KB")
print(f"Total Blocks: {len(memory_blocks)}\n")

# Process memory requirements (in KB)
processes = {
    "P1": 20,
    "P2": 45,
    "P3": 60,
    "P4": 30
}

allocated = {}
internal_fragmentation = 0

# 1. Fixed Partition Allocation (First Fit)
print("1. MEMORY ALLOCATION (Fixed Partition - First Fit)\n")

for process, size in processes.items():
    for i in range(len(memory_blocks)):
        if memory_blocks[i] >= size:
            allocated[process] = i
            internal_fragmentation += memory_blocks[i] - size
            memory_blocks[i] = 0
            print(f"{process} allocated to Block {i} (Process size: {size} KB)")
            break
    else:
        print(f"{process} could not be allocated")

print(f"\nTotal Internal Fragmentation: {internal_fragmentation} KB\n")

# 2. Paging Simulation
print("2. PAGING SIMULATION\n")

PAGE_SIZE = 16  # KB

for process, size in processes.items():
    pages = math.ceil(size / PAGE_SIZE)
    print(f"{process} requires {pages} pages")

print("\nPaging avoids external fragmentation\n")

# 3. External Fragmentation Simulation
print("3. EXTERNAL FRAGMENTATION SIMULATION\n")

free_blocks = memory_blocks.count(BLOCK_SIZE)
external_fragmentation = free_blocks * BLOCK_SIZE

print(f"Free Blocks: {free_blocks}")
print(f"Total Free Memory: {external_fragmentation} KB")

print("\nSimulation Completed")

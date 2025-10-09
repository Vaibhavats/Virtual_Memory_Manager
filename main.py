from memory_manager import Memory
from process_manager import Process

def main():
    memory_size = 8
    frame_size = 1
    memory = Memory(memory_size, frame_size)

    print("=== Virtual Memory Management Simulation ===")
    print(f"Total Memory Frames: {memory_size}")
    print(f"Frame Size: {frame_size}\n")

    # Create multiple processes
    processes = [
        Process(pid=1, num_pages=3),
        Process(pid=2, num_pages=4),
        Process(pid=3, num_pages=3),
    ]

    # Load each process into memory
    for p in processes:
        print(f"Allocating memory for Process {p.pid}...")
        p.load_into_memory(memory)
        print(p)
        print()

    # Display current memory status
    memory.display()

if __name__ == "__main__":
    main()

# cli.py
from memory_manager import Memory
from process_manager import Process

class CLI:
    def __init__(self):
        print("=== Virtual Memory Manager CLI ===")
        total_frames = int(input("Enter total frames: "))
        frame_size = int(input("Enter frame size: "))
        policy = input("Choose replacement policy (FIFO/LRU): ").upper()

        self.memory = Memory(total_frames, frame_size, replacement_policy=policy)
        self.processes = {}

    def run(self):
        while True:
            try:
                command = input(">>> ").strip().split()
                if not command:
                    continue

                cmd = command[0].lower()

                if cmd == "load":
                    self.load_process(command) 
                elif cmd == "access":
                    self.access_page(command)
                elif cmd == "frames":
                    self.show_frames()
                elif cmd == "stats":
                    self.show_stats()
                elif cmd == "exit":
                    print("Exiting...")
                    break
                else:
                    print("Unknown command. Try: load, access, frames, stats, exit")

            except Exception as e:
                print("Error:", e)

    def load_process(self, command):
        if len(command) != 3:
            print("Usage: load <pid> <num_pages>")
            return
        pid = int(command[1])
        num_pages = int(command[2])
        if pid in self.processes:
            print(f"Process {pid} already exists.")
            return
        process = Process(pid=pid, num_pages=num_pages)
        self.processes[pid] = process
        print(f"Loaded process {pid} with {num_pages} pages.")
        # allocate first page
        for i in range(num_pages):
            self.memory.allocate_page(pid, i)
        print("Frames:", self.memory.frames)

    def access_page(self, command):
        if len(command) != 3:
            print("Usage: access <pid> <page_number>")
            return
        pid = int(command[1])
        page = int(command[2])
        if pid not in self.processes:
            print(f"Process {pid} not found.")
            return
        hit = self.memory.access_page(pid, page)
        if hit:
            print(f"Page ({pid}, {page}) HIT")
        else:
            print(f"Page ({pid}, {page}) FAULT")
        self.show_frames()

    def show_frames(self):
        print("Frames:", self.memory.frames)

    def show_stats(self):
        stats = self.memory.stats()
        print("=== Stats ===")
        for k, v in stats.items():
            print(f"{k}: {v}")

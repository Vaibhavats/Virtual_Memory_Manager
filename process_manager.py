# process.py
class Process:
    def __init__(self, pid, num_pages):
        self.pid = pid
        self.num_pages = num_pages
        self.page_table = [-1] * num_pages  # -1 = not in memory

    def load_into_memory(self, memory):
        """Try to allocate frames for each page of this process."""
        for page_no in range(self.num_pages):
            frame = memory.allocate_page(self.pid, page_no)
            if frame != -1:
                self.page_table[page_no] = frame
            else:
                # no free frame — page stays -1
                print(f"⚠️ No free frame for P{self.pid} page {page_no}")

    def __repr__(self):
        return f"<Process {self.pid} pages={self.num_pages} page_table={self.page_table}>"

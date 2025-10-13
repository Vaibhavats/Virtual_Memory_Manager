# memory_manager.py
from replacement import FIFOReplacement, LRUReplacement

class Memory:
    def __init__(self, total_frames, frame_size, replacement_policy="FIFO"):
        self.total_frames = total_frames
        self.frame_size = frame_size
        self.frames = [None] * total_frames
        self.page_table = {}
        self.free_frames = list(range(total_frames))
        self.page_faults = 0
        self.page_hits = 0

        if replacement_policy == "LRU":
            self.replacement = LRUReplacement()
        else:
            self.replacement = FIFOReplacement()

    def allocate_page(self, pid, page):
        # Page already in memory → no fault
        if (pid, page) in self.frames:
            self.page_hits += 1
            self.replacement.access_page((pid, page))
            return

        # PAGE FAULT
        self.page_faults += 1

        # If free frame → allocate
        if self.free_frames:
            frame = self.free_frames.pop(0)
            self.frames[frame] = (pid, page)
            self.page_table.setdefault(pid, set()).add(page)
            self.replacement.add_page((pid, page))
        else:
            # Evict
            victim = self.replacement.evict_page()
            victim_frame = self.find_frame(victim)
            self.frames[victim_frame] = (pid, page)
            self.page_table[victim[0]].remove(victim[1])
            self.page_table.setdefault(pid, set()).add(page)
            self.replacement.add_page((pid, page))

    def access_page(self, pid, page):
        if (pid, page) in self.frames:
            self.page_hits += 1
            self.replacement.access_page((pid, page))
            return True
        else:
            self.allocate_page(pid, page)
            return False

    def find_frame(self, page_tuple):
        for i, content in enumerate(self.frames):
            if content == page_tuple:
                return i
        return -1

    def stats(self):
        total = self.page_faults + self.page_hits
        hit_ratio = self.page_hits / total if total else 0
        fault_ratio = self.page_faults / total if total else 0
        return {
            "Page Faults": self.page_faults,
            "Page Hits": self.page_hits,
            "Hit Ratio": round(hit_ratio, 2),
            "Fault Ratio": round(fault_ratio, 2)
        }

# memory_manager.py
class Memory:
    def __init__(self, total_frames, frame_size):
        self.total_frames = total_frames
        self.frame_size = frame_size
        self.frames = [None] * total_frames  # (pid, page_no) or None

    def allocate_page(self, pid, page_no):
        """Find a free frame and allocate it to the given process page."""
        for i in range(self.total_frames):
            if self.frames[i] is None:
                self.frames[i] = (pid, page_no)
                return i  # return allocated frame index
        return -1  # no free frame

    def free_frame(self, frame_no):
        """Free a specific frame."""
        self.frames[frame_no] = None

    def display(self):
        """For debugging: show current memory state."""
        print("Memory Frames:")
        for i, frame in enumerate(self.frames):
            print(f"  Frame {i}: {frame}")

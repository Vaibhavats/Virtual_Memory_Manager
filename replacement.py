# replacement.py
from collections import deque, OrderedDict

class FIFOReplacement:
    def __init__(self):
        self.queue = deque()

    def access_page(self, page):
        # FIFO doesn’t need to do anything on access (no reordering)
        pass

    def evict_page(self):
        # Pop oldest page
        return self.queue.popleft()

    def add_page(self, page):
        self.queue.append(page)

class LRUReplacement:
    def __init__(self):
        self.pages = OrderedDict()

    def access_page(self, page):
        if page in self.pages:
            self.pages.move_to_end(page)  # mark page as recently used

    def evict_page(self):
        page, _ = self.pages.popitem(last=False)  # remove least recently used
        return page

    def add_page(self, page):
        self.pages[page] = True
        self.pages.move_to_end(page)

class MyCalendar:

    def __init__(self):
        self.events = deque()
        
    def book(self, start: int, end: int) -> bool:
        if len(self.events) == 0:
            self.events.append((start, end))
            return True
            
        idx = bisect.bisect_left(self.events, (start, end))
        
        # Event interval is biggest
        if idx == len(self.events):
            if self.events[idx-1][1] <= start:
                bisect.insort_left(self.events, (start, end))
                return True
            return False
        
        # Event interval is smalest
        if idx == 0:
            if self.events[0][0] >= end:
                bisect.insort_left(self.events, (start, end))
                return True
            return False
        
        
        if end <= self.events[idx][0] and start >= self.events[idx-1][1]:
            bisect.insort_left(self.events, (start, end))
            return True
        
        return False
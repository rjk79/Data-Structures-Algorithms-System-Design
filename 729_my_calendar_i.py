class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        if not self.events: 
            self.events.append([start, end])
            return True
        starts = [event[0] for event in self.events]
        idx = bisect.bisect(starts, start)
        self.events.insert(idx, [start, end])
        for i in range(0, len(self.events) -1):
            if self.events[i][1] > self.events[i + 1][0]: 
                self.events.pop(idx)
                return False
        return True

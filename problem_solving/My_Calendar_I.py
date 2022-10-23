from copy import copy


class MyCalendar:

    def __init__(self):
        self.res=[]
        self.dic={}
    def book(self, start: int, end: int) -> bool:

        if not start or not end : 
            return []
        if not self.dic and start and end :
            self.res.append(True)
            self.dic[start]=end
        if start not in self.dic.keys() or end not in self.dic.values():
            for s, e in self.dic.copy().items():
                r=range(s+1,e+1)
                if start+1 in r or end in r:
                    self.res.append(False)
                else:
                    self.res.append(True)
                    self.dic[start]=end
        return self.res
            
            
        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
myCalendar = MyCalendar()
myCalendar.book(10, 20) # return True
myCalendar.book(15, 25) # return False, It can not be booked because time 15 is already booked by another event.
print(myCalendar.book(20, 30)) # return True, The event can be booked, as the first event takes every time less than 20, but not including 20.

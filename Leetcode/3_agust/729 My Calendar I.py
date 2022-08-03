# class MyCalendar:

#     def __init__(self):
#         self.cal = set()
#         self.caltemp = set()

#     def book(self, start: int, end: int) -> bool:
#         for n in range(start,end):
#             # print(f"start is {start} end is {end} n is {n}")
#             if n in self.cal:
#                 self.caltemp = set()
#                 return False
#             else :
#                 self.caltemp.add(n)
#         else:
#             self.cal.update(self.caltemp)
#             self.caltemp = set()
#             return True


# # Your MyCalendar object will be instantiated and called as such:
# # obj = MyCalendar()
# # param_1 = obj.book(start,end)

# # 95 / 107 test cases passed.
# # 	Status: Memory Limit Exceeded



class MyCalendar:

    def __init__(self):
        self.starts = []
        self.cal = {}

    def where_to_insert(self, a):
        sind = 0
        eind = len(self.starts) - 1 
        if a < self.starts[sind]:
            return "first"
        elif a > self.starts[eind]:
            return "last"
        else:
            while sind != eind -1 :
                mid = (sind+eind)//2
                if self.starts[mid] < a:
                    sind = mid
                else :
                    eind = mid
            return sind

    def add_to(self,start,end):
        self.starts.append(start)
        self.cal.update({start:end})
        # print(self.cal, self.starts, end)
        self.starts.sort()
        return True


    def book(self, start: int, end: int) -> bool:
        e = len(self.starts)
        if e > 1:
            s = self.starts[0]
            ind = self.where_to_insert(start) 

            if ind == "first":
                if end <= self.starts[0]:
                    return self.add_to(start, end)
                else :
                    return False

            elif ind == "last":
                if start >= self.cal[self.starts[e-1]]:
                    return self.add_to(start, end)

                else:
                    return False
            else:
                if self.cal[self.starts[ind]] <= start and end <= self.starts[ind+1]:
                    return self.add_to(start, end)
                else:
                    return False

        elif e == 1 :
            s = self.starts[0]
            if start > s:
                if self.cal[s] <= start:
                    return self.add_to(start, end)

                else:
                    return False 
                
            elif start < s :
                if end <= s:
                    return self.add_to(start, end)

                else:
                    return False

        elif e == 0:
            return self.add_to(start, end)


Runtime: 441 ms, faster than 53.55% of Python3 online submissions for My Calendar I.
Memory Usage: 14.8 MB, less than 58.88% of Python3 online submissions for My Calendar I.
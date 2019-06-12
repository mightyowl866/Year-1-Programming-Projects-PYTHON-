class Stack:
    def __init__(self):
         self.items = []
    def Clear(self):
        self.items.clear()
    def Clone(self):
        new_stack = self.items.copy()
        return new_stack
    def Contains(self,other):
        for i in self.items:
            if i in self.items:
                return True
            else:
                return False
    def __eq__(self,other):
        if self.items == other:
            return True
        else:
            return False
    def __iter__(self):
        for i in self.items:
            print(i)
    def Peek(self):
        return self.items[len(self.items)-1]
    def Pop(self):
        return self.items.pop()
    def Push(self,object):
        self.items.append(object)
    def __str__(self):
        return str(self.items)





#_________________________________________________________




class Queue:
    def __init__(self):
        self.queue = []
    def Clear(self):
        self.queue.clear()
    def Clone(self):
        new_queue = self.queue.copy()
        return new_queue
    def Contains(self,other):
        for item in self.queue:
            if item in other:
                return True
            else:
                return False
    def Dequeue(self):
        return self.queue.pop()
    def Enqueue(self,other):
        return self.queue.append(other)
    def __eq__(self,other):
        if self.queue == other:
            return True
        else:
            return False
    def __iter__(self):
        for i in self.queue:
            print(i)
    def Peek(self):
        i = self.queue[0]
        return i
    def __str__(self):
        return self.queue

        
        
        
        
        
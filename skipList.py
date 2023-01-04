# amirabbas gashtil 400442333
# saba sarmadi 400442171

from random import randint

class Node:  
    def __init__(self, height = 0, data=None):
        self.data = data
        self.next = [None]*height

class SkipList:

    def __init__(self):
        self.head = Node()
        self.len = 0
        self.maxHeight = 0

    def __len__(self):
        return self.len

    def searchandreturn(self, data, update=None):
        if update == None:
            update = self.update(data)
        if len(update) > 0:
            item = update[0].next[0]
            if item != None and item.data == data:
                return True
        return False

    def search(self, data, update = None):
        if update == None:
            update = self.update(data)
        if len(update) > 0:
            item = update[0].next[0]
            if item != None and item.data == data:
                return item
        return None
    
    def contains(self, data, update = None):
        return self.search(data, update) != None

    def headOrTail(self):
        height = 1
        while randint(1, 2) != 1:
            height += 1
        return height

    def update(self, data):
        update = [None]*self.maxHeight
        itr = self.head
        for i in reversed(range(self.maxHeight)):
            while itr.next[i] != None and itr.next[i].data < data:
                itr = itr.next[i]
            update[i] = itr
        return update
        
    def add(self, data):

        node = Node(self.headOrTail(), data)

        self.maxHeight = max(self.maxHeight, len(node.next))
        while len(self.head.next) < len(node.next):
            self.head.next.append(None)

        update = self.update(data)            
        if self.search(data, update) == None:
            for i in range(len(node.next)):
                node.next[i] = update[i].next[i]
                update[i].next[i] = node
            self.len += 1

    def erease(self, data):

        update = self.update(data)
        itr = self.search(data, update)
        if itr != None:
            for i in reversed(range(len(itr.next))):
                update[i].next[i] = itr.next[i]
                if self.head.next[i] == None:
                    self.maxHeight -= 1
            self.len -= 1            
                
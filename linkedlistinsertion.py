class node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class sll:
    def __init__(self):
        self.head=None
    def in_b(self,data):
        nb=node(data)
        nb.next=self.head
        self.head=nb
    def n_e(self,data):
        ne=node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne
    def n_p(self,pos,data):
        np=node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        np.data=data
        np.next=temp.next
        temp.next=np


    def print(self):
        if self.head is None:
            print("its a empty linked list")
        else:
            temp=self.head
            while temp:
                if temp.next:
                    print(temp.data,end="-->")
                else:
                    print(temp.data)
                temp=temp.next
l=sll()
l.head=node(10)
n1=node(20)
l.head.next=n1
n2=node(30)
n1.next=n2
l.in_b(22)
l.n_e(55)
l.n_p(2,77)
l.print()

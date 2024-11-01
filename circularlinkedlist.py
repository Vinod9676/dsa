class node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class sll:
    def __init__(self):
        self.head=None
        self.tail=None
    def print(self):
        temp=self.tail
        print(temp.data, end="-->")
        while temp.next !=self.head:
            temp = temp.next
            if temp.next:
                print(temp.data,end="-->")
            else:
                print(temp.data)
        temp=temp.next
        print(temp.data)
l=sll()
n=node(10)
l.head=n
l.tail=n
n1=node(20)
l.tail.next=n1
n2=node(30)
n1.next=n2
n2.next=n
l.print()

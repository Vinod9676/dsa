class node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class sll:
    def __init__(self):
        self.head=None
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
l.print()

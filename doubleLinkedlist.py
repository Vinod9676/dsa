class node:
    def __init__(self,data,next=None,pre=None):
        self.data=data
        self.next=next
        self.pre=pre
class sll:
    def __init__(self):
        self.head=None
    def print(self):
        if self.head is None:
            print("its a empty linked list")
        else:
            temp=self.head.next
            prev=self.head
            while temp:
                if temp.next:
                    print(prev.data,end="-->")
                else:
                    print(prev.data,end="-->")
                temp=temp.next
                prev=prev.next
            print(prev.data)
            print()
            while prev:
                if prev.pre:
                    print(prev.data,end="-->")
                else:
                    print(prev.data)
                prev=prev.pre
l=sll()
n=node(10)
l.head=n
n1=node(20)
n.next=n1
n1.pre=n
n2=node(30)
n1.next=n2
n2.pre=n1
l.print()

class node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class sll:
    def __init__(self):
        self.head=None
    def d_s(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    def d_e(self):
        temp=self.head.next
        prev=self.head
        while temp.next:
            temp=temp.next
            prev=prev.next
        prev.next=None
    def d_p(self,pos):
        temp = self.head.next
        prev = self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None


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
n3=node(40)
n2.next=n3
l.d_p(3)
l.print()

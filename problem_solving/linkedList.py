
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Linked_list (): 
    def __init__(self, head=None):
        self.head=head 

    def append_value(self,value):
        new_node= ListNode(value)
        if not self.head:
            self.head=new_node
        temp=self.head
        while temp.next:
            temp=temp.next    
        temp.next=new_node

    def reverseBetween( self, left: int, right: int) :
        prev=None
        temp=self.head
        count=1
        while count<=right and temp!=None:
            next=temp.next
            if count==left:
                a=prev 
                c=temp
            if count==right:
                b=next
                d=temp
            if left<=count<=right:
                temp.next=prev # 4
            prev=temp
            temp=next
            count+=1
        c.next=b
        if not a:
            self.head=d
        else:
            a.next=d
        return self.head   

    def __str__(self): 
        result = ''
        current = self.head
        while current : 
            result += f"{current.val}->"
            current=current.next 
        return result 
  

if __name__ == '__main__':
    values = [1,2,3,4,5]   
    left = 2
    right = 4
    head=ListNode(values[0])
    ll=Linked_list(head)
    for n in values[1:]:
        ll.append_value(n)
    print(ll)
    print(ll.reverseBetween(left,right))
    print(ll)
class Node:
    
    def __init__(self,value):
        self.next=None 
        self.value=value 

class MyLinkedList:

    def __init__(self):
        self.head=Node(0)  
        self.next = None 
        

        

        
        

    def get(self, index: int) -> int:
        temp = self.head
        if index < 0 :
            return -1
        for i in range(index+1):

            temp=temp.next 
            if temp == None:
                return -1

        return temp.value

        

    def addAtHead(self, val: int) -> None:
        
        newnode=Node(val)
        newnode.next = self.head.next
        self.head.next = newnode 
        


        

    def addAtTail(self, val: int) -> None:
        temp = self.head
        while temp.next != None :
           temp = temp.next
        newnode = Node(val)
        temp.next = newnode

    def addAtIndex(self, index: int, val: int) -> None:
        temp = self.head
        if index < 0 :
            return 
        for i in range(index):

            temp=temp.next
            if temp == None:
                return 
        newnode=Node(val)
        newnode.next=temp.next
        temp.next = newnode

         
        

    def deleteAtIndex(self, index: int) -> None:
        temp = self.head     
        if index < 0 :
            return -1
        for i in range(index):

            temp=temp.next
            if temp == None:
              return 
        if temp.next :
            temp.next = temp.next.next

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
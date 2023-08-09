# The Linked List is made up of a Node that has a data and the index to the 
# next node.

class Node:
    # The Node is the smallest unit of a LinkedList
    def __init__(self, data) -> None:
        self.data = data
        self.nextNode = None
    def __str__(self) -> str:
        return "This contains " + self.data

class LinkedList:
    
    def __init__(self) -> None:
        self.head = None
    # This method is to print all the elements of the LinkedList
    def listPrint(self):
        curretNode = self.head
        while curretNode is not None:
            print(curretNode.data)
            curretNode = curretNode.nextNode
    
    # This method inserts elements at the beginning
    def insertAtBeginning(self, node):
        headNode = self.head
        self.head = node
        node.nextNode = headNode
    
    # This method appends elements to the end
    def appendNode(self, node):
        
        currentNode = self.head
        if(currentNode.nextNode ==None):
            currentNode.nextNode = node
            return
        lastNode = self.head
        while lastNode.nextNode != None:
            lastNode = lastNode.nextNode
        lastNode.nextNode = node
        return
    
    # This method inserts elements at a particular index
    def appendAtIndex(self, node, index):
        currNode= self.head
        for _ in range(index-1):
            currNode =currNode.nextNode
        nextValue = currNode.nextNode
        currNode.nextNode = node
        node.nextNode = nextValue
    
    # Removes the Element at the first Index
    def removeIndexAtFirst(self):
        self.head = self.head.nextNode
    
    # Remove the element at the last Index:
    def removeElementAtLast(self):
        previousNode =self.head
        currentNode = previousNode.nextNode
        if(currentNode==None):
            self.head =None
            return 
        while currentNode !=None:
            
            previousNode = currentNode
            currentNode =currentNode.nextNode
            print(currentNode, previousNode)
            
        previousNode=None

list1= LinkedList()
node1 = Node("Mon")

list1.head = node1
node2= Node("Tue")

node3= Node("Wed")
node1.nextNode = node2
node2.nextNode= node3
node4 = Node("Sun")
list1.insertAtBeginning(node4)
list1.appendNode(Node("Thur"))
list1.appendNode(Node("Fri"))

list1.appendAtIndex(Node("Break"),2)
list1.removeElementAtLast()
# list1.listPrint()
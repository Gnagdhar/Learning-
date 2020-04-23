# Create Node
# Create LikedList
# Add nodes to Linked List
# Print data of Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertEnd(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                else:
                    lastNode = lastNode.next
            lastNode.next = newNode

    def insertFirst(self, newNode):
        tempNode = self.head
        self.head = newNode
        newNode.next = tempNode
        del tempNode

    def printData(self):
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            else:
                print(currentNode.data)
                currentNode = currentNode.next

    def insertAt(self, newNode, pos):
        currentNode = self.head
        currentPos = 0
        previousNode = None
        while True:
            if currentPos == pos:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            else:
                previousNode = currentNode
                currentNode = currentNode.next
                currentPos += 1
    def delete(self):
        lastNode = self.head
        while lastNode.next is not None:
            prvNode = lastNode
            lastNode = lastNode.next

        prvNode.next = None
        # del lastNode

    def deleteAt(self, pos):
        currentNode = self.head
        presentPos = 0
        previousNode = None
        while True:
            if presentPos == pos:
                previousNode.next = currentNode.next
                currentNode.next = None
                break
            else:
                previousNode = currentNode
                currentNode = currentNode.next
                presentPos += 1


node1 = Node("10")
Linkedlist = LinkedList()
Linkedlist.insertEnd(node1)
node2 = Node("20")
Linkedlist.insertEnd(node2)
node3 = Node("30")
Linkedlist.insertEnd(node3)
node4 = Node("40")
Linkedlist.insertEnd(node4)
node5 = Node("1")
Linkedlist.insertFirst(node5)
node6 = Node("2")
Linkedlist.insertAt(node6, 2)
Linkedlist.delete()
Linkedlist.deleteAt(1)
Linkedlist.printData()
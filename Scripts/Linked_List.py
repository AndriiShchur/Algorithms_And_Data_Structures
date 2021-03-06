class Node(object):
    
	def __init__(self, data):
		self.data = data;
		self.nextNode = None;
		
class LinkedList(object):

	def __init__(self):
		self.head = None;
		self.size = 0;
		
	# O(1) !!!	
	def insertStart(self, data):
	
		self.size = self.size + 1;
		newNode = Node(data);
		
		if not self.head:
			self.head = newNode;
		else:
			newNode.nextNode = self.head;
			self.head = newNode;
			
	def remove(self, data):
	
		if self.head is None:
			return;
			
		self.size = self.size - 1;
		
		currentNode = self.head;
		previousNode = None;
		
		while currentNode.data != data:
			previousNode = currentNode;
			currentNode = currentNode.nextNode;
			
		if previousNode is None:
			self.head = currentNode.nextNode;
		else:
			previousNode.nextNode = currentNode.nextNode;			
		
	# O(1)	
	def size1(self):
		return self.size;
		
	# O(N) not good !!!	
	def size2(self):
		
		actualNode = self.head;
		size = 0;
		
		while actualNode is not None:
			size+=1;
			actualNode = actualNode.nextNode;
			
		return size;
		
	# O(N)
	def insertEnd(self, data):
	
		self.size = self.size + 1;
		newNode = Node(data);
		actualNode = self.head;
		
		while actualNode.nextNode is not None:
			actualNode = actualNode.nextNode;
			
		actualNode.nextNode = newNode;
		
	def traverseList(self):
	
		actualNode = self.head;
		
		while actualNode is not None:
			print(actualNode.data);
			actualNode = actualNode.nextNode;


linked_list = LinkedList()
linked_list.insertStart(4)
linked_list.insertStart(3)
linked_list.insertStart(7)

linked_list.insertEnd(15)
linked_list.insertEnd(150)
linked_list.insertEnd(1500)

linked_list.insertStart(3.0)
linked_list.insertStart("Adam")


linked_list.traverseList()
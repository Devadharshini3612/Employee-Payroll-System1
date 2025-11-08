"""
Queue Data Structure Implementation in Python
FIFO - First In, First Out
"""

class Queue:
    """
    A basic queue implementation using Python list.
    Queue follows FIFO (First In, First Out) principle.
    """
    
    def __init__(self, max_size=None):
        """
        Initialize an empty queue.
        
        Args:
            max_size (int, optional): Maximum number of elements the queue can hold.
        """
        self.items = []
        self.max_size = max_size
    
    def enqueue(self, element):
        """
        Add an element to the rear of the queue.
        
        Args:
            element: The element to be added to the queue.
            
        Returns:
            int: The new size of the queue.
            
        Raises:
            OverflowError: If queue has reached its maximum size.
        """
        if self.max_size is not None and len(self.items) >= self.max_size:
            raise OverflowError("Queue overflow - maximum size reached")
        
        self.items.append(element)
        return len(self.items)
    
    def dequeue(self):
        """
        Remove and return the front element from the queue.
        
        Returns:
            The front element of the queue.
            
        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Queue underflow - queue is empty")
        
        return self.items.pop(0)
    
    def front(self):
        """
        Return the front element without removing it.
        
        Returns:
            The front element of the queue, or None if queue is empty.
        """
        if self.is_empty():
            return None
        
        return self.items[0]
    
    def rear(self):
        """
        Return the rear element without removing it.
        
        Returns:
            The rear element of the queue, or None if queue is empty.
        """
        if self.is_empty():
            return None
        
        return self.items[-1]
    
    def is_empty(self):
        """
        Check if the queue is empty.
        
        Returns:
            bool: True if queue is empty, False otherwise.
        """
        return len(self.items) == 0
    
    def size(self):
        """
        Get the number of elements in the queue.
        
        Returns:
            int: The number of elements in the queue.
        """
        return len(self.items)
    
    def clear(self):
        """
        Remove all elements from the queue.
        """
        self.items = []
    
    def set_max_size(self, size):
        """
        Set the maximum size of the queue.
        
        Args:
            size (int): The maximum number of elements allowed.
        """
        self.max_size = size
    
    def get_all(self):
        """
        Get all elements in the queue (for display/debugging).
        
        Returns:
            list: A copy of all elements in the queue.
        """
        return self.items.copy()
    
    def __str__(self):
        """
        String representation of the queue.
        
        Returns:
            str: String representation of the queue.
        """
        return str(self.items)
    
    def __repr__(self):
        """
        Official string representation of the queue.
        
        Returns:
            str: String representation showing queue contents.
        """
        return f"Queue({self.items})"
    
    def search(self, element):
        """
        Search for an element in the queue.
        
        Args:
            element: The element to search for.
            
        Returns:
            int: Index of the element from the front (0 = front), -1 if not found.
        """
        try:
            return self.items.index(element)
        except ValueError:
            return -1
    
    def element_at(self, position):
        """
        Get element at specific position from the front.
        
        Args:
            position (int): Position from front (0 = front element).
            
        Returns:
            The element at the specified position, or None if invalid position.
        """
        if position < 0 or position >= len(self.items):
            return None
        
        return self.items[position]


class CircularQueue:
    """
    Circular Queue implementation for fixed-size queues.
    More efficient for fixed-size scenarios.
    """
    
    def __init__(self, capacity):
        """
        Initialize a circular queue with given capacity.
        
        Args:
            capacity (int): Maximum number of elements the queue can hold.
        """
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = -1
        self.rear = -1
        self.size = 0
    
    def enqueue(self, element):
        """
        Add an element to the rear of the circular queue.
        
        Args:
            element: The element to be added.
            
        Returns:
            int: The new size of the queue.
            
        Raises:
            OverflowError: If the queue is full.
        """
        if self.is_full():
            raise OverflowError("Circular queue is full")
        
        if self.is_empty():
            self.front = 0
        
        self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = element
        self.size += 1
        return self.size
    
    def dequeue(self):
        """
        Remove and return the front element from the circular queue.
        
        Returns:
            The front element of the queue.
            
        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Circular queue is empty")
        
        element = self.items[self.front]
        self.items[self.front] = None
        
        if self.size == 1:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        
        self.size -= 1
        return element
    
    def get_front(self):
        """
        Return the front element without removing it.
        
        Returns:
            The front element of the queue, or None if queue is empty.
        """
        if self.is_empty():
            return None
        
        return self.items[self.front]
    
    def get_rear(self):
        """
        Return the rear element without removing it.
        
        Returns:
            The rear element of the queue, or None if queue is empty.
        """
        if self.is_empty():
            return None
        
        return self.items[self.rear]
    
    def is_empty(self):
        """
        Check if the circular queue is empty.
        
        Returns:
            bool: True if queue is empty, False otherwise.
        """
        return self.size == 0
    
    def is_full(self):
        """
        Check if the circular queue is full.
        
        Returns:
            bool: True if queue is full, False otherwise.
        """
        return self.size == self.capacity
    
    def get_size(self):
        """
        Get the number of elements in the circular queue.
        
        Returns:
            int: The number of elements in the queue.
        """
        return self.size
    
    def clear(self):
        """
        Remove all elements from the circular queue.
        """
        self.items = [None] * self.capacity
        self.front = -1
        self.rear = -1
        self.size = 0
    
    def get_all(self):
        """
        Get all elements in the circular queue.
        
        Returns:
            list: All elements in the queue from front to rear.
        """
        if self.is_empty():
            return []
        
        result = []
        current = self.front
        for i in range(self.size):
            result.append(self.items[current])
            current = (current + 1) % self.capacity
        
        return result


class PriorityQueue:
    """
    Priority Queue implementation where elements are dequeued based on priority.
    Higher priority elements are dequeued first.
    """
    
    def __init__(self):
        """
        Initialize an empty priority queue.
        """
        self.items = []
    
    def enqueue(self, element, priority):
        """
        Add an element with given priority to the queue.
        
        Args:
            element: The element to be added.
            priority (int): The priority of the element (higher number = higher priority).
            
        Returns:
            int: The new size of the queue.
        """
        queue_element = {"element": element, "priority": priority}
        
        if self.is_empty():
            self.items.append(queue_element)
        else:
            added = False
            for i in range(len(self.items)):
                if queue_element["priority"] > self.items[i]["priority"]:
                    self.items.insert(i, queue_element)
                    added = True
                    break
            
            if not added:
                self.items.append(queue_element)
        
        return len(self.items)
    
    def dequeue(self):
        """
        Remove and return the highest priority element from the queue.
        
        Returns:
            The highest priority element.
            
        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        
        return self.items.pop(0)["element"]
    
    def front(self):
        """
        Return the highest priority element without removing it.
        
        Returns:
            The highest priority element, or None if queue is empty.
        """
        if self.is_empty():
            return None
        
        return self.items[0]["element"]
    
    def is_empty(self):
        """
        Check if the priority queue is empty.
        
        Returns:
            bool: True if queue is empty, False otherwise.
        """
        return len(self.items) == 0
    
    def size(self):
        """
        Get the number of elements in the priority queue.
        
        Returns:
            int: The number of elements in the queue.
        """
        return len(self.items)
    
    def clear(self):
        """
        Remove all elements from the priority queue.
        """
        self.items = []
    
    def get_all(self):
        """
        Get all elements in the priority queue.
        
        Returns:
            list: All elements with their priorities.
        """
        return [{"element": item["element"], "priority": item["priority"]} 
                for item in self.items]


class Deque:
    """
    Double-ended Queue implementation.
    Elements can be added/removed from both ends.
    """
    
    def __init__(self):
        """
        Initialize an empty deque.
        """
        self.items = []
    
    def add_front(self, element):
        """
        Add an element to the front of the deque.
        
        Args:
            element: The element to be added.
            
        Returns:
            int: The new size of the deque.
        """
        self.items.insert(0, element)
        return len(self.items)
    
    def add_rear(self, element):
        """
        Add an element to the rear of the deque.
        
        Args:
            element: The element to be added.
            
        Returns:
            int: The new size of the deque.
        """
        self.items.append(element)
        return len(self.items)
    
    def remove_front(self):
        """
        Remove and return the front element from the deque.
        
        Returns:
            The front element of the deque.
            
        Raises:
            IndexError: If the deque is empty.
        """
        if self.is_empty():
            raise IndexError("Deque is empty")
        
        return self.items.pop(0)
    
    def remove_rear(self):
        """
        Remove and return the rear element from the deque.
        
        Returns:
            The rear element of the deque.
            
        Raises:
            IndexError: If the deque is empty.
        """
        if self.is_empty():
            raise IndexError("Deque is empty")
        
        return self.items.pop()
    
    def peek_front(self):
        """
        Return the front element without removing it.
        
        Returns:
            The front element of the deque, or None if deque is empty.
        """
        if self.is_empty():
            return None
        
        return self.items[0]
    
    def peek_rear(self):
        """
        Return the rear element without removing it.
        
        Returns:
            The rear element of the deque, or None if deque is empty.
        """
        if self.is_empty():
            return None
        
        return self.items[-1]
    
    def is_empty(self):
        """
        Check if the deque is empty.
        
        Returns:
            bool: True if deque is empty, False otherwise.
        """
        return len(self.items) == 0
    
    def size(self):
        """
        Get the number of elements in the deque.
        
        Returns:
            int: The number of elements in the deque.
        """
        return len(self.items)
    
    def clear(self):
        """
        Remove all elements from the deque.
        """
        self.items = []
    
    def get_all(self):
        """
        Get all elements in the deque.
        
        Returns:
            list: All elements in the deque.
        """
        return self.items.copy()


def simulate_printer_queue():
    """
    Simulate a printer queue using queue data structure.
    """
    print("=== Printer Queue Simulation ===")
    printer_queue = Queue()
    
    # Add print jobs
    documents = ["Document1.pdf", "Document2.docx", "Document3.txt", "Document4.pptx"]
    for doc in documents:
        printer_queue.enqueue(doc)
        print(f"Added to print queue: {doc}")
    
    print(f"\nPrint queue: {printer_queue}")
    print(f"Next to print: {printer_queue.front()}")
    
    # Process print jobs
    print("\nProcessing print jobs:")
    while not printer_queue.is_empty():
        current_job = printer_queue.dequeue()
        print(f"Printing: {current_job}")
    
    print("All documents printed!")


def simulate_customer_service():
    """
    Simulate customer service with priority queue.
    """
    print("\n=== Customer Service Simulation ===")
    service_queue = PriorityQueue()
    
    # Add customers with priorities (higher number = higher priority)
    customers = [
        ("Customer1", 1),  # Low priority
        ("VIP Customer", 5),  # High priority
        ("Customer2", 2),
        ("Premium Customer", 4),
        ("Customer3", 1)
    ]
    
    for customer, priority in customers:
        service_queue.enqueue(customer, priority)
        print(f"Added customer: {customer} (Priority: {priority})")
    
    print(f"\nService queue: {service_queue.get_all()}")
    print(f"Next to serve: {service_queue.front()}")
    
    # Process customers
    print("\nServing customers by priority:")
    while not service_queue.is_empty():
        current_customer = service_queue.dequeue()
        print(f"Serving: {current_customer}")


def simulate_browser_history():
    """
    Simulate browser history using deque.
    """
    print("\n=== Browser History Simulation ===")
    history = Deque()
    
    # Visit websites
    websites = ["google.com", "github.com", "stackoverflow.com", "youtube.com"]
    for site in websites:
        history.add_rear(site)
        print(f"Visited: {site}")
    
    print(f"\nBrowser history: {history.get_all()}")
    print(f"Current page: {history.peek_rear()}")
    
    # Go back
    print(f"Going back to: {history.remove_rear()}")
    print(f"Current page: {history.peek_rear()}")
    
    # Add new page
    history.add_rear("reddit.com")
    print(f"Visited: reddit.com")
    print(f"Updated history: {history.get_all()}")


# Example usage and testing
if __name__ == "__main__":
    print("=== Queue Implementation Demo ===")
    
    # Basic queue operations
    queue = Queue()
    print(f"Empty queue: {queue}")
    print(f"Is empty: {queue.is_empty()}")
    
    # Enqueue elements
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")
    print(f"After enqueuing A, B, C: {queue}")
    print(f"Size: {queue.size()}")
    
    # Front and rear
    print(f"Front element: {queue.front()}")
    print(f"Rear element: {queue.rear()}")
    
    # Dequeue
    print(f"Dequeued: {queue.dequeue()}")
    print(f"After dequeue: {queue}")
    
    # Search
    print(f"Search for B: {queue.search('B')}")
    print(f"Element at position 0: {queue.element_at(0)}")
    
    # Circular queue
    print("\n=== Circular Queue Demo ===")
    circ_queue = CircularQueue(3)
    circ_queue.enqueue(1)
    circ_queue.enqueue(2)
    circ_queue.enqueue(3)
    print(f"Circular queue: {circ_queue.get_all()}")
    print(f"Dequeued: {circ_queue.dequeue()}")
    circ_queue.enqueue(4)
    print(f"After enqueue 4: {circ_queue.get_all()}")
    
    # Priority queue
    print("\n=== Priority Queue Demo ===")
    pq = PriorityQueue()
    pq.enqueue("Task1", 1)
    pq.enqueue("Urgent Task", 5)
    pq.enqueue("Task2", 2)
    pq.enqueue("Critical Task", 4)
    print(f"Priority queue: {pq.get_all()}")
    print(f"Next to process: {pq.front()}")
    
    # Deque
    print("\n=== Deque Demo ===")
    deque = Deque()
    deque.add_rear(1)
    deque.add_front(2)
    deque.add_rear(3)
    deque.add_front(4)
    print(f"Deque: {deque.get_all()}")
    print(f"Remove front: {deque.remove_front()}")
    print(f"Remove rear: {deque.remove_rear()}")
    print(f"After operations: {deque.get_all()}")
    
    # Applications
    print("\n=== Queue Applications ===")
    simulate_printer_queue()
    simulate_customer_service()
    simulate_browser_history()
    
    print("\n=== Queue Demo Complete ===")
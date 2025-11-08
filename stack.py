"""
Stack Data Structure Implementation in Python
LIFO - Last In, First Out
"""

class Stack:
    """
    A basic stack implementation using Python list.
    Stack follows LIFO (Last In, First Out) principle.
    """
    
    def __init__(self, max_size=None):
        """
        Initialize an empty stack.
        
        Args:
            max_size (int, optional): Maximum number of elements the stack can hold.
        """
        self.items = []
        self.max_size = max_size
    
    def push(self, element):
        """
        Add an element to the top of the stack.
        
        Args:
            element: The element to be added to the stack.
            
        Returns:
            int: The new size of the stack.
            
        Raises:
            OverflowError: If stack has reached its maximum size.
        """
        if self.max_size is not None and len(self.items) >= self.max_size:
            raise OverflowError("Stack overflow - maximum size reached")
        
        self.items.append(element)
        return len(self.items)
    
    def pop(self):
        """
        Remove and return the top element from the stack.
        
        Returns:
            The top element of the stack.
            
        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Stack underflow - stack is empty")
        
        return self.items.pop()
    
    def peek(self):
        """
        Return the top element without removing it.
        
        Returns:
            The top element of the stack, or None if stack is empty.
        """
        if self.is_empty():
            return None
        
        return self.items[-1]
    
    def is_empty(self):
        """
        Check if the stack is empty.
        
        Returns:
            bool: True if stack is empty, False otherwise.
        """
        return len(self.items) == 0
    
    def size(self):
        """
        Get the number of elements in the stack.
        
        Returns:
            int: The number of elements in the stack.
        """
        return len(self.items)
    
    def clear(self):
        """
        Remove all elements from the stack.
        """
        self.items = []
    
    def set_max_size(self, size):
        """
        Set the maximum size of the stack.
        
        Args:
            size (int): The maximum number of elements allowed.
        """
        self.max_size = size
    
    def get_all(self):
        """
        Get all elements in the stack (for display/debugging).
        
        Returns:
            list: A copy of all elements in the stack.
        """
        return self.items.copy()
    
    def __str__(self):
        """
        String representation of the stack.
        
        Returns:
            str: String representation of the stack.
        """
        return str(self.items)
    
    def __repr__(self):
        """
        Official string representation of the stack.
        
        Returns:
            str: String representation showing stack contents.
        """
        return f"Stack({self.items})"
    
    def search(self, element):
        """
        Search for an element in the stack.
        
        Args:
            element: The element to search for.
            
        Returns:
            int: Index of the element from the top (0 = top), -1 if not found.
        """
        try:
            index = len(self.items) - 1 - self.items[::-1].index(element)
            return len(self.items) - 1 - index
        except ValueError:
            return -1
    
    def element_at(self, position):
        """
        Get element at specific position from the top.
        
        Args:
            position (int): Position from top (0 = top element).
            
        Returns:
            The element at the specified position, or None if invalid position.
        """
        if position < 0 or position >= len(self.items):
            return None
        
        return self.items[len(self.items) - 1 - position]


class StackWithMin(Stack):
    """
    Enhanced stack that keeps track of minimum element.
    """
    
    def __init__(self, max_size=None):
        super().__init__(max_size)
        self.min_stack = []
    
    def push(self, element):
        """
        Add element to stack and update minimum tracking.
        """
        super().push(element)
        
        # Update min stack
        if not self.min_stack or element <= self.min_stack[-1]:
            self.min_stack.append(element)
    
    def pop(self):
        """
        Remove element from stack and update minimum tracking.
        """
        element = super().pop()
        
        # Update min stack
        if element == self.min_stack[-1]:
            self.min_stack.pop()
        
        return element
    
    def get_min(self):
        """
        Get the minimum element in the stack.
        
        Returns:
            The minimum element, or None if stack is empty.
        """
        if not self.min_stack:
            return None
        return self.min_stack[-1]


def is_balanced_parentheses(expression):
    """
    Check if parentheses in expression are balanced using stack.
    
    Args:
        expression (str): The expression to check.
        
    Returns:
        bool: True if parentheses are balanced, False otherwise.
    """
    stack = Stack()
    opening = {'(', '[', '{'}
    closing = {')', ']', '}'}
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in expression:
        if char in opening:
            stack.push(char)
        elif char in closing:
            if stack.is_empty():
                return False
            if pairs[stack.pop()] != char:
                return False
    
    return stack.is_empty()


def reverse_string_using_stack(text):
    """
    Reverse a string using stack.
    
    Args:
        text (str): The string to reverse.
        
    Returns:
        str: The reversed string.
    """
    stack = Stack()
    
    # Push all characters to stack
    for char in text:
        stack.push(char)
    
    # Pop all characters to build reversed string
    reversed_text = ""
    while not stack.is_empty():
        reversed_text += stack.pop()
    
    return reversed_text


def decimal_to_binary(decimal_num):
    """
    Convert decimal number to binary using stack.
    
    Args:
        decimal_num (int): The decimal number to convert.
        
    Returns:
        str: Binary representation of the number.
    """
    if decimal_num == 0:
        return "0"
    
    stack = Stack()
    
    while decimal_num > 0:
        remainder = decimal_num % 2
        stack.push(str(remainder))
        decimal_num = decimal_num // 2
    
    binary_result = ""
    while not stack.is_empty():
        binary_result += stack.pop()
    
    return binary_result


# Example usage and testing
if __name__ == "__main__":
    print("=== Stack Implementation Demo ===")
    
    # Basic stack operations
    stack = Stack()
    print(f"Empty stack: {stack}")
    print(f"Is empty: {stack.is_empty()}")
    
    # Push elements
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(f"After pushing 10, 20, 30: {stack}")
    print(f"Size: {stack.size()}")
    
    # Peek
    print(f"Top element: {stack.peek()}")
    
    # Pop
    print(f"Popped: {stack.pop()}")
    print(f"After pop: {stack}")
    
    # Search
    print(f"Search for 20: {stack.search(20)}")
    print(f"Element at position 0: {stack.element_at(0)}")
    
    # Min stack
    print("\n=== Min Stack Demo ===")
    min_stack = StackWithMin()
    min_stack.push(5)
    min_stack.push(3)
    min_stack.push(7)
    min_stack.push(1)
    print(f"Stack: {min_stack}")
    print(f"Minimum: {min_stack.get_min()}")
    min_stack.pop()
    print(f"After popping, minimum: {min_stack.get_min()}")
    
    # Applications
    print("\n=== Stack Applications ===")
    
    # Balanced parentheses
    expressions = ["()[]{", "({[]})", "([)]", "((()))"]
    for expr in expressions:
        print(f"'{expr}' is balanced: {is_balanced_parentheses(expr)}")
    
    # String reversal
    text = "Hello World"
    print(f"'{text}' reversed: '{reverse_string_using_stack(text)}'")
    
    # Decimal to binary
    number = 42
    print(f"{number} in binary: {decimal_to_binary(number)}")
    
    print("\n=== Stack Demo Complete ===")
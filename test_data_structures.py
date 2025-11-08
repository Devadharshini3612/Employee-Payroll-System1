"""
Test file for Stack and Queue implementations
Demonstrates usage with payroll system examples
"""

from stack import Stack, StackWithMin, is_balanced_parentheses, reverse_string_using_stack, decimal_to_binary
from queue import Queue, CircularQueue, PriorityQueue, Deque, simulate_printer_queue, simulate_customer_service, simulate_browser_history


def payroll_stack_example():
    """
    Demonstrate stack usage with payroll data.
    """
    print("=== Payroll Stack Example ===")
    
    # Stack for tracking recent payroll actions (LIFO)
    payroll_actions = Stack()
    
    # Simulate payroll actions
    actions = [
        "Processed salary for John Doe",
        "Added bonus for Jane Smith",
        "Updated tax deductions",
        "Generated payroll report",
        "Processed final payment"
    ]
    
    print("Payroll actions (most recent first):")
    for action in actions:
        payroll_actions.push(action)
        print(f"  {action}")
    
    print(f"\nStack size: {payroll_actions.size()}")
    print(f"Most recent action: {payroll_actions.peek()}")
    
    # Undo functionality (pop recent actions)
    print("\nUndoing recent actions:")
    while not payroll_actions.is_empty():
        undone_action = payroll_actions.pop()
        print(f"  Undone: {undone_action}")
    
    print(f"Stack empty: {payroll_actions.is_empty()}")


def payroll_queue_example():
    """
    Demonstrate queue usage with payroll processing.
    """
    print("\n=== Payroll Queue Example ===")
    
    # Queue for processing employee payroll (FIFO)
    payroll_queue = Queue()
    
    # Employees waiting for payroll processing
    employees = [
        {"name": "John Doe", "id": "EMP001", "salary": 5000},
        {"name": "Jane Smith", "id": "EMP002", "salary": 6000},
        {"name": "Bob Johnson", "id": "EMP003", "salary": 5500},
        {"name": "Alice Brown", "id": "EMP004", "salary": 5200}
    ]
    
    print("Employees waiting for payroll processing:")
    for emp in employees:
        payroll_queue.enqueue(emp)
        print(f"  {emp['name']} (ID: {emp['id']}) - ${emp['salary']}")
    
    print(f"\nQueue size: {payroll_queue.size()}")
    print(f"Next employee: {payroll_queue.front()['name']}")
    
    # Process payroll (FIFO order)
    print("\nProcessing payroll in order:")
    total_processed = 0
    while not payroll_queue.is_empty():
        employee = payroll_queue.dequeue()
        total_processed += employee['salary']
        print(f"  Processed: {employee['name']} - ${employee['salary']}")
    
    print(f"Total payroll processed: ${total_processed}")
    print(f"Queue empty: {payroll_queue.is_empty()}")


def priority_payroll_example():
    """
    Demonstrate priority queue with urgent payroll tasks.
    """
    print("\n=== Priority Payroll Queue Example ===")
    
    # Priority queue for urgent payroll tasks
    urgent_tasks = PriorityQueue()
    
    # Payroll tasks with different priorities
    tasks = [
        ("Regular salary processing", 1),
        ("Urgent bonus payment", 4),
        ("Tax deadline processing", 5),
        ("Regular report generation", 2),
        ("Critical audit preparation", 5),
        ("Monthly reconciliation", 3)
    ]
    
    print("Payroll tasks with priorities:")
    for task, priority in tasks:
        urgent_tasks.enqueue(task, priority)
        print(f"  Priority {priority}: {task}")
    
    print(f"\nTotal tasks: {urgent_tasks.size()}")
    
    # Process tasks by priority
    print("\nProcessing tasks by priority (highest first):")
    while not urgent_tasks.is_empty():
        task = urgent_tasks.dequeue()
        print(f"  Processing: {task}")


def circular_buffer_example():
    """
    Demonstrate circular queue for payroll log buffer.
    """
    print("\n=== Circular Buffer Payroll Log Example ===")
    
    # Circular queue for recent payroll logs (fixed size)
    log_buffer = CircularQueue(5)
    
    # Simulate payroll logs
    logs = [
        "2024-01-01: Payroll processed for 50 employees",
        "2024-01-02: Bonus calculations updated",
        "2024-01-03: Tax rates modified",
        "2024-01-04: New employee added to payroll",
        "2024-01-05: Monthly report generated",
        "2024-01-06: Audit trail updated",  # This will overwrite the oldest log
        "2024-01-07: Salary adjustments applied"
    ]
    
    print("Payroll log buffer (most recent 5 logs):")
    for log in logs:
        try:
            log_buffer.enqueue(log)
            print(f"  Added: {log}")
        except OverflowError:
            print(f"  Buffer full, overwriting oldest log: {log}")
            log_buffer.dequeue()
            log_buffer.enqueue(log)
    
    print(f"\nCurrent buffer contents:")
    current_logs = log_buffer.get_all()
    for i, log in enumerate(current_logs, 1):
        print(f"  {i}. {log}")


def deque_example():
    """
    Demonstrate deque for bidirectional payroll processing.
    """
    print("\n=== Deque Payroll Processing Example ===")
    
    # Deque for flexible payroll processing
    processing_deque = Deque()
    
    # Add employees from both ends (simulate different processing orders)
    high_priority = ["CEO", "CFO", "CTO"]
    regular = ["Manager1", "Manager2", "Employee1", "Employee2"]
    
    print("Adding high-priority employees to front:")
    for emp in high_priority:
        processing_deque.add_front(emp)
        print(f"  Added to front: {emp}")
    
    print("\nAdding regular employees to rear:")
    for emp in regular:
        processing_deque.add_rear(emp)
        print(f"  Added to rear: {emp}")
    
    print(f"\nDeque contents: {processing_deque.get_all()}")
    
    # Process from both ends
    print("\nProcessing from both ends:")
    print(f"  Process from front (high priority): {processing_deque.remove_front()}")
    print(f"  Process from rear (regular): {processing_deque.remove_rear()}")
    print(f"  Process from front (high priority): {processing_deque.remove_front()}")
    
    print(f"\nRemaining employees: {processing_deque.get_all()}")


def validate_payroll_expressions():
    """
    Use stack to validate payroll calculation expressions.
    """
    print("\n=== Payroll Expression Validation Example ===")
    
    # Payroll calculation expressions
    expressions = [
        "(salary + bonus) * tax_rate",
        "((base_salary + overtime) - deductions)",
        "[gross_pay - (tax + insurance)]",
        "{(annual_salary / 12) + benefits}",
        "(salary + bonus",  # Invalid - missing closing parenthesis
        "[pay - tax)"      # Invalid - mismatched brackets
    ]
    
    print("Validating payroll expressions:")
    for expr in expressions:
        is_valid = is_balanced_parentheses(expr)
        status = "✓ Valid" if is_valid else "✗ Invalid"
        print(f"  {expr:<30} {status}")


def payroll_data_processing():
    """
    Demonstrate various data structure operations with payroll data.
    """
    print("\n=== Payroll Data Processing Example ===")
    
    # Stack for salary history (LIFO)
    salary_history = Stack()
    salaries = [50000, 52000, 55000, 58000, 60000]
    
    print("Salary progression (stack):")
    for salary in salaries:
        salary_history.push(salary)
        print(f"  Salary: ${salary:,}")
    
    print(f"Current salary: ${salary_history.peek():,}")
    print(f"Previous salary: ${salary_history.element_at(1):,}")
    
    # Queue for employee onboarding (FIFO)
    onboarding_queue = Queue()
    new_employees = ["Alice", "Bob", "Charlie", "Diana"]
    
    print(f"\nEmployee onboarding queue: {new_employees}")
    for emp in new_employees:
        onboarding_queue.enqueue(emp)
    
    print("Processing onboarding in order:")
    while not onboarding_queue.is_empty():
        emp = onboarding_queue.dequeue()
        print(f"  Onboarded: {emp}")
    
    # Decimal to binary for employee IDs
    print(f"\nBinary representation of employee ID 42: {decimal_to_binary(42)}")
    
    # Reverse string for data formatting
    employee_name = "John Doe"
    reversed_name = reverse_string_using_stack(employee_name)
    print(f"Reversed employee name: {reversed_name}")


def run_all_tests():
    """
    Run all payroll data structure examples.
    """
    print("🧮 PAYROLL DATA STRUCTURES DEMO")
    print("=" * 50)
    
    payroll_stack_example()
    payroll_queue_example()
    priority_payroll_example()
    circular_buffer_example()
    deque_example()
    validate_payroll_expressions()
    payroll_data_processing()
    
    print("\n" + "=" * 50)
    print("✅ All payroll data structure examples completed!")


if __name__ == "__main__":
    run_all_tests()
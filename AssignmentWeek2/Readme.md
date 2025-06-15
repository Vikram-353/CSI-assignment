# Linked List Implementation in Python

A simple implementation of a singly linked list data structure with basic operations including node addition, deletion, and traversal.

## Features

- **Add Node**: Insert nodes at the end of the list
- **Print List**: Display all elements in the list
- **Delete Node**: Remove node at a specific position (1-based indexing)
- **Error Handling**: Comprehensive exception handling for edge cases

## Code Structure

The implementation consists of two main classes:

### `Node` Class

Represents individual nodes in the linked list with:

- `data`: Stores the node's value
- `next`: Reference to the next node

### `LinkedList` Class

Manages the linked list operations with:

- `head`: Reference to the first node
- `add_node()`: Adds new nodes to the end
- `print_list()`: Displays the entire list
- `delete_nth_node()`: Removes node at specified position

## Usage

```python
# Create a new linked list
ll = LinkedList()

# Add nodes
ll.add_node(67)
ll.add_node(364)
ll.add_node(343)

# Print the list
ll.print_list()  # Output: 67 -> 364 -> 343 -> None

# Delete node at position 2
ll.delete_nth_node(2)  # Deletes 364

# Print updated list
ll.print_list()  # Output: 67 -> 343 -> None
```

## Sample Output

```bash
Initial Linked List:
67 -> 364 -> 343 -> 230 -> 20 -> None
Deleted node at position 3: 343
After Deleting 3rd Node:
67 -> 364 -> 230 -> 20 -> None
Error: Index out of range.
Deleted node at position 1: 67
After Deleting 1st Node:
364 -> 230 -> 20 -> None
Error: Cannot delete from an empty list.
```

## Object-Oriented Programming Concepts Used

This implementation demonstrates several key OOP principles:

### 1. **Encapsulation**

- Data (node values, references) and methods (operations) are bundled together within classes
- Internal implementation details are hidden from external code
- Access to data is controlled through defined methods

### 2. **Abstraction**

- Complex linked list operations are simplified into easy-to-use methods
- Users interact with high-level methods without needing to understand internal pointer manipulation
- The `LinkedList` class provides a clean interface hiding the complexity of node management

### 3. **Data Hiding**

- Internal attributes like `head`, `data`, and `next` are accessed through methods
- Implementation details are concealed from the user
- The structure maintains data integrity through controlled access

### 4. **Modularity**

- Code is organized into separate, reusable classes (`Node` and `LinkedList`)
- Each class has a specific responsibility and purpose
- Easy to maintain, test, and extend

### 5. **Constructor Usage**

- `__init__` methods initialize object state
- Proper object initialization ensures data integrity from creation

### 6. **Method Organization**

- Related functionality is grouped within appropriate classes
- Clear separation of concerns between `Node` (data storage) and `LinkedList` (operations)

## Error Handling

The implementation includes robust error handling for:

- Deleting from empty lists
- Invalid index positions (less than 1)
- Index out of range scenarios
- Attempting to access non-existent nodes

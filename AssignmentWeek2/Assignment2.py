class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        """Add node to the end of the list"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def print_list(self):
        """Print all elements in the list"""
        if not self.head:
            print("List is empty.")
            return
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

    def delete_nth_node(self, n):
        """Delete the nth node (1-based index)"""
        try:
            if not self.head:
                raise Exception("Cannot delete from an empty list.")

            if n <= 0:
                raise Exception("Index must be 1 or greater.")

            if n == 1:
                deleted_data = self.head.data
                self.head = self.head.next
                print(f"Deleted node at position {n}: {deleted_data}")
                return

            curr = self.head
            for _ in range(n - 2):
                if not curr.next:
                    raise Exception("Index out of range.")
                curr = curr.next

            if not curr.next:
                raise Exception("Index out of range.")

            deleted_data = curr.next.data
            curr.next = curr.next.next
            print(f"Deleted node at position {n}: {deleted_data}")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    ll = LinkedList()
    
    ll.add_node(67)
    ll.add_node(364)
    ll.add_node(343)
    ll.add_node(230)
    ll.add_node(20)

    print("Initial Linked List:")
    ll.print_list()

    ll.delete_nth_node(3)

    print("After Deleting 3rd Node:")
    ll.print_list()

    ll.delete_nth_node(10)

    ll.delete_nth_node(1)
    
    print("After Deleting 1st Node:")
    ll.print_list()

    empty_list = LinkedList()
    empty_list.delete_nth_node(1)

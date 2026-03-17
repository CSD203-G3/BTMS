# data_structures.py
from models import BSTNode, LLNode

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, route_data):
        if self.root is None:
            self.root = BSTNode(route_data)
        else:
            self._insert_recursive(self.root, route_data)

    def _insert_recursive(self, node, data):
        if data.route_code < node.data.route_code:
            if node.left is None: node.left = BSTNode(data)
            else: self._insert_recursive(node.left, data)
        elif data.route_code > node.data.route_code:
            if node.right is None: node.right = BSTNode(data)
            else: self._insert_recursive(node.right, data)
        else:
            print("Route code already exists!")

    def inorder(self, node, result_list=None):
        if result_list is None: result_list = []
        if node:
            self.inorder(node.left, result_list)
            result_list.append(node.data)
            self.inorder(node.right, result_list)
        return result_list

    def bfs(self):
        if not self.root: return []
        queue = [self.root] # Dùng list như 1 queue cơ bản
        result = []
        while queue:
            current = queue.pop(0)
            result.append(current.data)
            if current.left: queue.append(current.left)
            if current.right: queue.append(current.right)
        return result

    def search(self, route_code):
        return self._search_recursive(self.root, route_code)

    def _search_recursive(self, node, code):
        if node is None or node.data.route_code == code:
            return node
        if node.data.route_code < code:
            return self._search_recursive(node.right, code)
        return self._search_recursive(node.left, code)

    def delete_by_copy(self, route_code):
        self.root = self._delete_node(self.root, route_code)

    def _delete_node(self, root, key):
        if not root: return root
        if key < root.data.route_code:
            root.left = self._delete_node(root.left, key)
        elif key > root.data.route_code:
            root.right = self._delete_node(root.right, key)
        else:
            if not root.left: return root.right
            elif not root.right: return root.left
            
            # Delete by copy: lấy phần tử nhỏ nhất bên phải đắp lên
            temp = self._get_min_value_node(root.right)
            root.data = temp.data 
            root.right = self._delete_node(root.right, temp.data.route_code)
        return root

    def _get_min_value_node(self, node):
        current = node
        while current.left is not None: current = current.left
        return current

    def balance(self):
        nodes = self.inorder(self.root)
        self.root = self._build_tree_from_sorted_list(nodes, 0, len(nodes) - 1)

    def _build_tree_from_sorted_list(self, nodes, start, end):
        if start > end: return None
        mid = (start + end) // 2
        node = BSTNode(nodes[mid])
        node.left = self._build_tree_from_sorted_list(nodes, start, mid - 1)
        node.right = self._build_tree_from_sorted_list(nodes, mid + 1, end)
        return node

    def count(self):
        return len(self.inorder(self.root))


class LinkedList:
    def __init__(self):
        self.head = None

    def add_last(self, data):
        new_node = LLNode(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def get_all(self):
        result = []
        curr = self.head
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result

    def search_passenger(self, p_id):
        curr = self.head
        while curr:
            if curr.data.passenger_id == p_id: return curr.data
            curr = curr.next
        return None

    def delete_passenger(self, p_id):
        curr = self.head
        prev = None
        while curr and curr.data.passenger_id != p_id:
            prev = curr
            curr = curr.next
        if not curr: return False # Không tìm thấy
        if not prev: self.head = curr.next # Xóa head
        else: prev.next = curr.next
        return True

    def delete_booking(self, b_id):
        curr = self.head
        prev = None
        while curr and curr.data.booking_id != b_id:
            prev = curr
            curr = curr.next
        if not curr: return False
        if not prev: self.head = curr.next
        else: prev.next = curr.next
        return True

    def sort_bookings(self):
        # Bubble sort đổi data trực tiếp trong Linked List
        if not self.head or not self.head.next: return
        swapped = True
        while swapped:
            swapped = False
            curr = self.head
            while curr.next:
                str1 = curr.data.route_code + curr.data.passenger_id
                str2 = curr.next.data.route_code + curr.next.data.passenger_id
                if str1 > str2:
                    curr.data, curr.next.data = curr.next.data, curr.data
                    swapped = True
                curr = curr.next
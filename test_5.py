
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        # flistning boshiga element qo'shish
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, prev_node, new_data):
        # listning ixtiyoriy nuqtasiga element qo'shish
        if prev_node is None:
            print("ERROR")
        # yangi element qo'shamiz
        new_node = Node(new_data)
        # yangi tugunni keyingi elementga qo'shamiz
        new_node.next = prev_node.next
        # avvalgi tugunni yangi elementga bog'laymiz
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    # bu method da hohlagan bitta elementni o'chirish mumkin o'zining nomi bilan

    def remove(self, deleted_data):
        if self.head is None:
            print("ERROR")

        if deleted_data == self.head:
            self.head = deleted_data.next

        last = self.head
        while last.next:
            if deleted_data == last.next:
                last.next = deleted_data.next
            last = last.next

    def sort(self):
        last = self.head
        while last.next:
            last = last.next
            if last.data < last.next.data:
                self.head = last.next


a = Node(201)
b = Node(101)
c = Node(121)
d = Node(3021)
e = Node(413)
f = Node(501)
r = Node(603)
k = Node(703)
linked = LinkedList()
linked.head = a
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = r
r.next = k
linked.print_list()

print("push")
linked.push(421)
linked.print_list()

print("append")
linked.append(840)
linked.print_list()

print("insert")
linked.insert(b, 230)
linked.print_list()

print("remove")
linked.remove(d)
linked.print_list()


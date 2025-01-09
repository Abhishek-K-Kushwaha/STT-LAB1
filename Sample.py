class Node:

  def __init__(self, data, next=None):
    self.data = data
    self.next = next


class linked_list:

  def __init__(self):
    self.head = None

  def insert_at_head(self, data):
    node = Node(data, self.head)
    self.head = node

  def print(ll):
    if ll.head == None:
      print("empty ll")
      return

    else:
      while ll.head != None:
        print(ll.head.data, end="-")
        ll.head = ll.head.next


ll1 = linked_list()
ll1.insert_at_head(13)
ll1.insert_at_head(25)
ll1.insert_at_head(50)
ll1.insert_at_head(75)

ll1.print()

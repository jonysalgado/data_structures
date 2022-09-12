


class Node:
    def __init__(self, dataval:str=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def print_elements(self):

      printval = self.headval
      while printval is not None:
         print(printval.dataval)
         printval = printval.nextval

    def add_to_begining(self, newdata):
        
        new_node = Node(newdata)
        new_node.nextval = self.headval
        self.headval = new_node

    def add_to_end(self, newdata):

        new_node = Node(newdata)
        if self.headval is None:
            self.headval = new_node
            return
        last = self.headval
        while(last.nextval is not None):
            last = last.nextval

        last.nextval = new_node

    def add_between(self, middle_node, new_data):

        assert middle_node != None

        new_node = Node(new_data)
        new_node.nextval = middle_node.nextval
        middle_node.nextval = new_node

    def remove_node(self, value):

        head_val = self.head

        if(head_val is not None):
            if(head_val.dataval == value):
                self.head = head_val.nextval
                head_val = None
                return
            while(head_val is not None):
                if head_val.dataval == value:
                    break
                prev = head_val
                head_val = head_val.nextval

            if(head_val is None):
                return

            prev.dataval = head_val.next
            head_val = None
        
        return


list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
# Link first Node to second node
list1.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3
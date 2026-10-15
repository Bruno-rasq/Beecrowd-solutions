import sys


class Node:
    def __init__(self, value=''):
        self.value = value
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def appendEnd(self, value):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode

    def appendHome(self, value):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def joinList(self):
        segment = ""
        pointer = self.head

        while pointer:
            segment += pointer.value
            pointer = pointer.next

        return segment


lines = sys.stdin.read().splitlines()

for line in lines:
    result = DoubleLinkedList()
    current_segment = []
    HomePress = False

    for char in line:
        if char == '[':
            if current_segment:
                text = "".join(current_segment)

                if not HomePress:
                    result.appendEnd(text)
                else:
                    result.appendHome(text)

                current_segment = []

            HomePress = True

        elif char == ']':
            if current_segment:
                text = "".join(current_segment)
                current_segment = []

                if not HomePress:
                    result.appendEnd(text)
                else:
                    result.appendHome(text)

            HomePress = False

        else:
            current_segment.append(char)

    if current_segment:
        text = "".join(current_segment)

        if not HomePress:
            result.appendEnd(text)
        else:
            result.appendHome(text)

    print(result.joinList())
def solution(n, k, cmd):
    class Node(object):
        def __init__(self, name=None, prev=None, next=None):
            self.name = name
            self.prev = prev
            self.next = next
    
    class Table(object):
        def __init__(self):
            self.head = None
            self.tail = None
            self.cursor = None
            self.trash = []
            
        def create(self,n,k):
            self.head = node = Node(0)
            for name in range(1, n-1):
                node.next = next_node = Node(name)
                next_node.prev = node
                node = next_node
                if k == name:
                    self.cursor = node
            node.next = self.tail = Node(n-1)
            self.tail.prev = node
            
            if k == 0: self.cursor = self.head
            elif k == n-1: self.cursor = self.tail
            
        def down(self, k):
            for _ in range(k):
                self.cursor = self.cursor.next
        
        def up(self, k):
            for _ in range(k):
                self.cursor = self.cursor.prev
        
        def delete(self):
            self.trash.append(self.cursor)
            if self.cursor == self.head:
                self.cursor.next.prev = None
                self.head = self.cursor = self.cursor.next
                
            elif self.cursor == self.tail:
                self.cursor.prev.next = None
                self.tail = self.cursor = self.cursor.prev
                
            else:
                self.cursor.next.prev = self.cursor.prev
                self.cursor.prev.next = self.cursor.next
                self.cursor = self.cursor.next
            # print("커서", self.cursor.name)
        
        def undo(self):
            undo_node = self.trash.pop()
            if undo_node.prev:
                undo_node.prev.next = undo_node
            if undo_node.next:
                undo_node.next.prev = undo_node
            
            if not undo_node.prev: 
                self.head = undo_node
            if not undo_node.next:
                self.tail = undo_node
            
        def result(self):
            ans = ['X']*n
            node = self.head
            ans[node.name] = 'O'
            while node.next:
                node = node.next
                ans[node.name] = 'O'
            return ans
        
        # def debug(self):
        #     node = self.head
        #     print('노드명: ', node.name, end=' ')
        #     for _ in range(1,n-1):
        #         print('next: ', node.next.name)
        #         node = node.next
        #         print('노드명: ', node.name, end=' ')
        #     print('next: ', node.next.name)
        #     node = node.next
        #     print('노드명: ', node.name, end=' ')

    table = Table()
    table.create(n,k)

    for comm in cmd:
        if comm[0] == 'C': 
            table.delete()
        elif comm[0] =='D':
            _, k = comm.split(" ")
            table.down(int(k))
        elif comm[0] =='U':
            _, k = comm.split(" ")
            table.up(int(k))
        else:
            table.undo()

    
    return ''.join(table.result())
        
# print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])        )

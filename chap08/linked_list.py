from __future__ import annotations
from typing import Any, Type

class Node:

    def __init__(self, data: Any = None, next: Node = None):
        """초기화"""
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.no = 0
        self.head = None
        self.current = None

    def __len__(self) -> int:
        return self.no
    
    def search(self, data: Any) -> int:
        cnt = 0
        ptr = self.head
        while ptr is not None:
            if ptr.data == data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = ptr.next
        return -1
    
    def __contatins__(self, data: Any) -> bool:
        """연결 리스트에 data가 포함되어 있는지 확인"""
        return self.search(data) >= 0
    
    def add_first(self, data: Any) -> None:
        """맨 앞에 노드를 삽입"""
        ptr = self.head
        self.head = self.current = Node(data, ptr)
        self.no += 1

    def add_last(self, data: Any):
        """맨 끝에 노드를 삽입"""
        if self.head is None:
            self.add_first(data)
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = self.current = Node(data, Node)
            self.no += 1
    

    
        
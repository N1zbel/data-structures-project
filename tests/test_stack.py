from src.stack import Stack


stack = Stack()
stack.push('data1')
stack.push('data2')
stack.push('data3')

def test_push():
    assert stack.top.data == 'data3'
    assert stack.top.next_node.data == 'data2'

def test_pop():
    assert stack.pop() == 'data3'
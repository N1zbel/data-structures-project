from src.stack import Stack




def test_push():
    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    stack.push('data3')
    assert stack.top.data == 'data3'
    assert stack.top.next_node.data == 'data2'

def test_pop():
    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    stack.push('data3')
    assert stack.pop() == 'data3'
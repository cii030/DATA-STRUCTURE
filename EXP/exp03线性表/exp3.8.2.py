from LinkedList import LinkedList
from CircularLinkedList import CircularLinkedlist

def testLinkedList(n, lst):
    if n == 'empty':
        print(lst.empty())
    elif n == 'len':
        print(lst.__len__())
    elif n == 'clear':
        lst.clear()
        print(lst)
    elif n == 'insert':
        item, i = eval(input('请输入要插入的值item和位置i（用,隔开）: '))
        lst.insert(i, item)
        print(lst)
    elif n == 'remove':
        i = int(input('请输入要删除的位置i: '))
        lst.remove(i)
        print(lst)
    elif n == 'retrieve':
        i = int(input('请输入想要输出元素的位置: '))
        print(lst.retrieve(i))
    elif n == 'replace':
        item, i = eval(input('请输入要更改的值item和位置i（用,隔开）: '))
        lst.replace(i, item)
        print(lst)
    elif n == 'contains':
        item = int(input('请输入要查询的元素item: '))
        print(lst.contains(item))
    elif n == 'reverse':
        lst.reverse()
        print(lst)
    else:
        print('未知的指令')


def test1():
    lst = LinkedList()
    while 1:
        n = input('请输入想要实现的方法（按Q或q退出程序）: ')
        if n == 'q' or n == 'Q':
            print('游戏停止')
            break
        else:
            try:
                testLinkedList(n,lst)
            except IndexError:
                print('位置不合法')

def testCircularLinkedList(n, lst):
    if n == 'empty':
        print(lst.empty())
    elif n == 'len':
        print(lst.__len__())
    elif n == 'clear':
        lst.clear()
        print(lst)
    elif n == 'insert':
        item, i = eval(input('请输入要插入的值item和位置i（用,隔开）: '))
        lst.insert(i, item)
        print(lst)
    elif n == 'remove':
        i = int(input('请输入要删除的位置i: '))
        lst.remove(i)
        print(lst)
    elif n == 'retrieve':
        i = int(input('请输入想要输出元素的位置: '))
        print(lst.retrieve(i))
    elif n == 'replace':
        item, i = eval(input('请输入要更改的值item和位置i（用,隔开）: '))
        lst.replace(i, item)
        print(lst)
    elif n == 'contains':
        item = int(input('请输入要查询的元素item: '))
        print(lst.contains(item))
    elif n == 'reverse':
        lst.reverse()
        print(lst)
    else:
        print('未知的指令')


def test2():
    lst = CircularLinkedlist()
    while 1:
        n = input('请输入想要实现的方法（按Q或q退出程序）: ')
        if n == 'q' or n == 'Q':
            print('游戏停止')
            break
        else:
            try:
                testLinkedList(n,lst)
            except IndexError:
                print('位置不合法')

if __name__ == '__main__':
    test2()
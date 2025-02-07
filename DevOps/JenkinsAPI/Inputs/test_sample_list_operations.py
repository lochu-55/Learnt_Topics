import pytest

def test_list():

    l1 = [8,9,4,5]
    l1.reverse()
    print("reversed list is: ",l1)

    l2 = [9,2,3,4,5,8,7,6]
    l2.sort()
    print("the sorted list: ",l2 )

    l3=l2.copy()
    print("list3: ",l3)

    index = l2[2:4]
    print("the index values are: ",index)
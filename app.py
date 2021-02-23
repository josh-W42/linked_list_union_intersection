class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    '''
    Computes the union operation on two linked lists.

    Returns:
        The result as a new linked list.
    '''
    if type(llist_1) != LinkedList or type(llist_2) != LinkedList:
        raise TypeError('Input must be of type: LinkedList')

    value_set = set()

    output_list = LinkedList()

    # Loop through list 1
    if llist_1.head:
        cur_node = llist_1.head

        while cur_node:
            if not cur_node.value in value_set:
                value_set.add(cur_node.value)
                output_list.append(cur_node.value)

            cur_node = cur_node.next

    
    # loop through list 2
    if llist_2.head:
        cur_node = llist_2.head

        while cur_node:
            if not cur_node.value in value_set:
                value_set.add(cur_node.value)
                output_list.append(cur_node.value)

            cur_node = cur_node.next

    return output_list
    

def intersection(llist_1, llist_2):
    '''
    Computes the intersection operation on two linked lists.

    Returns:
        The result of the intersection as a new linked list

    '''
    if type(llist_1) != LinkedList or type(llist_2) != LinkedList:
        raise TypeError('Input must be of type: LinkedList')

    value_set = set()

    output_list = LinkedList()

    # Loop through list 1
    if llist_1.head:
        cur_node = llist_1.head

        while cur_node:
            if not cur_node.value in value_set:
                value_set.add(cur_node.value)

            cur_node = cur_node.next

    
    # loop through list 2
    if llist_2.head:
        cur_node = llist_2.head

        while cur_node:
            if cur_node.value in value_set:
                output_list.append(cur_node.value)

            cur_node = cur_node.next


    return output_list

def test_suite():
    '''Runs a series of tests on the union and intersection methods'''

    print('\nBasic input tests Starting\n')

    print('Empty List Test for Union: ', end=' ')
    basic_linkedList_1 = LinkedList()
    basic_linkedList_2 = LinkedList()
    
    if union(basic_linkedList_1, basic_linkedList_2).size() == 0:
        print('pass')
    else:
        print('Fail')

    print('Empty List Test for Intersection: ', end=' ')
    
    if intersection(basic_linkedList_1, basic_linkedList_2).size() == 0:
        print('pass')
    else:
        print('Fail')



    print('Null Test for Union: ', end=' ')
    try:
        union(None, None)
    except TypeError:
        print('Pass')
    else:
        print('Fail')


    print('Null Test for Intersection: ', end=' ')
    try:
        intersection(None, None)
    except TypeError:
        print('Pass')
    else:
        print('Fail')


    print('\nFunction tests Starting \n')

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,21]
    element_2 = [6,32,4,9,6,1,11,21,1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    element_1 = set(element_1)
    element_2 = set(element_2)
    
    set_union_test = element_1.union(element_2)
    set_inter_test = element_1.intersection(element_2)

    my_solution_union = union(linked_list_1,linked_list_2)
    my_solution_inter = intersection(linked_list_1,linked_list_2)

    union_set = set()

    if my_solution_union.head:
        cur_node = my_solution_union.head
        
        union_set.add(cur_node.value)

        while cur_node.next:
            cur_node = cur_node.next
            
            union_set.add(cur_node.value)

    print('Union Test:', end=' ')

    if len(union_set.difference(set_union_test)) == 0:
        print('Pass')
    else:
        print('Fail')

    inter_set = set()

    if my_solution_inter.head:
        cur_node = my_solution_inter.head
        
        inter_set.add(cur_node.value)

        while cur_node.next:
            cur_node = cur_node.next

            inter_set.add(cur_node.value)
    
    print('Intersection Test:', end=' ')

    if len(inter_set.difference(set_inter_test)) == 0:
        print('Pass')
    else:
        print('Fail')

    print('\n')



if __name__ == "__main__":
    test_suite()
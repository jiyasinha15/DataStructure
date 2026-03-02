MAX = 10

data = [0] * MAX
next = [1] * MAX

head = -1      #start of linked list
free = 0       #start of free list

for i in range(MAX - 1):
    next[i] = i + 1
next[MAX - 1] = -1


def insert_begin(value):
    global head, free

    if free == -1:
        print("Overflow")
        return

    new_node = free
    free = next[free]

    data[new_node] = value
    next[new_node] = head
    head = new_node


def display():
    temp = head
    while temp != -1:
        print(data[temp], end=" -> ")
        temp = next[temp]
    print("Null")

insert_begin(10)
insert_begin(20)
insert_begin(30)

display()


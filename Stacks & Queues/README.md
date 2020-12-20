# Stack

The Stack Data Structure follows the First-In-Last-Out principle or the Last-In-First-Out. We can only add (push) and get data from the top (pop) of the stack. As we add more and more elements to the stack the other elements sink further in the stack. Stacks can be used for web browsers to keep track of previously visited pages and they are used in text editors to store changes in the document so that you can undo changes.

## List Implementation

The list implementation uses a simple list to store the data. This is easy to implement, however the array has a constant size and so must be resized when there are too many elements in the array. This complicates the runtime of the pop and push operations

### Operations

| Operation | Runtime |
|-----------|---------|
| top       | O(1)    |
|-----------|---------|
| push      | O(1) *  |
|-----------|---------|
| pop       | O(1) *  |
|-----------|---------|
| length    | O(1)    |
|-----------|---------|
| is_empty  | O(1)    |
|-----------|---------|

* These Operations in most situations take constant time but in some cases the worst case becomes O(n) where n is the number of elements in the stack. This is because the array needs to be resized.

## Singly linked List Implementation

The singly linked list implementation has nodes which each contain a value and reference to the next node in the stack. The bottom node in the stack contains no reference to other nodes. This implementation is much easier because we don't need to bother about resizing operations. We simply keep a reference to the top node and a reference to the number of nodes in the stack.

| Operation | Runtime |
|-----------|---------|
| top       | O(1)    |
|-----------|---------|
| push      | O(1)    |
|-----------|---------|
| pop       | O(1)    |
|-----------|---------|
| length    | O(1)    |
|-----------|---------|
| is_empty  | O(1)    |
|-----------|---------|

# Queue

The Queue data structure follows the First-In-First-Out principle. This means that we can only look and remove data from the front of the queue and we can only add new data to the end of the queue. The data at the front of the queue is data that has been in the front for the longest, because of this it is mostly useful for scheduling tasks. There are five main operations: enqueue: add data to end, dequeue: remove data from front, first: check first element, is_empty: check if queue is empty, length: the number of elements in the queue.

## List Implementation

The list implementation is much more complicated than the singly linked list implementation, because if we enqueue and dequeue continously the data in the queue shifts right continously so the list exapnds with each enqueue operation. Because of this we have to make the list circular, which means we have to keep a reference to the front of the queue and we resize the array when there are too many elements for it.

| Operation | Runtime |
|-----------|---------|
| first     | O(1)    |
|-----------|---------|
| enqueue      | O(1) *   |
|-----------|---------|
| dequeue       | O(1) *   |
|-----------|---------|
| length    | O(1)    |
|-----------|---------|
| is_empty  | O(1)    |
|-----------|---------|

* Most operations are in constant time, however some operations, similar to the list implemented stack are in O(n) time because of array resizing.

## Singly Linked List Implementation

The singly linked list implementation uses nodes to keep track of the data and the references to other nodes. There is a reference to the head and a reference to the tail. This means that adding elements to the front and deleting elements from the front takes constant time. The add operation for the last element of the array is also a constant time operation. To delete the last element is a linear time operation.

# Dequeue

A Dequeue is a queue but we can add and delete elements on both sides of the queue. We pronounce it 'deck' as to not collide the with delete operation dequeue. We have the same operations as the queue but we can now add to the front and we can delete from the rear. The addition to the front is a constant time operation, and the deletion from the rear is a linear time operation.

## List Implementation


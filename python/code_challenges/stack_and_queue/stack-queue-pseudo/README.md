# Challenge Summary
## Implement a Queue using two Stacks.

## Whiteboard Process
<!-- Embedded whiteboard image -->
-at the enqueue , will push the value to the first stack
so we will have a FILO list

at the dequeue will loop in first stack if the second stack is empty and do
 - pop from first_stack and push the value to the second stack
 - after finish , will pop from the second stack
 - thats it

## Approach & Efficiency
i will solve this problem by inserting nodes in the first stack, then reverse the nodes by moving them to the second stack and pop for the dequeue

| Time | Space |
| :----------- | :----------- |
| O(n) | O(1) |
## Solution
<!-- Show how to run your code, and examples of it in action -->

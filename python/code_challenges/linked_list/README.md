# Daily Code Challenge 

## linked list
*Author: Odeh Abuzaid*

---

### Problem Domain
Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.

---

### Inputs and Expected Outputs

example : 
```py
arr = ["1", "2", "3", "4", "5"]
iter_values = LinkedList(arr)

print(iter_values) # {1} -> {2} -> {3} -> {4} -> {5} -> Null
```
---

### Big O

| Time | Space |
| :----------- | :----------- |
| O(n) | O(n) |

---

### Change Log
***
14.oct 2021 first commit

16.oct 2021  

- fixed : includes method that indicates whether that value exists as a Node’s value somewhere within the list.

- fixed : return string formating.
- fixed : test import links.
- added : tests that met with all requirements.
- added : `__iter__`  to LinkedList :   yields every single node.
- added : `__main__` :   Verify & Validate Requirements 
- added : `collect`  :   returns a collection of all the values exists
---

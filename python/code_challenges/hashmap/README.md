# Hashtables
Implement a Hashtable Class with the following methods:

add
---

This method should hash the key, and add the key and value pair to the table, handling collisions as needed.

Arguments: key, value
Returns: nothing


get
---

Arguments: key
Returns: Value associated with that key in the table


contains
--------
Arguments: key

Returns: Boolean, indicating if the key exists in the table
already.


hash
----
Arguments: key

Returns: Index in the collection for that key

## Approach & Efficiency
by creating a list and inserting LLists inside that list indeces

each index will be the has of the key value

- insertion:
    - Time -> O(1)
    - Space -> O(1)
- retrieval:
    - Time -> O(n)
    - Space -> O(1)

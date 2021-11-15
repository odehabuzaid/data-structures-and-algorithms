-   [Insertion Sort](#Insertion-sort)
-   [Pseudocode](#Pseudocode)
-   [Trace](#Trace)
-   [Efficency](#Efficency)

Insertion Sort is a sorting algorithm where the sorted array is built having one item at a time. The array elements are compared with each other sequentially and then arranged simultaneously in some particular order.

## Pseudocode

```
  InsertionSort(int[] arr)
    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp
```

## Trace

Sample Array: `[8,4,23,42,16,15]`


<img src='.\blog\capture.JPG'>



**Pass 1**:
in this iteration where :

while loop : 1 0 -> [8, 4, 23, 42, 16, 15]

<img src='.\blog\1.JPG'>
<br><br>
temp = arr[i] = 4
<br>
<ins>`i = 1`</ins>  &  <ins>`j = 0`</ins>
<br>
<ins>`arr[i]`</ins>  = 4

<ins>`arr[j]`</ins>  = 8

__4 is less than 8__

then -> arr[0+1] = 8

after exiting the while -> arr[0+1] = temp = 4

in the third iteration where i = 2  this is how the list will look like :
<img src='.\blog\2.JPG'>

<ins> this process will accure also in the 4th and 5th iteration as follow:


<img src='.\blog\4.JPG'>
<img src='.\blog\5.JPG'>


After last iteration, it will break out of the for loop and leaving our array now sorted.

```
[4, 8, 15, 16, 23, 42]
```

## Efficency

-   Time: O(n^2)
    -   The basic operation of this algorithm is comparison. This will happen n \* (n-1) number of times…concluding the algorithm to be n squared.
-   Space: O(1)
    -   No additional space is being created. This array is being sorted in place…keeping the space at constant O(1).

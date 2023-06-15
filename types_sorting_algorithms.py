def bubble_sort(arr):
    count = 0
    need_iteration = 'true'
    while need_iteration == 'true':
        need_iteration = 'false'
        for i in range(len(arr)):
            for j in range(0, len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    need_iteration = 'true'
                    count +=1
    print("The number of permutations is", count)
 
libraryNum = [124,235,456,123,756,476,285,998,379,108] 
print("Initial array:", libraryNum) 
bubble_sort(libraryNum) 
print ("Sorted array:", libraryNum)

C language
#include <stdio.h>
#include <stdbool.h>
 
void bubbleSort(int arr[], int n) 
{ 
   int i, j; 
   int count = 0;
   bool needIteration = true;
   while(needIteration) {
       needIteration = false;
       for(i = 0; i < n-1; i++)
       {
           for(j = 0; j < n-i-1; j++)
           {
               if(arr[j] > arr[j+1])
               { 
                   int temp = arr[j]; 
                   arr[j] = arr[j+1]; 
                   arr[j+1] = temp; 
                   needIteration = true;
                   count++;
                }
            }
        }
    }
   printf("The number of permutations is %d. \n", count); 
} 
 
void showArray(int arr[], int size) 
{ 
    int i; 
    for(i=0; i < size; i++) 
        printf("%d ", arr[i]); 
    printf("\n"); 
}
 
int main()
{ 
    int libraryNum[] = {124,235,456,123,756,476,285,998,379,108}; 
    int n = sizeof(libraryNum)/sizeof(libraryNum[0]); 
 
    printf("Initial array: \n"); 
    showArray(libraryNum, n); 
    bubbleSort(libraryNum, n); 
    printf("Sorted array: \n"); 
    showArray(libraryNum, n); 
    return 0; 
}

JAVA language
public class SortingArray {
    static void bubbleSort(int arr[])
    {
        int count = 0;
        boolean needIteration = true;
        while(needIteration) {
            needIteration = false;
            int n = arr.length;
            for(int i = 0; i < n-1; i++)
                for(int j = 0; j < n-i-1; j++)
                    if(arr[j] > arr[j+1])
                    {
                        int temp = arr[j];
                        arr[j] = arr[j+1];
                        arr[j+1] = temp;
                        needIteration = true;
                        count++;
                    }
        }
        System.out.println("The number of permutations is " + count);
    }
 
    static void showArray(int[] arr)
    {
        for(int value : arr) System.out.print(value + " ");
        System.out.println();
    }
 
    public static void main(String []args) {
        int[] libraryNum = {124,235,456,123,756,476,285,998,379,108};
        System.out.println("Initial array");
        showArray(libraryNum);
        bubbleSort(libraryNum);
        System.out.println("Sorted array");
        showArray(libraryNum);
    }
}

JAVASCRIPT
function bubbleSort(arr) {
  let count = 0;
  let needIteration = true;
  while (needIteration) {
    needIteration = false;
 
    for (let i = 0; i < arr.length; i++) {
      for (let j = 0; j < arr.length - i - 1; j++) {
        if (arr[j] > arr[j + 1]) {
          const temp = arr[j + 1];
          arr[j + 1] = arr[j];
          arr[j] = temp;
          count += 1;
          needIteration = true;
        }
      }
    }
    return count;
  }
}
 
const initData = [124, 235, 456, 123, 756, 476, 285, 998, 379, 108];
console.log(`Initial array:`, initData);
const iterationsTestData = bubbleSort(initData);
console.log(`The number of permutations is: ${iterationsTestData}`, `\nSorted array:`, initData);



def insertion_sort(arr):
    count = 0
    for i in range(1, len(arr)):
        key_item = arr[i]
        j = i-1
        while j >= 0 and key_item < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            count +=1
        arr[j + 1] = key_item
    print("The number of permutations is", count)
 
library_num = [124,235,456,123,756,476,285,998,379,108]
print("Initial array:", library_num)
insertion_sort(library_num)
print ("Sorted array:", library_num)

C
#include <stdio.h>
 
void insertionSort(int arr[], int n) 
{ 
   int i, j, keyItem; 
   int count=0;
   for(i = 1; i < n; i++) 
   {
       keyItem = arr[i];
       j = i - 1;
       while(j >= 0 && arr[j] > keyItem)
       {
           arr[j + 1] = arr[j]; 
            j = j - 1;
            count ++;
       }
       arr[j + 1] = keyItem;
   }
   printf("The number of permutations is %d. \n", count); 
} 
 
void showArray(int arr[], int size) 
{ 
    int i; 
    for(i=0; i < size; i++) 
        printf("%d ", arr[i]); 
    printf("\n"); 
}
 
int main()
{ 
    int libraryNum[] = {124,235,456,123,756,476,285,998,379,108}; 
    int n = sizeof(libraryNum)/sizeof(libraryNum[0]); 
 
    printf("Initial array: \n"); 
    showArray(libraryNum, n); 
    insertionSort(libraryNum, n); 
    printf("Sorted array: \n"); 
    showArray(libraryNum, n); 
    return 0; 
}

JAVA
public class SortingArray {
    static void insertionSort(int arr[])
    {
        int count=0;
        int n = arr.length;
        for(int i = 1; i < n; i++) {
            int keyItem = arr[i];
            int j = i - 1;
            while(j >= 0 && arr[j] > keyItem) {
                arr[j + 1] = arr[j];
                j = j - 1;
                count++;
            }
            arr[j + 1] = keyItem;
        }
        System.out.println("The number of permutations is " + count);
    }
 
    static void showArray(int[] arr)
    {
        for(int value : arr) System.out.print(value + " ");
        System.out.println();
    }
 
    public static void main(String []args) {
        int[] libraryNum = {124,235,456,123,756,476,285,998,379,108};
        System.out.println("Initial array");
        showArray(libraryNum);
        insertionSort(libraryNum);
        System.out.println("Sorted array");
        showArray(libraryNum);
    }
}

JAVASCRIPT
function insertionSort(arr) {
  let count = 0;
 
  for (let i = 1; i < arr.length; i++) {
    const keyItem = arr[i];
    let j = i - 1;
 
    while (j >= 0 && keyItem < arr[j]) {
      const temp = arr[j + 1];
      arr[j + 1] = arr[j];
      arr[j] = temp;
      count += 1;
      j--;
    }
  }
 return count;
}
 
const initData = [124, 235, 456, 123, 756, 476, 285, 998, 379, 108];
console.log(`Initial array:`, initData);
const iterationsTestData = insertionSort(initData);
console.log(`The number of permutations is: ${iterationsTestData}`, `\nSorted array:`, initData);


def selection_sort(arr):    
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[min] > arr[j]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
 
library_num = [124,235,456,123,756,476,285,998,379,108]
print("Initial array:", library_num)
selection_sort(library_num)
print ("Sorted array:", library_num)

C
#include <stdio.h>
 
void selectionSort(int arr[], int n) 
{ 
   int i, j, min; 
   int count=0;
   for(i = 0; i < n-1; i++) 
   {
       min = i;
       for(j = i+1; j < n; j++)
       {
           if(arr[j] < arr[min])
           { 
              min = j;
           }    
        }
        int temp = arr[min]; 
        arr[min] = arr[i]; 
        arr[i] = temp; 
        count++;      
   }
   printf("The number of permutations is %d. \n", count); 
} 
 
void showArray(int arr[], int size) 
{ 
    int i; 
    for(i=0; i < size; i++) 
        printf("%d ", arr[i]); 
    printf("\n"); 
}
 
int main()
{ 
    int libraryNum[] = {124,235,456,123,756,476,285,998,379,108}; 
    int n = sizeof(libraryNum)/sizeof(libraryNum[0]); 
 
    printf("Initial array: \n"); 
    showArray(libraryNum, n); 
    selectionSort(libraryNum, n); 
    printf("Sorted array: \n"); 
    showArray(libraryNum, n); 
    return 0; 
}

JAVA
public class SortingArray {
    static void selectionSort(int arr[])
    {
        int count=0;
        int n = arr.length;
        for(int i = 0; i < n-1; i++)
        {
            int min = i;
            for(int j = i+1; j < n; j++)
                if(arr[j] < arr[min])
                    min = j;
            int temp = arr[min];
            arr[min] = arr[i];
            arr[i] = temp;
            count++;
        }
        System.out.println("The number of permutations is " + count);
    }
 
    static void showArray(int[] arr)
    {
        for(int value : arr) System.out.print(value + " ");
        System.out.println();
    }
 
    public static void main(String []args) {
        int[] libraryNum = {124,235,456,123,756,476,285,998,379,108};
        System.out.println("Initial array");
        showArray(libraryNum);
        selectionSort(libraryNum);
        System.out.println("Sorted array");
        showArray(libraryNum);
    }
}

JAVASCRIPT
function selectionSort(arr) {
  for (let i = 0; i < arr.length; i++) {
    let min = i;
 
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[min] > arr[j]) {
        min = j;
      }
    }
 
    const temp = arr[min];
    arr[min] = arr[i];
    arr[i] = temp;
  }
}
 
const initData = [124, 235, 456, 123, 756, 476, 285, 998, 379, 108];
console.log(`Initial array:`, initData);
selectionSort(initData);
console.log(`Sorted array:`, initData);


def heapify(arr, n, i):
      largest = i
      left = 2 * i + 1
      right = 2 * i + 2
 
      if left < n and arr[i] < arr[left]:
          largest = left
 
      if right < n and arr[largest] < arr[right]:
          largest = right
 
      if largest != i:
          arr[i], arr[largest] = arr[largest], arr[i]
          heapify(arr, n, largest)
 
def heap_sort(arr):    
    for i in range(len(arr)//2,-1,-1):
        heapify(arr, len(arr), i)
    for i in range(len(arr)-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
 
library_num = [124,235,456,123,756,476,285,998,379,108]
print("Initial array:", library_num)
heap_sort(library_num)
print ("Sorted array:", library_num)

C
#include <stdio.h>
 
 // Write a recursion function to find largest among root, left child, and right child
void heapify(int arr[], int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;
 
    if (left < n && arr[left] > arr[largest])
      largest = left;
 
    if (right < n && arr[right] > arr[largest])
      largest = right;
 
    if (largest != i) {// Swap and continue heapifying if root is not largest
        int temp = arr[i];
        arr[i] = arr[largest];
        arr[largest] = temp;
        heapify(arr, n, largest);
    }
  }
 
  void heapSort(int arr[], int n) {
    for (int i = n / 2 - 1; i >= 0; i--)// Build max heap
        heapify(arr, n, i);
    for (int i = n - 1; i >= 0; i--) {// Heap sort
        int temp = arr[0];
        arr[0] = arr[i];
        arr[i] = temp;
        heapify(arr, i, 0);// Heapify root element to get highest element at root again
    }
  }
 
void showArray(int arr[], int size) 
{ 
    int i; 
    for (i=0; i < size; i++) 
        printf("%d ", arr[i]); 
    printf("\n"); 
}
 
int main()
{ 
    int libraryNum[] = {124,235,456,123,756,476,285,998,379,108}; 
    int n = sizeof(libraryNum)/sizeof(libraryNum[0]); 
 
    printf("Initial array: \n"); 
    showArray(libraryNum, n); 
    heapSort(libraryNum, n); 
    printf("Sorted array: \n"); 
    showArray(libraryNum, n); 
    return 0; 
}

JAVA
public class SortingArray {
 
public static void heapSort(int arr[]) {
        int n = arr.length;
 
        for (int i = n / 2 - 1; i >= 0; i--) {// Build max heap
            heapify(arr, n, i);
        }
 
        for (int i = n - 1; i >= 0; i--) { // Heap sort
            int temp = arr[0];
            arr[0] = arr[i];
            arr[i] = temp;
            heapify(arr, i, 0);// Heapify root element to get highest element at root again
        }
    }
 
    static void heapify(int arr[], int n, int i) {
        int largest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;
 
        if (left < n && arr[left] > arr[largest])
            largest = left;
 
        if (right < n && arr[right] > arr[largest])
            largest = right;
 
        // Swap and continue heapifying if root is not largest
        if (largest != i) {
            int temp = arr[i];
            arr[i] = arr[largest];
            arr[largest] = temp;
            heapify(arr, n, largest);
        }
    }
    static void showArray(int[] arr)
    {
        for (int value : arr) System.out.print(value + " ");
        System.out.println();
    }
 
public static void main(String []args) {
        int[] libraryNum = {124,235,456,123,756,476,285,998,379,108};
        System.out.println("Initial array");
        showArray(libraryNum);
        heapSort(libraryNum);
        System.out.println("Sorted array");
        showArray(libraryNum);
    }
}

JAVASCRIPT
function heapify(arr, n, i) {
  let largest = i;
  let left = 2 * i + 1;
  let right = 2 * i + 2;
 
  if (left < n && arr[i] < arr[left]) {
    largest = left;
  }
 
  if (right < n && arr[largest] < arr[right]) {
    largest = right;
  }
 
  if (largest != i) {
    const temp = arr[largest];
    arr[largest] = arr[i];
    arr[i] = temp;
 
    heapify(arr, n, largest);
  }
}
 
function heapSort(arr) {
  for (let i = Math.floor(arr.length / 2); i >= 0; i--) {
    heapify(arr, arr.length, i);
  }
 
  for (let i = arr.length - 1; i >= 1; i--) {
    const temp = arr[0];
    arr[0] = arr[i];
    arr[i] = temp;
 
    heapify(arr, i, 0);
  }
}
 
const initData = [124, 235, 456, 123, 756, 476, 285, 998, 379, 108];
console.log(`Initial array:`, initData);
heapSort(initData);
console.log(`Sorted array:`, initData);


def merge_sort(arr):
    if len(arr) > 1:
        mean = len(arr)//2
        left_arr = arr[:mean]
        right_arr = arr[mean:]
        merge_sort(left_arr)
        merge_sort(right_arr)
 
        i = j = k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
 
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1    
 
library_num = [124,235,456,123,756,476,285,998,379,108]
print("Initial array:", library_num)
merge_sort(library_num)
print ("Sorted array:", library_num)


C
#include <stdio.h>
 
 void merge(int items[], int left, int mean, int right) {
    int leftSize = mean - left + 1;
    int rightSize = right - mean;
    int leftArr[leftSize], rightArr[rightSize];
    for (int i = 0; i < leftSize; i++)
        leftArr[i] = items[left + i];
    for (int j = 0; j < rightSize; j++)
        rightArr[j] = items[mean + 1 + j];
 
  // Maintain current index of sub-arrays and main array
  int i = 0;
  int j = 0;
  int k = left;
 
  // Until we reach the end of either leftArr or rightArr, pick larger among
  // elements leftArr and rightArr and place them in the correct position at items[left..right]
  while(i < leftSize && j < rightSize) {
    if (leftArr[i] <= rightArr[j]) {
        items[k] = leftArr[i];
        i++;
        } else {
            items[k] = rightArr[j];
            j++;
            }
    k++;
  }
  while (i < leftSize) {
    items[k] = leftArr[i];
    i++;
    k++;
    }
    while (j < rightSize) {
        items[k] = rightArr[j];
        j++;
        k++;
        }
}
 
// Divide the array into two subarrays, sort them and merge them
void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        int mean  = left + (right - left) / 2;
        mergeSort(arr, left, mean );
        mergeSort(arr, mean  + 1, right);
        merge(arr, left, mean , right);
        }
}
 
void showArray(int arr[], int size) 
{ 
    int i; 
    for (i=0; i < size; i++) 
        printf("%d ", arr[i]); 
    printf("\n"); 
}
 
int main()
{ 
    int libraryNum[] = {124,235,456,123,756,476,285,998,379,108}; 
    int n = sizeof(libraryNum)/sizeof(libraryNum[0]); 
 
    printf("Initial array: \n"); 
    showArray(libraryNum, n); 
    mergeSort(libraryNum, 0, n-1); 
    printf("Sorted array: \n"); 
    showArray(libraryNum, n); 
    return 0; 
}

JAVA
public class SortingArray {
 
    public static void mergeSort(int[] arr, int left, int right)
    {
        if (left < right) {
            int mean = (left + right) / 2;
            mergeSort(arr, left, mean);
            mergeSort(arr, mean+1, right);
            merge(arr, left, mean, right);
        }
    }
 
    private static void merge(int[] items, int left, int mean, int right)
    {
        int leftSize = mean - left + 1;
        int rightSize = right - mean;
        int[] leftArr = new int[leftSize];
        int[] rightArr = new int[rightSize];
        for (int i = 0; i < leftSize; i++)
            leftArr[i] = items[left + i];
        for (int j = 0; j < rightSize; j++)
            rightArr[j] = items[mean + 1 + j];
 
        // Maintain current index of sub-arrays and main array
        int i = 0;
        int j = 0;
        int k = left;
 
        // Until we reach the end of either leftArr or rightArr, pick larger among
        // elements leftArr and rightArr and place them in the correct position at  
        //items[left..right]
        while(i < leftSize && j < rightSize)
        {
            if (leftArr[i] <= rightArr[j]) {
                items[k] = leftArr[i];
                i++;
            } else {
                items[k] = rightArr[j];
                j++;
            }
            k++;
        }
        while (i < leftSize) {
            items[k] = leftArr[i];
            i++;
            k++;
        }
 
        while (j < rightSize) {
            items[k] = rightArr[j];
            j++;
            k++;
        }
    }
 
    static void showArray(int[] arr)
    {
        for (int value : arr) System.out.print(value + " ");
        System.out.println();
    }
 
    public static void main(String []args) {
        int[] libraryNum = {124,235,456,123,756,476,285,998,379,108};
        System.out.println("Initial array");
        showArray(libraryNum);
        mergeSort(libraryNum, 0, libraryNum.length - 1);
        System.out.println("Sorted array");
        showArray(libraryNum);
    }
}

JAVASCRIPT
function mergeSort(arr) {
  if (arr.length > 1) {
    const mean = Math.floor(arr.length / 2);
    const leftArr = arr.slice(0, mean);
    const rightArr = arr.slice(mean, arr.length);
 
    mergeSort(leftArr);
    mergeSort(rightArr);
 
    let i = 0;
    let j = 0;
    let k = 0;
 
    while (i < leftArr.length && j < rightArr.length) {
      if (leftArr[i] < rightArr[j]) {
        arr[k] = leftArr[i];
        i += 1;
      } else {
        arr[k] = rightArr[j];
        j += 1;
      }
 
      k += 1;
    }
 
    while (i < leftArr.length) {
      arr[k] = leftArr[i];
      i += 1;
      k += 1;
    }
 
    while (j < rightArr.length) {
      arr[k] = rightArr[j];
      j += 1;
      k += 1;
    }
  }
}
 
const initData = [124, 235, 456, 123, 756, 476, 285, 998, 379, 108];
console.log(`Initial array:`, initData);
mergeSort(initData);
console.log(`Sorted array:`, initData);

Quicksort sort Python
def partition(arr,left,right): 
    i = ( left-1 )      # index of smaller element 
    key = arr[right]    # a key element 
 
    for j in range(left, right): 
        if   arr[j] < key:  
            i += 1 
            arr[i],arr[j] = arr[j],arr[i]  
    arr[i + 1],arr[right] = arr[right],arr[i + 1] 
    return ( i+1 )
 
def quick_sort(arr,left,right):
    if left < right:
        key_index = partition(arr,left,right)
        quick_sort(arr,left,key_index - 1)
        quick_sort(arr,key_index + 1, right)        
 
library_num = [124,235,456,123,756,476,285,998,379,108]
print("Initial array:", library_num)
quick_sort(library_num, 0, len(library_num) - 1)
print ("Sorted array:", library_num)

C
#include <stdio.h>
 
 int partition(int items[], int left, int right) {
    int key = items[right];
    int i = left - 1;
        for (int j = left; j < right; j++) {
            if (items[j] <= key) {
                i++;
                int temp = items[i];
                items[i] = items[j];
                items[j] = temp;
            }
        }
        int temp = items[i + 1];
        items[i + 1] = items[right];
        items[right] = temp;
        return (i + 1);
}
 
void quickSort(int arr[], int left, int right) {
    if (left < right) {
        int keyIndex = partition(arr, left, right);
        quickSort(arr, left, keyIndex - 1);// Sort the elements on the left of a key element
        quickSort(arr, keyIndex + 1, right);// Sort the elements on the right of a key element
        }
}
 
void showArray(int arr[], int size) 
{ 
    int i; 
    for (i=0; i < size; i++) 
        printf("%d ", arr[i]); 
    printf("\n"); 
}
 
int main()
{ 
    int libraryNum[] = {124,235,456,123,756,476,285,998,379,108}; 
    int n = sizeof(libraryNum)/sizeof(libraryNum[0]); 
 
    printf("Initial array: \n"); 
    showArray(libraryNum, n); 
    quickSort(libraryNum, 0, n-1); 
    printf("Sorted array: \n"); 
    showArray(libraryNum, n); 
    return 0; 
}



JAVA
public class SortingArray {
 
    public static void quickSort(int[] arr, int left, int right)
    {
        if (left < right) {
            int keyIndex = partition(arr, left, right);
            quickSort(arr, left, keyIndex - 1);// Sort the elements on the left of a key element
            quickSort(arr, keyIndex + 1, right);// Sort the elements on the right of a key element
        }
    }
 
    private static int partition(int[] items, int left, int right)
    {
        int key = items[right];
        int i = left - 1;
        for (int j = left; j < right; j++) {
            if (items[j] <= key) {
                i++;
                int temp = items[i];
                items[i] = items[j];
                items[j] = temp;
            }
        }
        int temp = items[i + 1];
        items[i + 1] = items[right];
        items[right] = temp;
        return (i + 1);
    }
 
    static void showArray(int[] arr)
    {
        for (int value : arr) System.out.print(value + " ");
        System.out.println();
    }
 
    public static void main(String []args) {
        int[] libraryNum = {124,235,456,123,756,476,285,998,379,108};
        System.out.println("Initial array");
        showArray(libraryNum);
        quickSort(libraryNum, 0, libraryNum.length - 1);
        System.out.println("Sorted array");
        showArray(libraryNum);
    }
}

JAVASCRIPT
function partition(arr, left, right) {
  let i = left - 1;
  let key = arr[right];
 
  for (let j = left; j <= right; j++) {
    if (arr[j] < key) {
      i += 1;
 
      const temp = arr[j];
      arr[j] = arr[i];
      arr[i] = temp;
    }
  }
 
  const temp = arr[right];
  arr[right] = arr[i + 1];
  arr[i + 1] = temp;
  return i + 1;
}
 
function quickSort(arr, left, right) {
  if (left < right) {
    const keyIndex = partition(arr, left, right);
    quickSort(arr, left, keyIndex - 1);
    quickSort(arr, keyIndex + 1, right);
  }
}
 
const initData = [124, 235, 456, 123, 756, 476, 285, 998, 379, 108];
console.log('Initial array:', initData);
quickSort(initData, 0, initData.length-1);
console.log(`Sorted array:`, initData);


Radix sort Python
def counting_sort(arr, place):
    size = len(arr)
    output = [0] * size
    count = [0] * 10
 
    # Determine count of elements
    for i in range(0, size):
        index = arr[i] // place
        count[index % 10] += 1
 
    # Determine cummulative count
    for i in range(1, 10):
        count[i] += count[i - 1]
 
    # Place the elements in the correct place
    i = size - 1
    while i >= 0:
        index = arr[i] // place
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
 
    for i in range(0, size):
        arr[i] = output[i]
 
def radix_sort(arr):
    max_item = max(arr)
    place = 1
    while max_item // place > 0:
        counting_sort(arr, place)
        place *= 10
 
library_num = [124,235,456,123,756,476,285,998,379,108]
print("Initial array:", library_num)
radix_sort(library_num)
print ("Sorted array:", library_num)

C
#include <stdio.h>
 
int findMax(int arr[], int size) {
  int maxItem = arr[0];
  for (int i = 1; i < size; i++)
    if (arr[i] > maxItem)
      maxItem = arr[i];
  return maxItem;
}
 
void countingSort(int arr[], int size, int place) {
  int output[size + 1];
  int maxItem = (arr[0] / place) % 10;
 
  for (int i = 1; i < size; i++) {
    if (((arr[i] / place) % 10) > maxItem)
      maxItem = arr[i];
  }
  int count[maxItem + 1];
 
  for (int i = 0; i < maxItem; ++i)
    count[i] = 0;
 
  // Determine count of elements
  for (int i = 0; i < size; i++)
    count[(arr[i] / place) % 10]++;
 
  // Determine cummulative count
  for (int i = 1; i < 10; i++)
    count[i] += count[i - 1];
 
  // Place the elements in the correct place
  for (int i = size - 1; i >= 0; i--) {
    output[count[(arr[i] / place) % 10] - 1] = arr[i];
    count[(arr[i] / place) % 10]--;
  }
 
  for (int i = 0; i < size; i++)
    arr[i] = output[i];
}
 
void radixSort(int arr[], int size) {
  int maxItrm = findMax(arr, size);
  for (int place = 1; maxItrm / place > 0; place *= 10)
    countingSort(arr, size, place);
}
 
void showArray(int arr[], int size) 
{ 
    int i; 
    for (i=0; i < size; i++) 
        printf("%d ", arr[i]); 
    printf("\n"); 
}
 
int main()
{ 
    int libraryNum[] = {124,235,456,123,756,476,285,998,379,108}; 
    int n = sizeof(libraryNum)/sizeof(libraryNum[0]); 
 
    printf("Initial array: \n"); 
    showArray(libraryNum, n); 
    radixSort(libraryNum, n); 
    printf("Sorted array: \n"); 
    showArray(libraryNum, n); 
    return 0; 
}


JAVA
public class SortingArray {
    static int findMax(int[] arr)
    {
        int maxItem = arr[0];
        for (int i = 1; i < arr.length; i++)
            if (arr[i] > maxItem)
                maxItem = arr[i];
        return maxItem;
    }
 
    static void countingSort(int[] arr, int place) {
        int size = arr.length;
        int[] output = new int[size + 1];
        int maxItem = findMax(arr);
 
        int[] count = new int[maxItem + 1];
        for (int i = 0; i < maxItem; ++i)
            count[i] = 0;
 
        // Determine count of elements
        for (int i = 0; i < size; i++)
            count[(arr[i] / place) % 10]++;
 
        // Determine cummulative count
        for (int i = 1; i < 10; i++)
            count[i] += count[i - 1];
 
        // Place the elements in the correct place
        for (int i = size - 1; i >= 0; i--) {
            output[count[(arr[i] / place) % 10] - 1] = arr[i];
            count[(arr[i] / place) % 10]--;
        }
        for (int i = 0; i < size; i++)
            arr[i] = output[i];
    }
 
    // Main function to implement radix sort
    static void radixSort(int[] arr) {
        int max = findMax(arr);
 
        // Apply counting sort to sort elements based on place value.
        for (int place = 1; max / place > 0; place *= 10)
            countingSort(arr, place);
    }
 
    static void showArray(int[] arr)
    {
        for (int value : arr) System.out.print(value + " ");
        System.out.println();
    }
 
    public static void main(String []args) {
        int[] libraryNum = {124,235,456,123,756,476,285,998,379,108};
        System.out.println("Initial array");
        showArray(libraryNum);
        radixSort(libraryNum);
        System.out.println("Sorted array");
        showArray(libraryNum);
    }
}

JAVASCRIPT
function countingSort(arr, place) {
  const output = new Array(arr.length).fill(0);
  const count = new Array(10).fill(0);
 
  for (let i = 0; i < arr.length; i++) {
    count[Math.floor(arr[i] / place) % 10] += 1;
  }
 
  for (let i = 1; i <= 10; i++) {
    count[i] += count[i - 1];
  }
 
  let i = arr.length - 1;
 
  while (i >= 0) {
    const index = Math.floor(arr[i] / place) % 10;
    output[count[index] - 1] = arr[i];
    count[index] -= 1;
 
    i -= 1;
  }
 
  for (let i = 0; i < arr.length; i++) {
    arr[i] = output[i];
  }
}
 
function radixSort(arr) {
  const max = Math.max(...arr);
  let place = 1;
 
  while (Math.floor(max / place) > 0) {
    countingSort(arr, place);
    place *= 10;
  }
}
 
const initData = [124, 235, 456, 123, 756, 476, 285, 998, 379, 108];
console.log(`Initial array:`, initData);
radixSort(initData);
console.log(`Sorted array:`, initData);


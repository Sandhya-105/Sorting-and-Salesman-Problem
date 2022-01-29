import time
        
def mergeSort(arr):
    if len(arr) > 1:
  
         # Finding the mid of the array
        mid = len(arr)//2
  
        # Dividing the array elements
        L = arr[:mid]
  
        # into 2 halves
        R = arr[mid:]
  
        # Sorting the first half
        mergeSort(L)
  
        # Sorting the second half
        mergeSort(R)
  
        i = j = k = 0
  
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
  
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def main():
    with open("file.txt", mode = 'r') as file:
        array = [float(line) for line in file]
    start = time.time()
    mergeSort(array)
    end = time.time()
    print(end - start)
    '''with open("unfile.txt", mode = 'w') as out_file:
        for arr in array:
          out_file.write(str(arr) + "\n")'''
    
if __name__ == "__main__":
    main()
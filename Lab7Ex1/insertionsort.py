import time
   
def insertionSort(array):
    for i in range(1, len(array)):
        k = array[i] 
        # insert a[i] into sorted sequence a[1..i-1]
        j = i-1
        #print("i = ", i) 
        #print("k = ", k) 
        #print("j = ", j) 
        while j>=0 and array[j]>k: 
            # move a[j] one position to the right
            #print("entering while")
            array[j+1] = array[j]
            j = j-1
        array[j+1] = k 
        #print("-----")

def main():
    with open("file.txt", mode = 'r') as file:
        array = [float(line) for line in file]
    start = time.time()
    insertionSort(array)# Chunk of code you want to measure
    end = time.time()
    print(end - start)
    '''with open("unfile.txt", mode = 'w') as out_file:
        for pt in array:
            out_file.write(str(pt)+"\n")'''
    

if __name__ == "__main__":
    main()
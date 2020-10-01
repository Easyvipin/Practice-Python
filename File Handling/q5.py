def insertion_desc(arr): 
	for i in range(1, len(arr)): 
		key = arr[i]  
		j = i-1
		while j >= 0 and key > arr[j] : 
				arr[j + 1] = arr[j] 
				j -= 1
		arr[j + 1] = key 


 
arr = [14,15,9,1,7,10] 
insertion_desc(arr) 
print(arr)

def binary_search(arr,target):
  low=0
  high=len(arr)-1
  
  while(low<=high):
    mid=(left+right)//2
    
    if arr[mid]==target:
      return mid
    
    elif arr[mid]<target:
      low=mid+1
    else:
      high=mid-1
      return -1
      
      #example
      arr=input("enter the sorted elements").split()
      arr=[int(num) for num in arr]
      target=int(input("enter the sorted element"))
      result= binary_search(arr,target)
      
      if result != -1:
        
        print("element are the found")
      else:
        
                print("not found")
           

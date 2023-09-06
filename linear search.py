#Author : ShankRoy

def linearsearch(arr, x):
   return next((i for i in range(len(arr)) if arr[i] == x), -1)
arr = ['t','u','t','o','r','i','a','l']
x = 'a'
print(f"element found at index {str(linearsearch(arr, x))}")

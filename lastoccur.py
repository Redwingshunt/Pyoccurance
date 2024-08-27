
def Lastoccurance(l:list, n:int)->int:
    low=0
    high=len(l)-1
    while low<=high:
        mid=(low+high)//2
        if (l[mid]<n):
            low =mid+1
        elif (l[mid]>n):
            high =mid-1
        else:
            if mid==len(l)-1 or l[mid]!=l[mid+1]:
                return mid
            else:
                low = mid+1




l =[1, 23, 35, 56, 67, 87, 87, 87, 98, 192, 243]
n= 87

print(Lastoccurance(l,n))
``

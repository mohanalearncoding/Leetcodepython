def max_sub_array_of_size_k(k, arr):
    maximum=0
    sum=0
    startingelement=0
    counter=0
    for i in range(len(arr)):
        sum+=arr[i]
        counter+=1
        if counter==k:
            maximum=max(maximum,sum)
            counter=k-1
            sum=sum-arr[startingelement]
            startingelement=startingelement+1
    return maximum
print(max_sub_array_of_size_k(2,[2, 3, 4, 1, 5]))
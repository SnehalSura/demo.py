def sort(nums):
    for i in range(5):
        minp = i;
        for j in range(i,6):
            if nums[j]<nums[minp]:
                minp = j;
        temp = nums[i]
        nums[i] = nums[minp]
        nums[minp] = temp
        
        print(nums)
nums = [5,2,6,8,7,4]
sort(nums)
print(nums)

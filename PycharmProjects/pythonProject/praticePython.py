def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    result = []
    for i in range(len(nums)):
        # if len(result)!=0:
        #     break
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                result.append(i)
                result.append(j)
                break
    return result


#print(twoSum([2, 7, 11, 15], 9))
def solution(number):
    if number<0:
        return 0
    else:
        list1=[i  for i in range(0,number,3)]
        list2=[j  for j in range(0,number,5)]
        for i in list2:
            if i not in list1:
                list1.append(i)
        sum=0
        for i in list1:
            sum=sum+i
        return sum

def filter_list(l):
    'return a new list with the strings filtered out'
    # new_list=[]
    # for i in l:
    #     if isinstance(i,int) and i>0:
    #         new_list.append(i)
    return [i for i in l if isinstance(i,int) and i>0]



print(filter_list([1,2,'a','b']))
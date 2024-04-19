class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        sum = 0
        arr=[]
        while numbers[left] + numbers[right] != target:
            sum =  numbers[left] + numbers[right]
            if  sum < target:
                left +=1
            elif sum > target:
                right -=1
        arr.append(left+1), arr.append(right+1)

        return arr

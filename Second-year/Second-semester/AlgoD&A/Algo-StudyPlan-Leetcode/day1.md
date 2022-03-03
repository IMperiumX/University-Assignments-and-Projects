# Algorithm Study Plan [link](https://leetcode.com/study-plan/algorithm/?progress=d8qn2ze)

In mathematics and computer science, an algorithm is defined as a process or set of rules to be followed in calculations or other problem-solving operations. This practical method is often used in calculations, data processing, and automatic reasoning because it contains clear and concise instructions and can be executed in limited time and space complexities.

## Day 1 Binary Search

##

[704. Binary Search](https://leetcode.com/problems/binary-search/)

**Example:**

```
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
```

```python
import bisect

def search(nums, target):
    index = bisect.bisect_left(nums, target)
    return index if index < len(nums) and nums[index] == target else -1
```

##

```python
def search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        else:
            return mid
    return -1
```

##

[278. First Bad Version](https://leetcode.com/problems/first-bad-version/submissions/)


You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions `[1, 2, ..., n]` and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool `isBadVersion(version)` which returns whether `version` is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.


**Example:**

```
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
```

```python

def firstBadVersion(n) -> int:
    left, right = 1, n
    while left < right:
        mid = left + (right - left) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    return left
```
##

```python
def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    left, right = 0, len(array)
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left
```

##

[35. Search Insert Position](https://leetcode.com/problems/search-insert-position/)

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

**Example 1:**

```
Input: nums = [1,3,5,6], target = 5
Output: 2
```

**Example 2:**

```
Input: nums = [1,3,5,6], target = 2
Output: 1
```

**Binary Search By Hand**


```python
def searchInsert(nums: List[int], target: int) -> int:
    low, high = 0, len(nums)
    while low < high:
        mid = (low + high) // 2
        if target > nums[mid]:
            low = mid + 1
        else:
            high = mid
    return low
```

##


**Using bisect module**

```python
import bisect

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)
```

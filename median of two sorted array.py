class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        total_len = len(nums1) + len(nums2)
        if total_len % 2 == 0:
            return (self.findKth(nums1,nums2,total_len/2) + self.findKth(nums1,nums2,total_len/2+1))/2.0
        else:
            return self.findKth(nums1,nums2,(total_len+1)/2)
        
            
    def findKth(self,nums1,nums2,k):
        #print nums1,nums2,k
        if not nums1:
            return nums2[k-1]
        if not nums2:
            return nums1[k-1]
        if len(nums1) > len(nums2):
            return self.findKth(nums2,nums1,k)
        if k == 1:
            return min(nums1[0],nums2[0])
        mid1 = (len(nums1)+1) / 2
        mid2 = k - mid1
        if nums1[mid1-1] > nums2[mid2-1]:
            return self.findKth(nums1[:mid1],nums2[mid2:],mid1)
        else:
            return self.findKth(nums1[mid1:],nums2[:mid2],mid2)
        
sol = Solution()
print sol.findMedianSortedArrays([1,2],[1,2])
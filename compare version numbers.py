class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        nums1 = version1.split('.')
        nums2 = version2.split('.')
        i = 0
        while i < min(len(nums1),len(nums2)):
            if int(nums1[i]) < int(nums2[i]):
                return -1
            elif int(nums1[i]) > int(nums2[i]):
                return 1
            i += 1
        if len(nums1) == len(nums2):
            return 0
        elif len(nums1) > len(nums2):
            while i < len(nums1):
                if int(nums1[i]) > 0:
                    return 1
                i += 1
        else:
            while i < len(nums2):
                if int(nums2[i]) > 0:
                    return -1
                i += 1
        return 0
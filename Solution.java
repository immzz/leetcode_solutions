public class Solution {
    public int[] twoSum(int[] numbers, int target) {
        Map<Integer,Integer> map = new HashMap<Integer,Integer>();
        for(int i=0;i<numbers.length;i++){
            if(map.containsKey(target - numbers[i])){
                return new int[]{Math.min(i,map.get(target))+1,Math.max(i,map.get(target))+1};
            }
            map.put(numbers[i],i);
        }
        return null;
    }
}
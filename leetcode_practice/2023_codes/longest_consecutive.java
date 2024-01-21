class Solution {
    public int longestConsecutive(int[] nums) {
        if(null == nums || nums.length == 0){
            return 0;
        }
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for(int i = 0;i<nums.length;i++){
            map.put(nums[i],1);
        }
        int max_so_far = 1;
        Map<Integer, Integer> map2 = new HashMap<Integer, Integer>();
        for(int i = 0;i<nums.length;i++){
            int start = nums[i]+1;
            int count = 1;
            while(map.containsKey(start)){
                count = count + map.get(start);
                map.put(nums[i], count);
                map.remove(start);
                start++;
            }
            max_so_far = Math.max(max_so_far, count);
        }
        return max_so_far;
    }
}
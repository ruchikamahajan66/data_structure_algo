class Solution {
    public int smallestSubstring(String str) {
        // Code here
        int count = 0, j=0, min_so_far = Integer.MAX_VALUE;
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        for(int i=0;i<str.length();i++){
            count = count+1;
            if(!map.containsKey(str.charAt(i))){
                map.put(str.charAt(i), 1);
            }else{
                map.put(str.charAt(i), map.get(str.charAt(i))+1);
            }
            if(map.size()==3){
                if(count<min_so_far){
                    min_so_far=count;
                }
            }
            while(map.size()==3){
                 if(map.get(str.charAt(j)) == 1){
                    map.remove(str.charAt(j));
                }else{
                    map.put(str.charAt(j), map.get(str.charAt(j))-1);
                }
                count--;
                j++;
                if(map.size()==3){
                    if(count<min_so_far){
                        min_so_far=count;
                    }
                }
            }
    }
    return min_so_far == Integer.MAX_VALUE ? -1 : min_so_far;
}
    
}

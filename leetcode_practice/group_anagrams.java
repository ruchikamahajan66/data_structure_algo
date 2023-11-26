class Solution {

    public List<List<String>> groupAnagrams(String[] strs) {
        if(null == strs || strs.length == 0){
            return new ArrayList<>();
        }
        Map<String, List<String>> map = new HashMap<String,  List<String>>();

        for(int i =0;i<strs.length;i++){
            char[] ca = strs[i].toCharArray();
            Arrays.sort(ca);
            String keyStr = String.valueOf(ca);
            if(!map.containsKey(keyStr)){
                map.put(keyStr, new ArrayList<>());
            }
            map.get(keyStr).add(strs[i]);
        }
        return new ArrayList<>(map.values());
    }
}
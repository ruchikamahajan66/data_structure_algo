class Compute {
    public String isSubset( long a1[], long a2[], long n, long m) {
        //your code here 
        HashMap<Long, Integer> map = new HashMap<Long, Integer>();
        for(int i =0; i<n;i++){
            if (!map.containsKey(a1[i])){
                map.put(a1[i],1);
            }else{
                map.put(a1[i],map.get(a1[i])+1);
                }
             //System.out.println(map);
        }
        for (int i = 0; i < m; i++) {
            if (!map.containsKey(a2[i])){
                return "No";
            }else{
                if(map.get(a2[i]) == 1){
                    map.remove(a2[i]);
                }
                else{
                map.put(a2[i],map.get(a2[i])-1);
                }
            }
        }
        return "Yes";
    }
}

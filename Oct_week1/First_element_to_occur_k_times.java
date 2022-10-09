class Solution
{
    public int firstElementKTime(int[] A, int n, int k) { 
        Map<Integer,Integer> map = new HashMap<>();
        for (int i =0; i<n;i++){
            if(map.containsKey(A[i])){
                map.put(A[i],map.get(A[i])+1);
            }else{
                map.put(A[i],1);
            }
            if (map.get(A[i]) == k){
                    return A[i];
                }
            
        }
        return -1;
        
    } 
}

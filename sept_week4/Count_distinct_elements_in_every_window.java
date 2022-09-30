class Solution
{
    ArrayList<Integer> countDistinct(int A[], int n, int k)
    {
        // code here 
        ArrayList<Integer> res =new ArrayList<Integer>();
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for(int i=0;i<k;i++){
            if(!map.containsKey(A[i])){
                map.put(A[i],1);   
            }
            else{
                map.put(A[i],map.get(A[i])+1);
            }
        }
        res.add(map.size());

        for(int i=k;i<n;i++){
            if(!map.containsKey(A[i])){
                map.put(A[i],1);   
            }
            else{
                map.put(A[i],map.get(A[i])+1);
            }
            if(map.get(A[i-k])==1){
                map.remove(A[i-k]);
            }
            else{
                map.put(A[i-k],map.get(A[i-k])-1);
            }
            res.add(map.size());
        }
        return res;
        
    }
}

class Solution {
    public pair[] allPairs( long A[], long B[], long N, long M, long X) {
        // Your code goes here 
        HashMap<Long, Integer> map = new HashMap<Long, Integer>();
        ArrayList<pair> res =new ArrayList<pair>();
        for(int i =0; i<N;i++){
            if (!map.containsKey(A[i])){
                map.put(A[i],0);
            }
            else{
                map.put(A[i],1);
            }
        }
        for(int j =0; j<M;j++){
            if (map.containsKey(X-B[j])){
                res.add(new pair(X-B[j], B[j]));
                // System.out.printf("%f%n", (X-B[j]),B[j]);
            }
        }
        // Collections.sort(res,
        // (pair1, pair2)-> Long.compare(pair1.first,pair2.first));
    return res.toArray(new pair[]{});
    }
}

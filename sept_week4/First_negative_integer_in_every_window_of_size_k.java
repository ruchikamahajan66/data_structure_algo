class Compute {
    
    public long[] printFirstNegativeInteger(long A[], int n, int k)
    {
        Queue<Integer> q = new LinkedList<>();
        long[] res = new long[n-k+1];
        int j =0;
        for(int i=0;i<k;i++){
            if(A[i]<0){
                q.add(i);
            }
        }
        if(q.isEmpty()){
                res[j] =0;
        }else{
            res[j]=A[q.peek()];
        }
        j++;
        
        for(int i=k;i<n;i++){
            //add
            if(A[i]<0){
                q.add(i);
            }
            
            // remove
            if(!q.isEmpty()){
                int temp = q.peek();
                if(temp==i-k){
                    q.remove();
                }
            }
            
            // fill window solution
            if(q.isEmpty()){
                res[j] =0;
            }else{
                res[j]=A[q.peek()];
            }
            j++;
             
        }
        return res;

    }
}

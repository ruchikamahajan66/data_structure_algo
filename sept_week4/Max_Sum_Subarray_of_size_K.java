class Solution{
    static long maximumSumSubarray(int k, ArrayList<Integer> a,int n){
        // code here
        long sum =0; long max_so_far = Long.MIN_VALUE;
        for(int i=0;i<k;i++){
            sum = sum+a.get(i);
            if(sum>max_so_far){
                max_so_far = sum;
            }
        }
        for(int i =k;i<n;i++){
            sum = sum+a.get(i)-a.get(i-k);
            if(sum>max_so_far){
                max_so_far = sum;
            }
        }
        return max_so_far;
    }
}

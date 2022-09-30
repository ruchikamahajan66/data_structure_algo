class Solution
{
    //Function to find a continuous sub-Array which adds up to a given number.
    static ArrayList<Integer> subarraySum(int[] a, int n, int k) 
    {
        // Your code here
        ArrayList<Integer> res =new ArrayList<Integer>();
        int sum =0;
        int l = 0, r = 0;
        for(int i=0;i<n;i++){
            sum = sum +a[i];
            r = i;
            while(sum>k){
                sum = sum -a[l];
                l = l+1;
                if (l> r){
                    r = l;
                }
            }
            
            if(sum ==k && k != 0){
                res.add(l+1);
                res.add(r+1);
                return res;
            }
        }
         res.add(-1);
        return res;
    }
}

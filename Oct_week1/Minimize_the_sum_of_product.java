class Solution {

    public long minValue(long a[], long b[], int n) 
    {
        // Your code goes here
        long Result = 0;
        Arrays.sort(a);
        Arrays.sort(b);
        //Arrays.sort(a);
        //Arrays.sort(b, Collections.reverseOrder());
        for(int i = 0; i<n; i++){
            Result = Result+(a[i]*b[n-i-1]);
        }
        return Result;
    }
}

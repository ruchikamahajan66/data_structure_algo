class Solution {

    
    // a: input array
    // n: size of array
    // Function to find equilibrium point in the array.
    public static int equilibriumPoint(long arr[], int n) {

        // Your code here
        long sum =0;
        long left_sum=0;
        for (int i = 0; i<n; i++){
            sum = sum + arr[i];
        }
        for (int i = 0; i<n; i++){
            sum = sum - arr[i];
            
            if(left_sum==sum){
                return i+1;
            }    
            left_sum = left_sum+arr[i];
        }
        return -1;
    }
}

class Solution
{
    long findMaxSubarraySum(long arr[], int N,int X)
    {
        // Your code goes here
        long sum =0; long max_so_far = Long.MIN_VALUE; int j = 0;
        for(int i=0;i<N;i++){
            sum = sum +arr[i];
            while(sum>X){
                sum = sum -arr[j];
                j++ ;
                }
            
            if(sum==X){
               return sum; 
            }
            if(sum>max_so_far){
              max_so_far = sum;  
            }
        }
            return max_so_far ;
        }
}

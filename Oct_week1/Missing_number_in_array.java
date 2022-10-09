class Solution {
    int MissingNumber(int array[], int n) {
        // Your Code Here
        int arr_sum = 0;
        int sum = (n*(n+1)/2);
        for (int i =0; i<n-1;i++){
            arr_sum = arr_sum + array[i];
        }
        
        return sum -arr_sum;
    }
}

class Solution {
    int binarysearch(int arr[], int n, int k) {
        // code here
        int start = 0;
        int end = n-1;
        while(start<=end){
            int mid = (start+end)/2;
            if (arr[mid]==k){
                return mid;
            }
            else if(arr[mid]>k){
                end = mid-1;
            }
                else{
                    start = mid+1;
                }
            }
        return -1;
    }
}

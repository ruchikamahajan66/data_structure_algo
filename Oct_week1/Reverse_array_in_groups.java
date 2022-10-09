class Solution {
    //Function to reverse every sub-array group of size k.
    //arr[i] --> arr.get(i)
    // arr[i] = arr[j] -->  arr.set(i, arr.get(j))
    void reverseInGroups(ArrayList<Integer> arr, int n, int k) {
        // code here
        for(int i=0;i<n;i=i+k){
           int start = i;
            int end = start+k-1;
            if (end>n-1){
                end = n-1;
            }
            reverse(arr, start, end);
        }
        
    }
    void reverse(ArrayList<Integer> arr, int start, int end) {
        // code here
        int i=start, j = end;
        while(i<j){
            int temp =  arr.get(i);
            arr.set(i, arr.get(j));
            arr.set(j, temp);
            i = i+1;
            j = j-1;
        }
        
    }
}

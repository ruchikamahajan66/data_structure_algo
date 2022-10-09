class Solution{
    //Function to find the leaders in the array.
    static ArrayList<Integer> leaders(int arr[], int n){
        // Your code here
        ArrayList<Integer> res =new ArrayList<Integer>();
        int max_so_far = Integer.MIN_VALUE;
        for(int i=n-1;i>=0;i--){
            if(arr[i]>=max_so_far){
                res.add(arr[i]);
                max_so_far = arr[i];
            }
        }
        Collections.reverse(res);
    return res;
    }
}

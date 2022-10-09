class GfG
{
    int maxLen(int arr[], int n)
    {
        // Your code here
        int sum = 0, curr_length = 0, max_so_far = 0;
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for(int i =0; i<n;i++){
            sum = sum +arr[i];
            if(sum==0){
                max_so_far = i+1;
            }
            if (!map.containsKey(sum)){
                map.put(sum,i);
            }else{
                curr_length = i-map.get(sum);
                if(curr_length>max_so_far){
                max_so_far = curr_length;
                }
            }
        }
    return max_so_far;
    }
}

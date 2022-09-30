class Solution {

    // arr[] : the input array containing 0s and 1s
    // N : size of the input array
    
    // return the maximum length of the subarray
    // with equal 0s and 1s
    int maxLen(int[] arr, int N)
    {
        // Your code here
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        int sum = 0; int max_so_far = 0;
        for(int i=0;i<N;i++){
            if(arr[i]==0){
                arr[i] =-1;
            }
            sum = sum +arr[i];
            if(sum ==0){
                if(max_so_far<i+1){
                    max_so_far = i+1;
                }
            }
            if (!map.containsKey(sum)){
                map.put(sum,i);
            }
            else{
                int index = map.get(sum);
                if(i-index> max_so_far){
                    max_so_far = i-index;
                }
            }
        }
        return max_so_far;
        
    }
}


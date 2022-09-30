class Solution{
    //Function to check whether there is a subarray present with 0-sum or not.
    static boolean findsum(int arr[],int n)
    {
        //Your code here
        Map map = new HashMap<Integer, Integer>();
        int sum = 0;
        for(int i=0;i<n;i++){
            sum = sum +arr[i];
            if(sum ==0){
                return true;
            }
            if (!map.containsKey(sum)){
                map.put(sum,i);
            }
            else{
               return true; 
            }
        }
        return false;
    }
}

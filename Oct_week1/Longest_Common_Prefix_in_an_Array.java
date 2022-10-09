class Solution{
    String longestCommonPrefix(String arr[], int n){
        // code here
        if(n==0){
            return "";
        }
        if(n==1){
            return arr[0];
        }
        Arrays.sort(arr);
        int i = 0, j = 0, count = 0;
        while(i< arr[0].length() &&
        i< arr[n-1].length() && arr[0].charAt(i)==arr[n-1].charAt(i) )
        {
             i++;
        }
        if(i == 0){
            return "-1";
        }
        String pre = arr[0].substring(0, i);
        return pre;
    }
}

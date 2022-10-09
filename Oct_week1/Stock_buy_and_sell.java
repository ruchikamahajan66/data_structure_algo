class Solution{
    //Function to find the days of buying and selling stock for max profit.
    ArrayList<ArrayList<Integer> > stockBuySell(int A[], int n) {
        // code here
        ArrayList<ArrayList<Integer>> finalRes = new ArrayList<ArrayList<Integer>>();
        for(int i =1;i<n;i++){
            if(A[i-1] < A[i]){
                ArrayList<Integer> res = new ArrayList<Integer> ();
                res.add(i-1);
                res.add(i);
                finalRes.add(res);
            }
        }

        return finalRes;
    }
}


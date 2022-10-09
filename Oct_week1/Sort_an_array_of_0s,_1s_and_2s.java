class Solution
{
    public static void sort012(int a[], int n)
    {
        // code here 
        int count1 = 0, count2 = 0, count3 = 0;
        for (int i=0;i<n;i++){
            if(a[i]==0){
                count1 = count1+1;
            }
            else if(a[i]==1){
                count2 = count2+1;
            }
            else{
                count3 = count3+1;
            }
        }
        for(int i=0;i<n;i++){
            if(count1!=0){
                a[i] = 0;
                count1 = count1 -1;
            }
            else if(count2!=0){
                a[i] = 1;
                count2 = count2 -1;
            }
            else{
                a[i] = 2;
                count3 = count3 -1;
            }
        }
    }
}

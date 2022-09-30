class Solution {
    void zigZag(int a[], int n) {
        // code here
        
        
        for (int i=1;i<n;i++){
            boolean flag = i%2 == 1 ? true:false;
            if (flag) {
                if (a[i]<a[i-1]){
                    int temp = a[i];
                    a[i]= a[i-1];
                    a[i-1] = temp;
                }
            }else {
                if (a[i]>a[i-1]){
                    int temp = a[i];
                    a[i]= a[i-1];
                    a[i-1] = temp;
                }    
        }
        // if (flag){
        //     flag = false;
        // }
        // else{
        //     flag = true;
        //     }
        }
    }

}

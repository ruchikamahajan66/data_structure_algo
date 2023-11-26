class Solution {
    public String simplifyPath(String path) {

        Stack<String> st = new Stack<String>();
        String str = "";
        for(int i =0;i<path.length();i++){
            if(path.charAt(i) == '/' ){
                if(!str.isEmpty()){
                    if(str.equals("..") ){
                        if(!st.isEmpty()){
                            st.pop();
                        }
                    }else if(!str.equals(".")){
                        st.push(str);
                    }
                }
                str = "";
            }else{
                str = str + path.charAt(i);
            }
        }

        if(!str.isEmpty()){
            if(str.equals("..") ){
                if(!st.isEmpty()){
                    st.pop();
                }
            }else if(!str.equals(".")){
                st.push(str);
            }
        }


        if(st.isEmpty()){
            return "/";
        }
        String res = "";
        while(!st.isEmpty()){
            res = "/"+st.pop()+res;
        }

        return res;
    }
}
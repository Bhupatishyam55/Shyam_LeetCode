class Solution {
    public int firstUniqChar(String s) {
        int[] arr=new int[128];
        for(int i=0 ; i<s.length();i++){
            char ch=s.charAt(i);
            arr[ch]++;
        }
        for(int i =0 ; i<s.length();i++){
            char ch=s.charAt(i);
            if(arr[ch]==1){
                return i;
            }
        }
        return -1;
    }
}
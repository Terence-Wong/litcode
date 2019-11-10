class Solution {
    public int fib(int N) {
        if(N == 0 || N == 1){
            return N;
        }
        int a  = 0;
        int b  = 1;
        int current = -1;
        for(int i = 0; i < N-1; i++){
            current = a + b;
            a = b;
            b = current;
        }
        return current;
    }
}
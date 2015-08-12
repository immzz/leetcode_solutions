#include <stdio.h>

class Solution {
public:
    double pow(double x, int n) {
        if(x == 0){
            return 0;
        }else{
            double pro = 1.0;
            if(n<0){
                for(int i=0;i>n;i--){
                    pro = pro/x;
                }
                return pro;
            }else if(n==0){
                return 1;
            }else{
                for(int i=0;i<n;i++){
                    pro = pro*x;
                }
                return pro;
            }
        }
    }

};

int main(){
	Solution sol;
	stdio::cout<<sol.pow(10,2);
}
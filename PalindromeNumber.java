public class PalindromeNumber {
    public boolean isPalindrome(int x) {
		if(x < 0){
			return false;
		}
        int div = 1;//Start from 1 because x might be smaller than 10
		while(x/div >= 10){
			div *= 10;
		}
		while(x!=0){//Use !=0 as the criteria because x might be 1000021
			if(x/div != x%10){
				return false;
			}
			x = (x%div)/10;
			div /= 100;
		}
		return true;
    }
	public static void main(String [] args){
		PalindromeNumber sol = new PalindromeNumber();
		System.out.println(sol.isPalindrome(1));
	}
}
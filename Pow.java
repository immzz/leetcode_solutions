public class Pow {
    public double pow(double x, int n) {
        if(x == 0){
            return 0;
        }else if(x == 1){
            return 1;
        }else if(x == -1){
			if(n%2 == 1) return -1; else return 1;
		}else if(n==0){
            return 1;
        }else if(n<0){
			return 1/pow(x,-n);
		}else if(n==1){
         	return x;
		}else if(n % 2 == 1){
			return x*pow(x*x,n/2);
        }else{
        	return pow(x*x,n/2);
        }
    }
	public static void main(String [] args){
		Pow p = new Pow();
		System.out.println("OK");
		System.out.println(p.pow(10,-2));
	}
}
import java.util.*;
import java.io.*;

public class loops2 {
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            int sum = a; 
            for (int j = 0; j < n; j++) {
                int next = (int) Math.pow(2,j)*b; 
                sum += next;
                System.out.printf("%s ", sum);
            }
            if (i < t - 1) {
                System.out.print("\n");
            }
        }
        in.close();
    }
}

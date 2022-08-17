import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class negSubarray {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] A = new int[n]; 
        
        for (int i = 0; i < n; i++) {
            A[i] = sc.nextInt();
        }
        
        int negs = 0; 
        for (int i = 0; i < A.length; i++) {
            for (int j = i; j < A.length; j++) {
                int[] temp = Arrays.copyOfRange(A, i, j + 1);  // make copy of original array over a range
                int tempSum = 0;
                for (int k = 0; k < temp.length; k++) {
                    tempSum += temp[k];
                }
                if (tempSum < 0) {
                    negs += 1;
                }
            }
        }
        System.out.println("" + negs);
    }
}
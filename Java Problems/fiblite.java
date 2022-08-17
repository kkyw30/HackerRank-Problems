import java.io.*;
import java.util.*;
import java.lang.*;

public class fiblite {
    public static int generateFibValue(int n) {  // n represents index in Fibonacci sequence
        // define base cases        
        if (n == 0) {
            return 0;
        } else if (n == 1) {
            return 1; 
        }
        // general case
        return generateFibValue(n - 1) + generateFibValue(n - 2); 
    }

    public static void main(String[] args) throws Exception {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        int N = Integer.parseInt(line);
        System.out.println(generateFibValue(N));
    }
}

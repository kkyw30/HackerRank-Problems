import java.io.*;
import java.util.*;

public class fibreturns {
    public static int fib(int input) {
        if (input == 0) {
            return 0; 
        } else if (input == 1) {
            return 1; 
        }
        return fib(input - 1) + fib(input - 2);
    }

    public static void main(String[] args) throws Exception {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = br.readLine()) != null) {
            for (String numStr: line.split("\\s")) {
                int input = Integer.parseInt(numStr);
                System.out.println(fib(input));
            }
        }
    }
}
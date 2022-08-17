import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class uncoupled {
    public static void main(String[] args) throws Exception {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in); 
        String [] str = sc.nextLine().split(",");
        int uncoupled = 0; 
        for (String i : str) {
            // XOR is associative and commutative
            uncoupled ^= Integer.parseInt(i.trim());
        }
        System.out.println("" + uncoupled);
    }
}

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

public class reverseGame {
    // form the starting array 
    public static int[] formStart(int n) {
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = i; 
        }
        return arr; 
    }
    
    // reverse the array starting from a certain index
    public static int[] reverseArray(int[] arr, int n) {
        for (int i = 0; i < arr.length; i++) {
            if (i <= n) {
                arr[i] = arr[i];
            } else {
                // switch the digits at the right indices
                int temp = arr[i]; 
                arr[i] = arr[arr.length - i - 1];
                arr[arr.length - i - 1] = temp;
            } 
        }
        return arr; 
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(bufferedReader.readLine().trim());
        
        for (int i = 0; i < t; i++) {
            String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");
            int n = Integer.parseInt(firstMultipleInput[0]);
            int k = Integer.parseInt(firstMultipleInput[1]);
            // solution reached using combinatorics
            System.out.println((k >= n / 2) ? (n - 1 - k) * 2 : 2 * k + 1);   
        }
        bufferedReader.close();
    }
}

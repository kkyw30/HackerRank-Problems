import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class javaList {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(); 
        List<Integer> arr = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            arr.add(sc.nextInt());
        }
        
        int Q = sc.nextInt();
        
        // compile list of commands and numbers
        String[] queries = new String[2*Q+1];
        for (int i = 0; i <= 2*Q; i++) {
            if (i == 0) {
                String line = sc.nextLine();
                continue;
            }
            String line = sc.nextLine();
            queries[i] = line; 
        }
        for (int i = 1; i < queries.length; i++) {
            if (i % 2 == 1) {
                if (queries[i].equals("Insert")) {
                    String numbers = queries[i+1];
                    String[] nums = numbers.split(" ", 2);
                    int index = Integer.parseInt(nums[0]);
                    int num = Integer.parseInt(nums[1]);
                    arr.add(index, num);
                } else if (queries[i].equals("Delete")) {
                    int index = Integer.parseInt(queries[i+1]);
                    arr.remove(index);
                }
            } else {
                continue; 
            }
        }
        
        String output = "";
        for (int i = 0; i < arr.size(); i++) {
            output += arr.get(i) + " ";
        }
        System.out.println(output);
    }
}
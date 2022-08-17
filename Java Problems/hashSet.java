import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class hashSet {

 public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int t = s.nextInt();
        String [] pair_left = new String[t];
        String [] pair_right = new String[t];
        
        for (int i = 0; i < t; i++) {
            pair_left[i] = s.next();
            pair_right[i] = s.next();
        }
        
        // assuming pair_left and pair_right are the same length
        Set<String> names = new HashSet<String>();               // HashSet has unique elements only (because of hashing)
        for (int i = 0; i < pair_left.length; i++) {
            String name = pair_left[i] + " " + pair_right[i];
            names.add(name);
            System.out.println(names.size());
        }

   }
}
import java.util.Scanner;

public class substringComparisons {

    public static String getSmallestAndLargest(String s, int k) {
        String smallest = "";
        String largest = "";

        // insert list library 
        java.util.List<String> subs = new java.util.ArrayList<>();
        
        // collect all substrings of length k
        for (int i = 0; i < s.length() - k + 1; i++) {
            subs.add(s.substring(i,i+k));
        }
        
        // introduct Collections library to sort collected substrings
        java.util.Collections.sort(subs);
        smallest = subs.get(0);
        largest = subs.get(subs.size() - 1);
        
        return smallest + "\n" + largest;
    }


    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();
      
        System.out.println(getSmallestAndLargest(s, k));
    }
}
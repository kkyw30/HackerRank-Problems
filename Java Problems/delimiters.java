import java.io.*;
import java.util.*;

public class delimiters {
    
    public static boolean validDelimiter(String delimiters) {
        // has to be even length 
        if (delimiters.length() % 2 != 0) {
            return false; 
        }
        
        // no null input strings
        if (delimiters == null) {
            return false; 
        }
        
        // make sure all chars are balanced
        while (delimiters.contains("()") || delimiters.contains("[]") || delimiters.contains("{}")) {
            delimiters = delimiters.replaceAll("\\(\\)", "").replaceAll("\\[\\]", "").replaceAll("\\{\\}", "");
        }
        return (delimiters.length() == 0);
    }

    public static void main(String[] args) throws Exception {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        String returnThis = "" + validDelimiter(line);
        String first = returnThis.substring(0,1);
        String first2 = first.toUpperCase();
        String remaining = returnThis.substring(1,returnThis.length());
        String returnThis2 = first2 + remaining; 
        System.out.println(returnThis2);
    }
}

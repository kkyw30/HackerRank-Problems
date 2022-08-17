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

class Result {

    public static int gcd(int l, int b) {
        int lesser = 0; 
        if (l <= b) lesser = l; 
        else lesser = b; 
        int gcd = 1; 
        for (int i = 2; i <= lesser; i++) {
            if (l % i == 0 && b % i == 0) {
                gcd = i; 
            }
        }
        return gcd; 
    }

    // goal to return number of max dimension of square-sized pieces
    public static int restaurant(int l, int b) {
        int product = l * b; 
        
        // find greatest common denominator of l and b (greatest dimension that can be taken out of l and b) 
        int gcd = gcd(l, b);
        int num = product / (gcd * gcd);      // max size square that can be made        
        return num; 
    }

}

public class restaurant {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int t = Integer.parseInt(bufferedReader.readLine().trim());

        IntStream.range(0, t).forEach(tItr -> {
            try {
                String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

                int l = Integer.parseInt(firstMultipleInput[0]);

                int b = Integer.parseInt(firstMultipleInput[1]);

                int result = Result.restaurant(l, b);

                bufferedWriter.write(String.valueOf(result));
                bufferedWriter.newLine();
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        bufferedReader.close();
        bufferedWriter.close();
    }
}

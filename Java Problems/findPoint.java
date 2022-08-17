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

    /*
     * Complete the 'findPoint' function below.
     *
     * The function is expected to return an INTEGER_ARRAY.
     * The function accepts following parameters:
     *  1. INTEGER px
     *  2. INTEGER py
     *  3. INTEGER qx
     *  4. INTEGER qy
     */

    public static List<Integer> findPoint(int px, int py, int qx, int qy) {
    // Write your code here
    List<Integer> returnThis = new ArrayList<>();
    int xdistance = qx - px; 
    int ydistance = qy - py; 
    int rx = 0; 
    int ry = 0;
    
    // find x-coordinate
    if (xdistance > 0) {
        rx = qx + xdistance;
    } else if (xdistance < 0) {
        rx = qx - xdistance; 
    } else if (xdistance == 0) {
        rx = qx;
    }
    
    // find y-coordinate
    if (ydistance > 0) {
        ry = qy + ydistance;
    } else if (ydistance < 0) {
        ry = qy - ydistance;
    } else if (ydistance == 0) {
        ry = qy;
    }
    returnThis.add(rx);
    returnThis.add(ry);
    return returnThis;
    }

}

public class findPoint {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        IntStream.range(0, n).forEach(nItr -> {
            try {
                String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

                int px = Integer.parseInt(firstMultipleInput[0]);

                int py = Integer.parseInt(firstMultipleInput[1]);

                int qx = Integer.parseInt(firstMultipleInput[2]);

                int qy = Integer.parseInt(firstMultipleInput[3]);

                List<Integer> result = Result.findPoint(px, py, qx, qy);
                System.out.println(result);

                bufferedWriter.write(
                    result.stream()
                        .map(Object::toString)
                        .collect(joining(" "))
                    + "\n"
                );
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        bufferedReader.close();
        bufferedWriter.close();
    }
}

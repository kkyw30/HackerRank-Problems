import java.util.*;

public class array {

    public static boolean canWin(int leap, int[] game) {
        return solvable(leap, game, 0);
    }
    
    // method to see if game can be solved
    public static boolean solvable(int leap, int[] game, int i) {
        if (i < 0 || game[i] == 1) {
            return false; 
        }
        if (i + 1 >= game.length || i + leap >= game.length) {
            return true;
        }
        
        game[i] = 1;           // so we can't come back to this index for recursive calls
        int back = i - 1; 
        int forward = i + 1; 
        int leaped = i + leap;

        return solvable(leap, game, forward) || solvable(leap, game, back) || solvable(leap, game, leaped);
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int q = scan.nextInt();
        while (q-- > 0) {
            int n = scan.nextInt();
            int leap = scan.nextInt();
            
            int[] game = new int[n];
            for (int i = 0; i < n; i++) {
                game[i] = scan.nextInt();
            }

            System.out.println( (canWin(leap, game)) ? "YES" : "NO" );
        }
        scan.close();
    }
}
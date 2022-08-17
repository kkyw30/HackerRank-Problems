import java.util.*;

class validDelimiters {
    
    // Java Stack is linear data structure that stores collection of objects, based on LIFO principle
    public static boolean isBalanced(String s) {
        Stack<Character> stack = new Stack<Character>();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') stack.push('(');
            else if (s.charAt(i) == '[') stack.push('[');
            else if (s.charAt(i) == '{') stack.push('{');
            else if (s.charAt(i) == ')') {
                if (stack.isEmpty()) return false; 
                if (stack.pop() != '(') return false;    // see if opposite end char is '('
            }
            else if (s.charAt(i) == ']') {
                if (stack.isEmpty()) return false;       // no former characters
                if (stack.pop() != '[') return false;
            } else if (s.charAt(i) == '}') {
                if (stack.isEmpty()) return false; 
                if (stack.pop() != '{') return false;
            }
        }
        return stack.isEmpty();       // all chars have been popped if done correctly
    }
	
	public static void main(String []argh)
	{
		Scanner sc = new Scanner(System.in);
		Stack<Character> stack = new Stack<Character>();
        
		while (sc.hasNext()) {
			String input = sc.nextLine();
            if (isBalanced(input)) System.out.println("true");
            else System.out.println("false");
		}
	}
}




//Complete this code or write your own from scratch
import java.util.*;
import java.io.*;

class javaMap {
	public static void main(String []argh)
	{
		Scanner in = new Scanner(System.in);
		int n=in.nextInt();
		in.nextLine();
        
        Map<String, Integer> phoneNumbers = new HashMap<String, Integer>();
		for(int i=0;i<n;i++)
		{
			String name=in.nextLine();
			int phone=in.nextInt();
            phoneNumbers.put(name, phone);
			in.nextLine();
		}
        
        // read remaining lines (names to search for in hashmap)
		while(in.hasNext())
		{
			String s=in.nextLine();
            if (phoneNumbers.containsKey(s)) {
                System.out.println(s + "=" + phoneNumbers.get(s));
            } else {
                System.out.println("Not found");
            }
		}
	}
}




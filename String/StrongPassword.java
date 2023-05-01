package String;

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



/*
 * Complete the 'minimumNumber' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. STRING password
 */





public class StrongPassword {
	public static int minimumNumber(int n, String password) {
		// Return the minimum number of characters to make the password strong
		    String numbers = "0123456789";
		    String lower_case = "abcdefghijklmnopqrstuvwxyz";
		    String upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
		    String special_characters = "!@#$%^&*()-+";
		    
		    int add_char = 0;
		    
		    boolean a1 = true;
		    boolean a2 = true;
		    boolean a3 = true;
		    boolean a4 = true;
	
		    for (int i = 0; i < password.length(); i++) {
		        char character = password.charAt(i); // ith index character of string
		        String str = Character.toString(character);
		        if (numbers.contains(str)){
		            a1 = false;
		        }
		        if (lower_case.contains(str)){
		            a2 = false;
		        }
		        if (upper_case.contains(str)){
		            a3 = false;
		        }
		        if (special_characters.contains(str)){
		            a4 = false;
		        }
		    }
		    if (a1){
		        add_char += 1;
		    }
		    if (a2){
		        add_char += 1;
		    }   
		    if (a3){
		        add_char += 1;
		    }   
		    if (a4){
		        add_char += 1;
		    }      
		    int length = add_char + password.length();
		    if (length <6){
		        add_char += (6-length);
		    }
		    
		    return add_char;
		}
    public static void main(String[] args) throws IOException {
//        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
//        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

//        int n = Integer.parseInt(bufferedReader.readLine().trim());

//        String password = bufferedReader.readLine();
        int n = 3;
        String password = "zss";

        int answer = minimumNumber(n, password);
        
        System.out.println("answer "+answer);

//        bufferedWriter.write(String.valueOf(answer));
//        bufferedWriter.newLine();
//
//        bufferedReader.close();
//        bufferedWriter.close();
    }
}

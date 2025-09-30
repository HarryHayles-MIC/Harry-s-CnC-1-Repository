// Harry Hayles 30/9/25- This code is an example of reading an input
package outputName;
//Import the Scanner Class. Code will not function without it
import java.util.Scanner;

public class outputName {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//Give your scanner a name like a variable
		Scanner sc = new Scanner(System.in);
		System.out.println ("What is your name? ");
		//this reads your input as 2 strings One for First Name, and one for the sur name
		String yourName = sc.next ();
		String surName = sc.next ();
		//this outputs the scanned strings and hello
		System.out.println("Hello " + yourName + " " + surName);
		System.out.println ("What is your favourite Color? ");
		//This Reads the colors string	
		String favColor = sc.next ();
		System.out.println("Your Favourite Colour is "+ favColor + "\n My favourite Color is Blue!");
		
	}

}

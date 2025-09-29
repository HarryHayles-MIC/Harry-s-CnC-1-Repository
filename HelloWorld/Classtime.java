//Java code to caluclate time in class
//Created by Harry Hayles
// 24/09/25
package Classtime;

public class Classtime {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//Variables
		int days= 5;
		int averagetime=7;
		int monday= 8;
		int friday= 4;
		int totaltime;
		//run code
		System.out.println("Welcome User");
		System.out.println("I am in class "+ days + " days per week");
		System.out.println("On average I am in for "+ averagetime +" hours but on mondays I am in for " + monday + " hours and on fridays I'm only in for "+ friday + " hours." );
		totaltime= averagetime*3 + monday + friday;
		System.out.println("I am in class for a total of "+ totaltime+ " hours per week.");
		System.out.println("Thank you for using this program.");
		System.out.println("Good Bye.");
		
	}

}

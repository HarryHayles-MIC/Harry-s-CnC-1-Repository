//Java app to store numb values and then combine them
//Created by Harry Hayles
// 16/09/25
package PrintNum;

public class PrintNum {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int number1 = 10;
		int number2 = 15;
		int number3 = 5;
		int total;

		System.out.println("Welcome to the number printing program");
		System.out.println("The first number is " + number1);
		System.out.println("The second number is " + number2);
		System.out.println("The thrid number is " + number3);
		total = number1 + number2 + number3;
		System.out.println("The total number is " + total);
		
		total = number1 + number2 - number3;
		System.out.println("The total number is " + total);
		System.out.println("Thank You");	
	}

}

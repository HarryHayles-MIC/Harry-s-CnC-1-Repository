//Java app to store numb values and then combine them
//Created by Harry Hayles
// 23/09/25
package AddNumbers;

public class AddNumbers {

	public static void main(String[] args) {
		int number1 = 20;
		int number2 = 5;
		int addtotal;
		int subTotal;
		int multi;
		int div;
		System.out.println("Welcome to the number printing program");
		System.out.println("The first number is " + number1);
		System.out.println("The second number is " + number2);
		addtotal = number1+number2;
		System.out.println("The total = "+addtotal);
		System.out.println(number1 + " + " + number2 + " = " + addtotal);
		subTotal = number1-number2;
		System.out.println(number1 + " - " + number2 + " = " + subTotal);
		multi = number1*number2;
		System.out.println(number1 + " * " + number2 + " = " + multi);
		div = number1/number2;
		System.out.println(number1 + " / " + number2 + " = " + div);
		
		System.out.println("Thank You");
}
}
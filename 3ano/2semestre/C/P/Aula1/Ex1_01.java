import java.util.Scanner;

public class Ex1_01 {
    final static Scanner in = new Scanner(System.in);
    public static void main(String args[]) { 
        while(in.hasNextLine()){
            double num1 = in.nextDouble();
            String operator = in.next();
            double num2 = in.nextDouble();

            double result;

            switch(operator) {
                case "+":
                    result = num1 + num2;
                    break;
                case "-":
                    result = num1 - num2;
                    break;
                case "*":
                    result = num1 * num2;
                    break;
                case "/":
                    if (num2 == 0) {
                        System.err.println("Error: Division by zero!");
                        in.close();
                        return;
                    }
                    result = num1 / num2;
                    break;
                default:
                    System.err.println("Error: Invalid operator!");
                    in.close();
                    return;
            }

            System.out.println(result);
            System.out.println("\n");
        }

        in.close();
    }
}

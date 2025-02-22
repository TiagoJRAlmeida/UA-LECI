import java.util.Scanner;
import java.util.Stack;

public class Ex1_03 {
    private static final Scanner in = new Scanner(System.in);
    private static final Stack<Double> stack = new Stack<Double>();
    public static void main(String[] args) {
        while(in.hasNextLine()) {
            String line = in.nextLine();
            Double var1;
            Double var2;

            Scanner sc = new Scanner(line);
            while(sc.hasNext()) {
                String newToken = sc.next();
                if(isNumeric(newToken)) stack.add(Double.parseDouble(newToken));
                else {
                    switch(newToken){
                        case "+":
                            if(stack.size() < 2){
                                System.err.println("Error: Invalid expression!");
                                sc.close();
                                in.close();
                                return;
                            }
                            var1 = stack.pop();
                            var2 = stack.pop();
                            stack.add(var1 + var2);
                            break;
                        case "-":
                            if(stack.size() < 2){
                                System.err.println("Error: Invalid expression!");
                                sc.close();
                                in.close();
                                return;
                            }
                            var1 = stack.pop();
                            var2 = stack.pop();
                            stack.add(var1 - var2);
                            break;
                        case "*":
                            if(stack.size() < 2){
                                System.err.println("Error: Invalid expression!");
                                sc.close();
                                in.close();
                                return;
                            }
                            var1 = stack.pop();
                            var2 = stack.pop();
                            stack.add(var1 * var2);
                            break;
                        case "/":
                            if(stack.size() < 2){
                                System.err.println("Error: Invalid expression!");
                                sc.close();
                                in.close();
                                return;
                            }
                            var1 = stack.pop();
                            var2 = stack.pop();
                            stack.add(var1 / var2);
                            break;
                        default:
                            System.err.println("Error: Invalid operator!");
                            sc.close();
                            in.close();
                            return;
                    }
                }
                
                System.out.println("Stack: " + stack);
            }
            sc.close();
        }

        in.close();
    }

    private static boolean isNumeric(String str) { 
        try {  
          Double.parseDouble(str);  
          return true;
        } catch(NumberFormatException e){  
          return false;  
        }  
      }
}

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Ex1_02 {
    private static final Scanner in  = new Scanner(System.in);
    private static final Map<String, Double> variables = new HashMap<String, Double>();
    public static void main(String[] args){
        while(in.hasNextLine()) {
            String line = in.nextLine().trim();
            
            // Sai quando uma linha vazia é introduzida (Enter para sair)
            if (line.isEmpty()) {
                break;
            }

            // Caso da atribuição de valores
            if(line.contains("=")) {
                String[] parts = line.split("=");
                if (parts.length != 2) {
                    System.err.println("Error: Invalid expression!");
                    break;
                }

                String key = parts[0].trim();
                String value = parts[1].trim();

                // Caso seja apenas uma atribuição sem uma expressão
                if(value.split("\\s+").length == 1) {
                    if(variables.containsKey(key)) variables.replace(key, Double.parseDouble(value));
                    else {
                        variables.put(key, Double.parseDouble(value));
                    }
                }
                else if(value.split("\\s+").length == 3) {
                    Double result = CalculateExpression(value);
                    if(result == null) break;
                    if(variables.containsKey(key)) variables.replace(key, result);
                    else variables.put(key, result);
                }
                else {
                    System.err.println("Error: Invalid expression!");
                    break;
                }

            }
        
            // Caso seja apenas uma conta sem atribuição
            else if(line.split("[ \n]+").length == 3) {
                Double result = CalculateExpression(line);
                if(result == null) break;
                System.out.println(String.format("Operation: %s = %.1f", line, result));
                System.out.flush();
            }
        
            // Caso seja uma operação não suportada
            else {
                System.err.println("Error: Invalid operation!");
                break;
            }
            
        }

        in.close();
    }


    private static Double CalculateExpression(String expression) {
        Scanner sc = new Scanner(expression);
                
        String var1 = sc.next();
        String operator = sc.next();
        String var2 = sc.next();
        
        Double num1;
        Double num2;
        Double result;

        if(variables.containsKey(var1)) num1 = variables.get(var1);
        else num1 = Double.parseDouble(var1);

        if(variables.containsKey(var2)) num2 = variables.get(var2);
        else num2 = Double.parseDouble(var2);

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
                    sc.close();
                    return null;
                }
                result = num1 / num2;
                break;
            default:
                System.err.println("Error: Invalid operator!");
                sc.close();
                return null;
        }
        
        sc.close();
        return result;
    }
}

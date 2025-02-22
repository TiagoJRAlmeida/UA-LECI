import java.io.File;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Ex1_05 {
    private final static Scanner in = new Scanner(System.in);
    private final static String filePath = "bloco1/numbers.txt";
    private final static Map<String, Integer> numberTable = readNumberFile(filePath);
    public static void main(String[] main){

        while(in.hasNextLine()){
            String line = in.nextLine();
            String processedLine = line.replace("-", " ");
            Scanner scline = new Scanner(processedLine);
            int number; 
            int acum = 0;
            int result = 0;
            while(scline.hasNext()) {
                String newToken = scline.next();
                String text = newToken.toLowerCase();
                if (numberTable.containsKey(text)) {
                    newToken = numberTable.get(text).toString();
                    number = Integer.parseInt(newToken);
                    if(number <= acum) {
                        result += acum;
                        acum = number;
                    }
                    else if(acum != 0 && number > acum) {
                        acum *= number;
                    }
                    else {
                        acum = number;
                    }
                }
            }
            result += acum;
            System.out.println(String.format("%s -> %d", line, result));
            scline.close();
        }
    }


    private static Map<String, Integer> readNumberFile(String path){
        File file = new File(path);
        Map<String, Integer> result = new HashMap<String, Integer>();
        
        try (Scanner scin = new Scanner(file)) {
            while(scin.hasNextLine()){
                String line = scin.nextLine().trim();
                if (line.length() > 0){
                    String[] parts = line.split(" - ");
                    if (parts.length != 2){
                        System.err.println("Error: Syntax error in numbers file!");
                        System.exit(1);
                    }
                    String key = parts[1].toLowerCase();
                    if (result.containsKey(key)){
                        System.err.println("Error: Repeated number");
                        System.exit(1);
                    }
                    try{
                        result.put(key, Integer.parseInt(parts[0]));
                    } catch(NumberFormatException e) {
                        System.err.println("Error: Invalid number");
                        System.exit(1);
                    }
                }
            }
        }catch (IOException e) {
            System.err.println("Erro ao ler o ficheiro: " + e.getMessage());
        }
        
        return result;
    }
}

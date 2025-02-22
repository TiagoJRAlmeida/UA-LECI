import java.io.File;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Ex1_06 {
    public static void main(String[] args){
        if (args.length < 2) {
            System.exit(1);
        }

        Map<String, String> dict = readTranslationFile(args[0]);

        for (int f = 1; f < args.length; f++) {
            try {
                File fin = new File(args[f]);
                Scanner scin = new Scanner(fin);
                while(scin.hasNextLine()) {
                    String line = scin.nextLine();
                    System.out.print("\"" + line + "\" -> \"");
                    String[] list = line.split("\\s+");
                    for (int i = 0; i < list.length; i++) {
                        if (i > 0) System.out.print(" ");
                        System.out.print(translate(dict, list[i], new HashMap<>()));
                    }
                    System.out.println("\"");
                }
                scin.close();
            } catch(IOException e) {
                System.err.println("ERROR: reading input file \"" + args[f]);
                System.exit(1);
            }
        }
    }


    private static Map<String, String> readTranslationFile(String path){
        Map<String, String> dict = new HashMap<String, String>();

        try {
            File file = new File(path);
            Scanner scin = new Scanner(file);
            while(scin.hasNextLine()) {
                String[] list = scin.nextLine().split("\\s+");
                if (list.length > 0) {
                    if (list.length < 2) {
                        System.err.println("ERROR: Line with bad formatting!");
                        System.exit(1);
                    }
                    if (dict.containsKey(list[0])) {
                        System.err.println("ERROR: Word already exists!");
                        System.exit(1);
                    }
                    String translation = list[1];
                    for (int i = 2; i < list.length; i++)
                        translation += " " + list[i];
                    
                    dict.put(list[0], translation);
                }
            }
            scin.close();
        } catch(IOException e) {
            System.err.println("ERROR: Reading dictionary file!");
            System.exit(1);
        }

        return dict;
    }


    private static String translate(Map<String, String> dict, String word, Map<String, Boolean> history) {
        if (history.containsKey(word)) {
            System.err.println("ERROR: Dictionary with infinite recursion detected!");
            System.exit(1);
        }
        
        String translation = dict.get(word);
        if (translation != null) {
            history.put(word, true);
            String[] words = translation.split("\\s+");
            StringBuilder result = new StringBuilder();
            for (String w : words) {
                if (result.length() > 0) result.append(" ");
                result.append(translate(dict, w, history));
            }
            history.remove(word);
            return result.toString();
        }
        return word;
    }
}

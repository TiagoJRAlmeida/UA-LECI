import java.io.File;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;
import java.io.FileNotFoundException;
import java.io.PrintStream;
import java.lang.Math;

public class WSGenerator {
    public static void main(String[] args) throws Exception {
        int reset = 1;
        try {

            String[] opts = readArgs(args);

            File puzzle = new File(opts[0]);
            int n = Integer.valueOf(opts[1]);

            if (opts[2] != null) {
                PrintStream newOut = new PrintStream(new File(opts[2]));
                System.setOut(newOut);
            }

            Soup soup = new Soup(n);

            List<String> insertedWords = new LinkedList<String>();

            while (reset == 1) {
                reset = 0;

                Scanner reader = new Scanner(puzzle);
                insertedWords.removeAll(insertedWords);


                soup = new Soup(n);
                soup.fillEmpty();

                int count, x, y;

                String data;
                reader.useDelimiter("[,;\r\n ]");
                while (reader.hasNext()) {

                    count = 0;

                    data = reader.next();
                    // System.out.printf("Lendo: %s \n", data);

                    if (!data.matches("[a-zA-Z]+") || data.length() < 3)
                        continue;

                    insertedWords.add(data);
                        
                    Word w;
                    do {
                        // Random Direction
                        DIRECTION dir = DIRECTION.getRandom();

                        // Random Coords(beginning of word)
                        x = (int) (Math.random() * n) + 1;
                        y = (int) (Math.random() * n) + 1;

                        w = new Word(dir, new int[] { x, y }, data);

                        count++;

                    } while (!soup.setword(w) && count <= 100);

                    if (count > 100) {
                        System.err.printf("Inserção de %s falhou... Reiniciando Processo.\n", data);
                        reset = 1;
                    }
                }

                reader.close();
                soup.filler();
            }

            System.out.println(soup.toString());
            for(String word:insertedWords)
                System.out.println(word);
            // System.out.println(new String(Files.readAllBytes(Paths.get(opts[0])), StandardCharsets.UTF_8));

        } catch (FileNotFoundException e) {
            System.out.println("Coudlnt open file.");
        }
    }

    public static String[] readArgs(String[] args) {
        int ind;
        String s;
        String[] opts = new String[3];

        for (String arg : args) {
            if (arg.charAt(0) == '-')
                if (arg.length() < 1 || !(arg.charAt(1) == 'o' || arg.charAt(1) == 'i' || arg.charAt(1) == 's'))
                    usage();
        }

        // -i option
        ind = find(args, "-i");
        opts[0] = getOpt(args, ind);

        // -s
        ind = find(args, "-s");
        s = getOpt(args, ind);
        // check if numeric
        try {
            Integer.parseInt(s);
        } catch (NumberFormatException e) {
            usage();
        }
        opts[1] = s;

        // -o
        ind = find(args, "-o");
        if (ind > -1) {
            opts[2] = getOpt(args, ind);
        }

        return opts;
    }

    public static String getOpt(String[] args, int ind) {
        if (ind < 0 || ++ind == args.length || args[ind].charAt(0) == '-') {
            usage();
        }
        return args[ind];
    }

    public static int find(String[] args, String s) {
        for (int n = 0; n < args.length; n++) {
            if (args[n].equals(s))
                return n;
        }
        ;
        return -1;
    }

    public static void usage() {
        System.err.println(" -i [file] -s [size] -o {file} ");
        System.exit(-1);
    }
}

package lab01;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

public class WSSolver {
    public static void main(String[] args) throws FileNotFoundException, IOException {
        // Verifica se o número de argumentos é válido
        if (args.length != 1) {
            System.out.println("Usage: java lab01/WSSolver lab01/<filename>");
            System.exit(1);
        }

        int size = 0;
        File soupFile = null;
        String fileName = null;

        // Tenta ler o ficheiro
        try {
            // Verifica se o ficheiro existe
            soupFile = new File(args[0]);
            fileName = args[0].replaceAll(".txt", "");

            // Tamanho da sopa de letras
            Scanner fileScanner = new Scanner(soupFile);
            size = fileScanner.nextLine().length();
            fileScanner.close();
        } catch (Exception e) {
            // Se não conseguir ler o ficheiro, termina o programa
            System.out.println("ERROR: Invalid file");
            System.exit(1);
        }

        // Verifica se o tamanho da sopa de letras é válido
        if (size > 40) {
            System.out.println("ERROR: Size of Soup too big (>40)");
            System.exit(1);
        }

        // Cria uma instância da classe WSSolver
        impWSSolver wsSolver = new impWSSolver();

        // Cria uma lista de palavras a procurar na sopa de letras e uma matriz com a
        // sopa de letras
        ArrayList<String> words = wsSolver.wordsToFind(soupFile, size);
        Character[][] soup = wsSolver.soupMatrix(soupFile, size);

        // Procura as palavras na sopa de letras e cria ficheiro com os resultados
        wsSolver.findWords(soup, words, fileName);
    }
}

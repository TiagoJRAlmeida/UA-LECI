package lab01;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Scanner;

public class impWSSolver {
    // Retorna uma lista de palavras a procurar na sopa de letras
    public ArrayList<String> wordsToFind(File file, int size) throws FileNotFoundException {
        Scanner fileScan = null;

        // Cria um ArrayList para guardar as palavras
        ArrayList<String> words = new ArrayList<String>();

        // Tenta abrir o ficheiro
        try {
            // Se conseguir, cria um scanner para o ficheiro
            fileScan = new Scanner(file);

            // Avança o scanner para a linha onde começa a lista de palavras
            for (int i = 0; i < size; i++) {
                String line = fileScan.nextLine();

                // Verifica se há linhas vazias
                if (line.length() == 0) {
                    System.out.println("ERROR: Empty line found on soup");
                    System.exit(1);
                }

                // Verificações para verificar se a sopa de letras é válida
                if (line.length() != size) {
                    System.out.println("ERROR: Invalid soup");
                    System.exit(1);
                }

                for (int j = 0; j < size; j++) {
                    if (!Character.isAlphabetic(line.charAt(j)) || !Character.isUpperCase(line.charAt(j))) {
                        System.out.println("ERROR: Invalid soup");
                        System.exit(1);
                    }
                }
            }

            // Esta variável fará com que seja apenas verificada a linha seguinte ao suposto término da sopa de letras
            boolean verificar = false;
            
            // Enquanto houver linhas no ficheiro
            while (fileScan.hasNextLine()) {
                // Lê a linha
                String line = fileScan.nextLine();

                // Verifica se há linhas vazias
                if (line.length() == 0) {
                    System.out.println("ERROR: Empty line found on word list");
                    System.exit(1);
                }

                // Verificar se a linha a seguir ao suposto término da sopa de letras ainda faria parte da mesma, sendo assim uma sopa não quadrada, o que não é permitido
                if (verificar == false) {
                    if (line.length() == size ) {
                        for (int j = 0; j < size; j++) {
                            if (Character.isAlphabetic(line.charAt(j)) && Character.isUpperCase(line.charAt(j))) {
                                System.out.println("ERROR: Invalid soup");
                                System.exit(1);
                            }
                        }
                    }
                    verificar = true;
                }

                // Separa a linha em palavras (separadas por vírgulas, espaços ou pontos e
                // vírgulas)
                String[] lineWords = line.split("[, ;]");

                // Para cada palavra
                for (int i = 0; i < lineWords.length; i++) {
                    String word = lineWords[i].toLowerCase();

                    // Se a palavra tiver menos de 3 caracteres, ignora-a
                    if (word.length() < 3) {
                        continue;
                    }

                    boolean validWord = true;
                    for (int charIndex = 0; charIndex < word.length(); charIndex++) {
                        // Se a palavra tiver caracteres que não sejam letras, ignora-a
                        if (!Character.isAlphabetic(word.charAt(charIndex))) {
                            System.out.printf(
                                    "Warning: Word '%s' will be ignored for containing non-alphabetic characters \n", word);
                            validWord = false;
                            break;
                        }
                    }

                    if (validWord) {
                        words.add(word);
                    }
                }
            }

            // Fecha o scanner
            fileScan.close();
        } catch (FileNotFoundException e) {
            // Se não conseguir, imprime um erro e termina o programa
            System.out.println("ERROR: File not found");
            System.exit(1);
        }

        // Remove palavras que são substrings de outras e deixa a maior
        for (int i = 0; i < words.size(); i++) {
            String word1 = words.get(i);
            for (int j = 0; j < words.size(); j++) {
                String word2 = words.get(j);
                // se a palavra 1 for menor que a palavra 2 e a palavra 2 contiver a palavra 1
                if (word1.length() < word2.length() && word2.contains(word1)) {
                    words.remove(i);
                    i--;
                    break;
                }
            }
        }

        return words;
    }

    // Retorna uma matriz com a sopa de letras
    public Character[][] soupMatrix(File file, int size) throws FileNotFoundException {
        Scanner fileScan = null;

        // Cria uma matriz para guardar a sopa de letras
        Character[][] soup = new Character[size][size];

        // Tenta abrir o ficheiro
        try {
            // Se conseguir, cria um scanner para o ficheiro
            fileScan = new Scanner(file);

            // Para cada linha da sopa de letras
            for (int i = 0; i < size; i++) {
                // Lê a linha
                String line = fileScan.nextLine();

                // Verifica se a sopa de letras é válida
                if (line.length() != size) {
                    System.out.println("ERROR: Invalid soup");
                    System.exit(1);
                }

                // Para cada caracter da linha guarda o caracter na matriz
                for (int j = 0; j < size; j++) {
                    soup[i][j] = Character.toLowerCase(line.charAt(j));
                }
            }

            // Fecha o scanner
            fileScan.close();
        } catch (FileNotFoundException e) {
            // Se não conseguir, imprime um erro e termina o programa
            System.out.println("ERROR: File not found");
            System.exit(1);
        }  

        return soup;
    }

    public Direction checkMatch(Character[][] soup, String word, int row, int col) {
        Direction direction = Direction.NONE;

        // Check horizontal right
        if (col + word.length() <= soup[row].length) {
            boolean found = true;
            for (int i = 0; i < word.length(); i++) {
                if (soup[row][col + i] != word.charAt(i)) {
                    found = false;
                    break;
                }
            }
            if (found) {
                direction = Direction.Right;
                return direction;
            }
        }

        // Check horizontal left
        if (col >= word.length() - 1) {
            boolean found = true;
            for (int i = 0; i < word.length(); i++) {
                if (soup[row][col - i] != word.charAt(i)) {
                    found = false;
                    break;
                }
            }
            if (found) {
                direction = Direction.Left;
                return direction;
            }
        }

        // Check vertical down
        if (row + word.length() <= soup.length) {
            boolean found = true;
            for (int i = 0; i < word.length(); i++) {
                if (soup[row + i][col] != word.charAt(i)) {
                    found = false;
                    break;
                }
            }
            if (found) {
                direction = Direction.Down;
                return direction;
            }
        }

        // Check vertical up
        if (row >= word.length() - 1) {
            boolean found = true;
            for (int i = 0; i < word.length(); i++) {
                if (soup[row - i][col] != word.charAt(i)) {
                    found = false;
                    break;
                }
            }
            if (found) {
                direction = Direction.Up;
                return direction;
            }
        }

        // Check diagonal down-right
        if (col + word.length() <= soup[row].length && row + word.length() <= soup.length) {
            boolean found = true;
            for (int i = 0; i < word.length(); i++) {
                if (soup[row + i][col + i] != word.charAt(i)) {
                    found = false;
                    break;
                }
            }
            if (found) {
                direction = Direction.DownRight;
                return direction;
            }
        }

        // Check diagonal down-left
        if (col >= word.length() - 1 && row + word.length() <= soup.length) {
            boolean found = true;
            for (int i = 0; i < word.length(); i++) {
                if (soup[row + i][col - i] != word.charAt(i)) {
                    found = false;
                    break;
                }
            }
            if (found) {
                direction = Direction.DownLeft;
                return direction;
            }
        }

        // Check diagonal up-right
        if (col + word.length() <= soup[row].length && row >= word.length() - 1) {
            boolean found = true;
            for (int i = 0; i < word.length(); i++) {
                if (soup[row - i][col + i] != word.charAt(i)) {
                    found = false;
                    break;
                }
            }
            if (found) {
                direction = Direction.UpRight;
                return direction;
            }
        }

        // Check diagonal up-left
        if (col >= word.length() - 1 && row >= word.length() - 1) {
            boolean found = true;
            for (int i = 0; i < word.length(); i++) {
                if (soup[row - i][col - i] != word.charAt(i)) {
                    found = false;
                    break;
                }
            }
            if (found) {
                direction = Direction.UpLeft;
                return direction;
            }
        }

        return direction;
    }

    public void findWords(Character[][] soup, ArrayList<String> words, String fileName) throws IOException {
        PrintWriter saveFile = null;

        // Tenta criar um ficheiro para guardar os resultados
        try {
            // Cria um ficheiro para guardar os resultados
            FileWriter file = new FileWriter(fileName + "_results.txt");
            saveFile = new PrintWriter(file);

            // Cria uma cópia da sopa de letras
            Character[][] soupCopy = new Character[soup.length][soup[0].length];
            for (int i = 0; i < soup.length; i++) {
                for (int j = 0; j < soup.length; j++) {
                    soupCopy[i][j] = soup[i][j];
                }
            }

            // Para cada palavra da lista de palavras
            for (int i = 0; i < words.size(); i++) {
                String word = words.get(i);
                // Para cada posição da sopa de letras
                for (int row = 0; row < soup.length; row++) {
                    for (int col = 0; col < soup.length; col++) {
                        Direction direction = checkMatch(soup, word, row, col);
                        String directionString = direction.toString();
                        // Se a palavra for encontrada, marca as letras na cópia da sopa de letras
                        if (direction != Direction.NONE) {
                            saveFile.printf("%-30s %-5d %-8s %-10s\n", word, word.length(), (row + 1) + "," + (col + 1), directionString);
                            markLetters(soupCopy, word, row, col, directionString);
                        }
                    }
                }
            }

            saveFile.println();

            // Substitui as letras não pertencentes a nenhuma palavra por "."
            for (int row = 0; row < soupCopy.length; row++) {
                for (int col = 0; col < soupCopy.length; col++) {
                    if (soupCopy[row][col] != '.') {
                        saveFile.print(". ");
                    } else {
                        saveFile.printf("%s ", Character.toUpperCase(soup[row][col]));
                    }
                }
                saveFile.println();
            }

            saveFile.close();
        } catch (Exception e) {
            // Se não conseguir criar o ficheiro, termina o programa
            System.out.println("ERROR: Could not create file");
            System.exit(1);
        }
    }

    // Marca as letras da palavra na sopa de letras
    private void markLetters(Character[][] soup, String word, int row, int col, String direction) {
        int length = word.length();
        int deltaRow = 0, deltaCol = 0;

        // Calcula o deslocamento de linha e coluna
        switch (direction) {
            // Direções horizontais
            case "Right":
                deltaCol = 1;
                break;
            case "Left":
                deltaCol = -1;
                break;
            // Direções verticais
            case "Down":
                deltaRow = 1;
                break;
            case "Up":
                deltaRow = -1;
                break;
            // Direções diagonais
            case "UpLeft":
                deltaRow = -1;
                deltaCol = -1;
                break;
            case "UpRight":
                deltaRow = -1;
                deltaCol = 1;
                break;
            case "DownLeft":
                deltaRow = 1;
                deltaCol = -1;
                break;
            case "DownRight":
                deltaRow = 1;
                deltaCol = 1;
                break;
        }

        // Marca as letras da palavra
        for (int i = 0; i < length; i++) {
            soup[row][col] = '.';
            // Atualiza a posição
            row += deltaRow;
            col += deltaCol;
        }
    }
}

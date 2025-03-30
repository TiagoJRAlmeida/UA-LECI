package lab01;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Scanner;

public class impWSGenerator {
    public ArrayList<String> wordsToFind(File file, int size) throws FileNotFoundException {
        Scanner fileScan = null;

        // Cria um ArrayList para guardar as palavras
        ArrayList<String> words = new ArrayList<String>();

        // Tenta abrir o ficheiro
        try {
            // Cria um scanner para ler o ficheiro
            fileScan = new Scanner(file);

            // Enquanto houver linhas no ficheiro
            while (fileScan.hasNextLine()) {
                // Lê a linha
                String line = fileScan.nextLine();

                // Se a linha estiver vazia, termina o programa
                if (line.length() == 0) {
                    System.out.println("ERROR: Empty line found on word list");
                    System.exit(1);
                }

                // Separa a linha em palavras (separadas por vírgulas, espaços ou pontos e vírgulas)
                String[] lineWords = line.split("[, ;]");

                // Para cada palavra
                for (int i = 0; i < lineWords.length; i++) {
                    String word = lineWords[i].toLowerCase();

                    // Se a palavra tiver menos de 3 caracteres, o programa acaba
                    if (word.length() < 3) {
                        System.out.println("Warning: Word '" + word + "' is too short");
                        System.exit(1);
                    }

                    // Se a palavra tiver mais caracteres que o tamanho da sopa, o programa acaba
                    if (word.length() > size) {
                        System.out.println("Warning: Word '" + word + "' is too long for the soup size");
                        System.exit(1);
                    }

                    boolean validWord = true;
                    for (int charIndex = 0; charIndex < word.length(); charIndex++) {
                        // Se a palavra tiver caracteres que não sejam letras, ignora-a
                        if (!Character.isAlphabetic(word.charAt(charIndex))) {
                            System.out.printf("Warning: Word '%s' will be ignored for containing non-alphabetic characters \n", word);
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

    public boolean writeToFile(String fileName,Character[][] soup, ArrayList<String> words) throws IOException {
        PrintWriter saveFile = null;

        // Tenta criar o ficheiro
        try {
            // Cria um PrintWriter para escrever no ficheiro
            FileWriter file = new FileWriter(fileName);
            saveFile = new PrintWriter(file);

            // Escreve a sopa de letras no ficheiro
            for(int i = 0 ; i<soup.length ;i++){
                for(int j = 0 ; j<soup.length ; j++)
                    saveFile.printf("%s", soup[i][j]);
                saveFile.println();
            }

            // Escreve as palavras no ficheiro
            for(String word : words){
                saveFile.printf("%s,", word);
            }

            saveFile.close();
        } catch (Exception e) {
            // Se não conseguir criar o ficheiro, termina o programa
            System.out.println("ERROR: Could not create file");
            System.exit(1);
        }

        return true;
    }

    public Character[][] createRandomSoup(ArrayList<String> words, int size) {
        // Cria a sopa de letras
        Character[][] soup = new Character[size][size];

        // Preenche a sopa com letras aleatórias
        for (int i = 0; i < soup.length; i++) {
            for (int j = 0; j < soup.length; j++) {
                soup[i][j] = Character.toUpperCase((char) (Math.random() * 26 + 'a'));
            }
        }

        return soup;
    }

    public Character[][] putWordsOnSoup(Character[][] soup, ArrayList<String> words) {
        //Array de posições já usadas
        ArrayList<Position> usedPositions = new ArrayList<Position>();

        int x = 0, y = 0;
        Direction direction = Direction.NONE;

        for (String word : words) {

            boolean validPosition = false;
            int times = 0;
            while (!validPosition) {
                if (times > 1000) {
                    System.out.println("ERROR: Could not find a valid position for word '" + word + "'");
                    System.exit(1);
                }
                
                times++;
                // Escolhe uma posição aleatória (apenas adicionamos 1 para melhor raciocinio  por fim subtrairemos 1) e uma direção aleatória
                x = (int) (Math.random() * (soup.length-1));
                y = (int) (Math.random() * (soup.length-1));
                direction = Direction.values()[(int) (Math.random() * 7)];

                switch (direction) {
                    // Se a direção for para a direita
                    case Up:
                        // Se a posição for válida
                        if (y - word.length() >= -1) {
                            // Verifica se as posições que a palavra vai ocupar já estão ocupadas
                            for (int i = 0; i < word.length(); i++) {
                                // Se estiverem ocupadas, a posição não é válida
                                if (usedPositions.contains(new Position(x, y - i)) && soup[x][y - i] != Character.toUpperCase(word.charAt(i))) {
                                    validPosition = false;
                                    break;
                                } else {
                                    validPosition = true;
                                }
                            }
                        }

                        break;
                    // Se a direção for para a esquerda
                    case Down:
                        // Se a posição for válida
                        if (y + word.length() <= soup.length) {
                            // Verifica se as posições que a palavra vai ocupar já estão ocupadas
                            for (int i = 0; i < word.length(); i++) {
                                // Se estiverem ocupadas, a posição não é válida
                                if (usedPositions.contains(new Position(x, y + i)) && soup[x][y + i] != Character.toUpperCase(word.charAt(i))) {
                                    validPosition = false;
                                    break;
                                } else {
                                    validPosition = true;
                                }
                            }
                        } 

                        break;
                    // Se a direção for para cima
                    case Left:
                        // Se a posição for válida
                        if (x - word.length() >= -1) {
                            // Verifica se as posições que a palavra vai ocupar já estão ocupadas
                            for (int i = 0; i < word.length(); i++) {
                                // Se estiverem ocupadas, a posição não é válida
                                if (usedPositions.contains(new Position(x - i, y)) && soup[x - i][y] != Character.toUpperCase(word.charAt(i))) {
                                    validPosition = false;
                                    break;
                                } else {
                                    validPosition = true;
                                }
                            }
                        }

                        break;
                    // Se a direção for para baixo
                    case Right:
                        // Se a posição for válida
                        if (x + word.length() <= soup.length) {
                            // Verifica se as posições que a palavra vai ocupar já estão ocupadas
                            for (int i = 0; i < word.length(); i++) {
                                // Se estiverem ocupadas, a posição não é válida
                                if (usedPositions.contains(new Position(x + i, y)) && soup[x + i][y] != Character.toUpperCase(word.charAt(i))) {
                                    validPosition = false;
                                    break;
                                } else {
                                    validPosition = true;
                                }
                            }
                        }

                        break;
                    // Se a direção for para cima e para a direita
                    case UpLeft:
                        // Se a posição for válida
                        if (y - word.length() >= -1 && x - word.length() >= -1) {
                            // Verifica se as posições que a palavra vai ocupar já estão ocupadas
                            for (int i = 0; i < word.length(); i++) {
                                // Se estiverem ocupadas, a posição não é válida
                                if (usedPositions.contains(new Position(x - i, y - i)) && soup[x - i][y - i] != Character.toUpperCase(word.charAt(i))) {
                                    validPosition = false;
                                    break;
                                } else {
                                    validPosition = true;
                                }
                            }
                        }

                        break;
                    // Se a direção for para baixo e para a esquerda
                    case DownLeft:
                        // Se a posição for válida
                        if (y + word.length() <= soup.length && x - word.length() >= -1) {
                            // Verifica se as posições que a palavra vai ocupar já estão ocupadas
                            for (int i = 0; i < word.length(); i++) {
                                // Se estiverem ocupadas, a posição não é válida
                                if (usedPositions.contains(new Position(x - i, y + i)) && soup[x - i][y + i] != Character.toUpperCase(word.charAt(i))) {
                                    validPosition = false;
                                    break;
                                } else {
                                    validPosition = true;
                                }
                            }
                        }

                        break;
                    // Se a direção for para cima e para a esquerda
                    case UpRight:
                        // Se a posição for válida
                        if (y - word.length() >= -1 && x + word.length() <= soup.length) {
                            // Verifica se as posições que a palavra vai ocupar já estão ocupadas
                            for (int i = 0; i < word.length(); i++) {
                                // Se estiverem ocupadas, a posição não é válida
                                if (usedPositions.contains(new Position(x + i, y - i)) && soup[x + i][y - i] != Character.toUpperCase(word.charAt(i))) {
                                    validPosition = false;
                                    break;
                                } else {
                                    validPosition = true;
                                }
                            }
                        }

                        break;
                    // Se a direção for para baixo e para a direita
                    case DownRight:
                        // Se a posição for válida
                        if (y + word.length() <= soup.length && x + word.length() <= soup.length) {
                            // Verifica se as posições que a palavra vai ocupar já estão ocupadas
                            for (int i = 0; i < word.length(); i++) {
                                // Se estiverem ocupadas, a posição não é válida
                                if (usedPositions.contains(new Position(x + i, y + i)) && soup[x + i][y + i] != Character.toUpperCase(word.charAt(i))) {
                                    validPosition = false;
                                    break;
                                } else {
                                    validPosition = true;
                                }
                            }
                        }

                        break;
                    case NONE:
                        break;
                }
            }

            // Se a posição for válida, a palavra é colocada na sopa
            for (int i = 0; i < word.length(); i++) {
                switch (direction) {
                    // Se a direção for para a direita
                    case Up:
                        // Adiciona a posição à lista de posições ocupadas
                        usedPositions.add(new Position(x, y - i));

                        // Coloca a letra maiúscula na sopa
                        soup[x][y - i] = Character.toUpperCase(word.charAt(i));
                        break;
                    // Se a direção for para a esquerda
                    case Down:
                        // Adiciona a posição à lista de posições ocupadas
                        usedPositions.add(new Position(x, y + i));

                        // Coloca a letra maiúscula na sopa
                        soup[x][y + i] = Character.toUpperCase(word.charAt(i));
                        break;
                    // Se a direção for para cima
                    case Left:
                        // Adiciona a posição à lista de posições ocupadas
                        usedPositions.add(new Position(x - i, y));

                        // Coloca a letra maiúscula na sopa
                        soup[x - i][y] = Character.toUpperCase(word.charAt(i));
                        break;
                    // Se a direção for para baixo
                    case Right:
                        // Adiciona a posição à lista de posições ocupadas
                        usedPositions.add(new Position(x + i, y));

                        // Coloca a letra maiúscula na sopa
                        soup[x + i][y] = Character.toUpperCase(word.charAt(i));
                        break;
                    // Se a direção for para cima e para a direita
                    case UpLeft:
                        // Adiciona a posição à lista de posições ocupadas
                        usedPositions.add(new Position(x - i, y - i));

                        // Coloca a letra maiúscula na sopa
                        soup[x - i][y - i] = Character.toUpperCase(word.charAt(i));
                        break;
                    // Se a direção for para baixo e para a esquerda
                    case DownLeft:
                        // Adiciona a posição à lista de posições ocupadas
                        usedPositions.add(new Position(x - i, y + i));

                        // Coloca a letra maiúscula na sopa
                        soup[x - i][y + i] = Character.toUpperCase(word.charAt(i));
                        break;
                    // Se a direção for para cima e para a esquerda
                    case UpRight:
                        // Adiciona a posição à lista de posições ocupadas
                        usedPositions.add(new Position(x + i, y - i));

                        // Coloca a letra maiúscula na sopa
                        soup[x + i][y - i] = Character.toUpperCase(word.charAt(i));
                        break;
                    case DownRight:
                        // Adiciona a posição à lista de posições ocupadas
                        usedPositions.add(new Position(x + i, y + i));

                        // Coloca a letra maiúscula na sopa
                        soup[x + i][y + i] = Character.toUpperCase(word.charAt(i));
                        break;
                    case NONE:
                        break;
                }
            }
        }

        return soup;
    }
}

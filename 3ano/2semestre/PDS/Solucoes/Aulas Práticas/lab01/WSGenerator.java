package lab01;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class WSGenerator {
    public static void main(String[] args) throws FileNotFoundException {
        // Verifica se o número de argumentos é válido
        if (args.length < 4) {
            System.out.println("Usage: java lab01/WSGenerator -i lab01/<wordlist> -s <soupsize> optional(-o lab01/<outputfile>)");
            System.exit(1);
        }

        // Cria um ArrayList para guardar as opções
        List<Option> optsList = new ArrayList<Option>();

        int useOptI = 0, useOptS = 0, useOptO = 0;

        // Para cada argumento
        for (int i = 0; i < args.length; i++) {
            // Se o argumento começar por um hífen
            if(args[i].charAt(0) == '-') {
                // Se o argumento for válido
                if (args[i].charAt(1) == 'i' || args[i].charAt(1) == 's' || args[i].charAt(1) == 'o') {
                    if (args[i].length() < 2) {
                        throw new IllegalArgumentException("Not a valid option: "+args[i]);
                    } else {
                        if (args.length-1 == i) {
                            throw new IllegalArgumentException("Expected argument after: "+args[i]);
                        }

                        switch(args[i].charAt(1)) {
                            // Se a opção for -i, verifica se o ficheiro tem a extensão .txt e se já foi usada
                            case 'i':
                                useOptI++;
                                if (useOptI > 1) {
                                    throw new IllegalArgumentException("Option -i can only be used once");
                                }

                                if (!args[i+1].endsWith(".txt")) {
                                    throw new IllegalArgumentException("Expected .txt file after: "+args[i]);
                                }
                                break;
                            // Se a opção for -s, verifica se o argumento é um inteiro e se esta opção já foi usada
                            case 's':
                                useOptS++;
                                if (useOptS > 1) {
                                    throw new IllegalArgumentException("Option -s can only be used once");
                                }

                                try {
                                    Integer.parseInt(args[i+1]);
                                } catch (NumberFormatException e) {
                                    throw new IllegalArgumentException("Expected integer after: "+args[i]);
                                }
                                break;
                            // Se a opção for -o, verifica se o ficheiro tem a extensão .txt, se o nome do ficheiro de output é diferente do nome do ficheiro de palavras e se esta opção já foi usada
                            case 'o':
                                useOptO++;
                                if (useOptO > 1) {
                                    throw new IllegalArgumentException("Option -o can only be used once");
                                }

                                if (!args[i+1].endsWith(".txt")) {
                                    throw new IllegalArgumentException("Expected .txt file after: "+args[i]);
                                }

                                for (Option opt : optsList) {
                                    if (opt.getOpt().equals("-i")) {
                                        if (args[i+1].equals(opt.getArg())) {
                                            throw new IllegalArgumentException("Expected different file name after: "+args[i]);
                                        }
                                    }
                                }
                                break;
                        }
                        // Adiciona a opção ao ArrayList
                        optsList.add(new Option(args[i], args[i+1]));
                        i++;
                    }
                } else {
                    // Se o argumento não for válido, termina o programa
                    throw new IllegalArgumentException("Not a valid option");
                }
            }
        }

        int size = 0;
        String saveFileName = null;
        String wordListFileName = null;

        for (Option opt : optsList) {
            if (opt.getOpt().equals("-i")) {
                wordListFileName = opt.getArg();
            } else if (opt.getOpt().equals("-s")) {
                size = Integer.parseInt(opt.getArg());
            } else if (opt.getOpt().equals("-o")) {
                saveFileName = opt.getArg();
            }
        }

        File soupFile = null;

        // Tenta ler o ficheiro
        try {
            // Verifica se o ficheiro existe
            soupFile = new File(wordListFileName);
        } catch (Exception e) {
            // Se não conseguir ler o ficheiro, termina o programa
            System.out.println("ERROR: Invalid file");
            System.exit(1);
        }

        // Cria uma instância da classe WSGenerator
        impWSGenerator wsGenerator = new impWSGenerator();
        
        // Cria a sopa de letras
        ArrayList<String> words = wsGenerator.wordsToFind(soupFile, size);
        Character[][] randomSoup = wsGenerator.createRandomSoup(words, size);
        Character[][] soup = wsGenerator.putWordsOnSoup(randomSoup, words);

        // Se o nome do ficheiro de output for diferente de null, escreve a sopa de letras e as palavras no ficheiro
        if (saveFileName != null) {
            try {
                wsGenerator.writeToFile(saveFileName, soup, words);
            } catch (IOException e) {
                System.out.println("ERROR: Could not write to file");
                System.exit(1);
            }
        // Se o nome do ficheiro de output for igual a null, escreve a sopa de letras e as palavras no ecrã
        } else {
            for (int i = 0; i < soup.length; i++) {
                for (int j = 0; j < soup.length; j++) {
                    System.out.printf("%s", soup[i][j]);
                }
                System.out.println();
            }

            for (String word : words) {
                System.out.printf("%s,", word);
            }
            System.out.println();
        }
    }
}

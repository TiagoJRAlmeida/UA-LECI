package lab03.SistemaReservas;

import java.io.FileNotFoundException;
import java.io.*;
import java.util.ArrayList;
import java.util.*;
import java.util.Scanner;

public class Main {
    
    static boolean hasExecutive = true;
    public static void main(String[] args) throws FileNotFoundException {
        char option = 'A';
        String[] input = null;
        Scanner sc = new Scanner(System.in);
        
        do {
            System.out.printf("Selecione uma opção: (H para ajuda)\n");
            input = sc.nextLine().split(" ");
            
            option = input[0].charAt(0); 
            
            switch (option) {
                case 'H':
                    
                    Display.printInfoH();
                    break;
                
                case 'I':

                    ArrayList<String> reservations = ReadFile(input[1]);
                    
                    if (hasExecutive) {
                        int numLugFilaExec = Integer.valueOf(reservations.get(1).split("x")[1]);
                        int numFilasExec = Integer.valueOf(reservations.get(1).split("x")[0]);
    
                        int numLugFilaTou = Integer.valueOf(reservations.get(2).split("x")[1]);
                        int numFilasTou = Integer.valueOf(reservations.get(2).split("x")[0]);

                        Aviao aviao = new Aviao(numLugFilaTou, numLugFilaExec, numFilasTou, numFilasExec);
                        Voo codigoVoo = new Voo(reservations.get(0), aviao);
                        Display.printInfoI(codigoVoo, aviao, reservations);
                    }
                    else {
                        int numLugFilaTou = Integer.valueOf(reservations.get(1).split("x")[1]);
                        int numFilasTou = Integer.valueOf(reservations.get(1).split("x")[0]);

                        Aviao aviao = new Aviao(numLugFilaTou, 0, numFilasTou, 0);
                        Voo codigoVoo = new Voo(reservations.get(0), aviao);
                        Display.printInfoI(codigoVoo, aviao, reservations);
                    }

                    
                    break;
                
                case 'M':
                    break;
                
                case 'F':

                    if (input.length == 4) {
                        
                        int numLugFilaExec = Integer.valueOf(input[2].split("x")[1]);
                        int numFilasExec = Integer.valueOf(input[2].split("x")[0]);
    
                        int numLugFilaTou = Integer.valueOf(input[3].split("x")[1]);
                        int numFilasTou = Integer.valueOf(input[3].split("x")[0]);
                        
                        Voo vooF = new Voo(input[1], new Aviao(numLugFilaTou, numLugFilaExec, numFilasTou, numFilasExec));
                        Display.printInfoF(vooF);
                    }
                
                    if (input.length == 3) {
    
                        int numLugFilaTou = Integer.valueOf(input[2].split("x")[1]);
                        int numFilasTou = Integer.valueOf(input[2].split("x")[0]);
                        
                        Voo vooF = new Voo(input[1], new Aviao(numLugFilaTou, 0, numFilasTou, 0));
                        Display.printInfoF(vooF);
                    }
                    break;
                    
                case 'R':
                    break;

                case 'C':

                    Display.printInfoC(input[1]);
                    break;
                
            }
        }
        while(option != 'Q');
        sc.close();
    }

   

    public static ArrayList<String> ReadFile(String filename) { 
        
        int controlo = 0;
        ArrayList<String>  reservations = new ArrayList<String>();
        
        try {
            
            Scanner fileReader = new Scanner(new FileReader("lab03/SistemaReservas/"+filename)); 
            while(fileReader.hasNextLine()) {
                
                if (controlo == 0) {
                    String[] flightInfo = (fileReader.nextLine().replace(">", "")).split(" ");
                    
                    if (flightInfo.length == 3) {
                        reservations.add(flightInfo[0]);
                        reservations.add(flightInfo[1]);
                        reservations.add(flightInfo[2]);
                        controlo = 1;
                    }

                    if (flightInfo.length == 2) {
                        hasExecutive = false;
                        reservations.add(flightInfo[0]);
                        reservations.add(flightInfo[1]);
                        controlo = 1;
                    }
                    
                    
                }
                else {
                    String[] flightInfo = fileReader.nextLine().split(" ");
                    reservations.add(flightInfo[0]);
                    reservations.add(flightInfo[1]);
                }
            }
        } catch (FileNotFoundException e) { 
            System.err.println("ERRO: ficheiro não encontrado!");
            System.exit(1);
        }
        return reservations;
    }
}
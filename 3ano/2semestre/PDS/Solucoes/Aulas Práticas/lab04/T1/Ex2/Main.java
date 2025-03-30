import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        ArrayList<String> flights = new ArrayList<>();
        ArrayList<ArrayList<String>> arrangements = new ArrayList<>();
        Scanner sc = new Scanner(System.in);
        boolean exit = false;
        while (!exit) {
            System.out.println("\nProgram options:\n" + 
                            "- H: Apresenta este menu.\n" + 
                            "- I filename: Le um ficheiro de texto contento informacao sobre um voo.\n" +
                            "- M flight_code: Exibe o mapa das reservas do voo especificado.\n" +
                            "- F flight_code num_seats_executive num_seats_touristoptional: Acrescenta um novo voo.\n" +
                            "- R flight_code class number_seats: Acrescenta uma nova reserva a um voo.\n" +
                            "- C reservation_code: Cancela uma reserva.\n" +
                            "- Q: Termina o programa.\n");
            String [] op = sc.nextLine().split(" ");
            switch (op[0].toUpperCase()) {
                case "H":
                    break;
                case "I":
                    if (op.length != 2) {
                        System.out.println("Input invalido. Ex: I filename");
                    } else {
                        optionI(op[1]);
                    }
                    break;
                case "M":
                    if (op.length != 2) {
                        System.out.println("Input invalido. Ex: M flight_code");
                    } else {
                        optionM(op[1], arrangements, flights);
                    }
                    break;
                case "F":
                    optionF(flights, arrangements, sc);
                    break;
                case "R":
                    if (op.length == 4 || op.length == 6) {
                        optionR(op, flights, arrangements);
                    } else {
                        System.out.println("Input invalido. Ex: R light_code class number_seats");
                    }
                    break;
                case "C":
                    if (op.length != 2) {
                        System.out.println("Input invalido. Ex: C reservation_code");
                    } else {
                        String []options = op[1].split(":");
                        String code = options[0];
                        String numR = options[1];
                        optionC(flights, arrangements, code, numR);
                    }
                    break;
                case "Q":
                    exit = true;
                    break;
                default:
                    System.out.println("Opcao nao disponivel.");
            }
        }
    }

    public static void optionI(String filename) throws IOException {
        File file = new File("./" + filename);
        BufferedReader read = new BufferedReader(new FileReader((file)));
        String info[] = read.readLine().split(" ");
        if (info.length == 3) {
            String infoE[] = info[1].split("x"), infoT[] = info[2].split("x"), line;
            int totalE = Integer.parseInt(infoE[0])*Integer.parseInt(infoE[1]), totalT = Integer.parseInt(infoT[0])*Integer.parseInt(infoT[1]);
            int remainingE = totalE, remainingT = totalT;
            System.out.printf("Codigo de voo %s. Lugares disponiveis: %d em classe Executiva; %d lugares em classe Turistica.\n", info[0].replace(">", ""), totalE, totalT);
            while ((line = read.readLine()) != null) {
                String[] data = line.split(" ");
                if (data[0].equals("T")) {
                    remainingT = remainingT-Integer.parseInt(data[1]);
                    if (remainingT < 0) {
                        System.out.println("Nao foi possivel obter lugares para a reserva: T " + data[1]);
                        break;
                    }
                }
                if (data[0].equals("E")) {
                    remainingE = remainingE-Integer.parseInt(data[1]);
                    if (remainingE < 0) {
                        System.out.println("Nao foi possivel obter lugares para a reserva: E " + data[1]);
                        break;
                    }
                }
            }
            read.close();
        }
        else if (info.length == 2) {
            String[] seatsT = info[1].split("x");
            int totalT = Integer.parseInt(seatsT[0]) * Integer.parseInt(seatsT[1]);
            int remainingT = totalT;
            String line;
            System.out.printf("Codigo de voo %s. Lugares disponiveis: %d lugares em classe Turistica.\nClasse executiva nao disponivel neste voo.\n", info[0].replace(">", ""), totalT);
            while ((line = read.readLine()) != null) {
                String[] data = line.split(" ");
                if (data[0].equals("T")) {
                    remainingT = remainingT - Integer.parseInt(data[1]);
                    if (remainingT < 0) {
                        System.out.println("Nao foi possivel obter lugares para a reserva: E " + data[1]);
                        break;
                    }
                }
            }
            read.close();
        }
        else {
            System.out.println("Ficheiro não encontrado");
            read.close();
        }
    }
    public static void optionM(String code, ArrayList<ArrayList<String>> arrangements, ArrayList<String> flights) {
        int index = -1;
        int index2 = flights.indexOf(code);
        for (int i=0; i<arrangements.size(); i++) {
            if (arrangements.get(i).contains(code)){
                index = i;
            }
        }
        if (index == -1 ) {
           System.out.println("Invalid code.");
        } else {
            int totalQueues = Integer.parseInt(String.valueOf(flights.get(index2+1))) + Integer.parseInt(String.valueOf(flights.get(index2+3)));
            int maxSeats = Math.max(Integer.parseInt(String.valueOf(flights.get(index2+2))), Integer.parseInt(String.valueOf(flights.get(index2+4))));
            String alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            System.out.print("  ");
            for (int i=1; i<=totalQueues; i++) System.out.print(i + " ");
            System.out.println();
            for (int i=1; i<= maxSeats; i++) {
                System.out.print(alpha.charAt(i-1) + " ");
                for (int j=0; j<totalQueues; j++) {
                    System.out.print(arrangements.get(index).get(j*maxSeats+i) + " ");
                }
                System.out.println();
            }
        }
    }
    public static void optionF(ArrayList<String> flights, ArrayList<ArrayList<String>> arrangements, Scanner sc) {
        System.out.println("Insira o codigo do voo:");
        String code = sc.nextLine();
        if (flights.contains(code) && (flights.indexOf(code)%5 == 0)) {
            System.out.println("This code already exists.");
        } else {
            System.out.println("Insira o numero de filas da classe Executiva (0 se nao existir a classe):");
            int queuesE = sc.nextInt();
            System.out.println("Insira o numero de assentos por fila da classe executiva (0 se nao existir a classe:");
            int seatsE = sc.nextInt();
            System.out.println("Insira o numero de filas da classe Turistica:");
            int queuesT = sc.nextInt();
            System.out.println("Insira o numero de assentos por fila da classe Turistica:");
            int seatsT = sc.nextInt();
            if (optionFValidation(queuesE, seatsE, queuesT, seatsT)) {
                new Voo(code, Integer.parseInt(String.valueOf(queuesT)), Integer.parseInt(String.valueOf(seatsT)), Integer.parseInt(String.valueOf(queuesE)), Integer.parseInt(String.valueOf(seatsE)), flights, arrangements);
            }
        }
        System.out.println(flights);
    }
    public static boolean optionFValidation(int queuesE, int seatsE, int queuesT, int seatsT) {
        boolean flag = true;
        if (queuesE < 0 || seatsE < 0 || seatsT <= 0 || queuesT <= 0) {
            System.out.println("Invalid input.");
            flag = false;
        }
        if (queuesE != 0 && seatsE == 0) {
            System.out.println("Business class without seats.");
            flag = false;
        }
        if (queuesE == 0 && seatsE != 0) {
            System.out.println("Business class with seats.");
            flag = false;
        }
        if (queuesE > 10 || queuesT > 10) {
            System.out.println("Invalid number of queues.");
            flag = false;
        }
        if (seatsE > 8 || seatsT > 8) {
            System.out.println("Invalid number of seats.");
            flag = false;
        }
        return flag;
    }
    public static void optionR(String[] op,ArrayList<String> flights, ArrayList<ArrayList<String>> arrangements){
        if (!flights.contains(op[1])) {
            System.out.println("Invalid code.");
        } else {
            ArrayList<String> replaceArrangement = new ArrayList<>();
            String seatsE = flights.get(flights.indexOf(op[1]) + 4);
            String seatsT = flights.get(flights.indexOf(op[1]) + 2);
            int queuesE = Integer.parseInt(flights.get(flights.indexOf(op[1]) + 3));
            int queuesT = Integer.parseInt(flights.get(flights.indexOf(op[1]) + 1));
            int maxSeats = Math.max(Integer.parseInt(seatsE), Integer.parseInt(seatsT));
            int rE = 0; int rT = 0;
            List<String> options = new ArrayList<>((Arrays.asList(op)));
            if (options.contains("E")) {
                rE = Integer.parseInt(options.get(options.indexOf("E") + 1));
            }
            if (options.contains("T")) {
                rT = Integer.parseInt(options.get(options.indexOf("T") + 1));
            }
            int numR = 0;
            int counter;
            boolean flag = false;
            String alpha = "ABCDEFGH";
            ArrayList<String> seatsR = new ArrayList<>();
            for (int i=0; i<arrangements.size(); i++) {
                if (arrangements.get(i).contains(op[1])) {
                    replaceArrangement = arrangements.get(i);
                    for (int j=1; j< replaceArrangement.size(); j++) {
                        if (!arrangements.get(i).get(j).equals(" ") && Integer.parseInt(arrangements.get(i).get(j)) > numR) {
                            numR = Integer.parseInt(arrangements.get(i).get(j));
                        }
                    }
                    numR++;
                    if (rE != 0) {
                        int ind = searchEmptyQueue(maxSeats, seatsE, queuesE,  queuesT, "E", replaceArrangement);
                        flag = false;
                        counter = 0;
                        int cicleS = 0;
                        int cicleQ = 1;

                        if (ind != -1 && rE <= Integer.parseInt(seatsE)) {
                            for (int k = ind; k <= (queuesE * maxSeats); k++) {
                                cicleQ = ind/maxSeats+1;
                                if (cicleS == maxSeats) {
                                    cicleS = 0;
                                    cicleQ++;
                                }
                                if (replaceArrangement.get(k).equals("0") && (counter < rE)) {
                                    counter++;
                                    replaceArrangement.set(k, String.valueOf(numR));
                                    String temp = String.valueOf(cicleQ) + alpha.charAt(cicleS);
                                    seatsR.add(temp);
                                }
                                cicleS++;
                            }
                        }
                        else {
                            for (int k = 1; k <= (queuesE * maxSeats); k++) {
                                if (cicleS == maxSeats) {
                                    cicleS = 0;
                                    cicleQ++;
                                }
                                if (replaceArrangement.get(k).equals("0") && (counter < rE)) {
                                    counter++;
                                    replaceArrangement.set(k, String.valueOf(numR));
                                    String temp = String.valueOf(cicleQ) + alpha.charAt(cicleS);
                                    seatsR.add(temp);
                                }
                                cicleS++;
                            }
                        }
                        if (counter == rE) {
                            flag = true;
                        }
                    }
                    if (rT != 0) {
                        int ind = searchEmptyQueue(maxSeats, seatsT, queuesE,  queuesT, "T", replaceArrangement);
                        flag = false;
                        counter = 0;
                        int cicleS = 0;
                        int cicleQ = 1;

                        if (ind != -1 && rT <= Integer.parseInt(seatsT)) {
                            cicleQ = ind/maxSeats+1;
                            for (int k = ind; k <= ((queuesE + queuesT) * maxSeats); k++) {
                                if (cicleS == maxSeats) {
                                    cicleS = 0;
                                    cicleQ++;
                                }
                                if (replaceArrangement.get(k).equals("0") && (counter < rT)) {
                                    counter++;
                                    replaceArrangement.set(k, String.valueOf(numR));
                                    String temp = String.valueOf(cicleQ) + alpha.charAt(cicleS);
                                    seatsR.add(temp);
                                }
                                cicleS++;
                            }
                        } else {
                           for (int k = 1 + (queuesE * maxSeats); k <= ((queuesE + queuesT) * maxSeats); k++) {
                                if (cicleS == maxSeats) {
                                    cicleS = 0;
                                    cicleQ++;
                                }
                                if (replaceArrangement.get(k).equals("0") && (counter < rT)) {
                                    counter++;
                                    replaceArrangement.set(k, String.valueOf(numR));
                                    String temp = String.valueOf(cicleQ) + alpha.charAt(cicleS);
                                    seatsR.add(temp);
                                }
                                cicleS++;
                            }
                        }
                        if (counter == rT) {
                            flag = true;
                        }
                    }
                    if (flag) {
                        arrangements.set(i, replaceArrangement);
                        System.out.print(op[1] + ":" + numR + " = ");
                        for (int j=0; j <seatsR.size(); j++) {
                            if (j < (seatsR.size() - 1)) {
                                System.out.print(seatsR.get(j) + " | ");
                            } else {
                                System.out.print(seatsR.get(j) + "\n");
                            }
                        }
                    } else {
                        System.out.println("Reserva nao efetuada.");
                    }
                    break;
                }
            }
        }
    }
    public static int searchEmptyQueue(int maxSeats,  String seats, int queuesE,  int queuesT, String classe, ArrayList<String> replaceArrangements) {
        int index = -1;
        if (classe.equals("E")) {
            int counter = 0;
            int resetCounter = 0;
            for (int k=1; k<=(queuesE*maxSeats); k++) {
                if (!replaceArrangements.get(k).equals(" ")) {
                    if (replaceArrangements.get(k).equals("0")) {
                        counter++;
                    }
                }
                resetCounter++;
                if (resetCounter % maxSeats == 0) {
                    if (counter == Integer.parseInt(seats)) {
                        index = (k - maxSeats + 1);
                        return index;
                    }
                    resetCounter = 0;
                    counter = 0;
                }
            }
        }
        if (classe.equals("T")) {
            int counter = 0;
            int resetCounter = 0;
            for (int k=1+(queuesE*maxSeats); k<=((queuesE+queuesT)*maxSeats); k++) {
                if (!replaceArrangements.get(k).equals(" ")) {
                    if (replaceArrangements.get(k).equals("0")) {
                        counter++;
                    }
                }
                resetCounter++;
                if (resetCounter % maxSeats == 0) {
                    if (counter == Integer.parseInt(seats)) {
                        index = (k - maxSeats + 1);
                        return index;
                    }
                    resetCounter = 0;
                    counter = 0;
                }
            }
        }
        return index;
    }
    public static void optionC(ArrayList<String> flights, ArrayList<ArrayList<String>> arrangements, String code, String numR) {
        if (flights.contains(code)) {
            for (int i=0; i<arrangements.size(); i++) {
                if (arrangements.get(i).contains(code)) {
                    for (int k=1; k< arrangements.get(i).size(); k++) {
                        if (arrangements.get(i).get(k).equals(numR)) {
                            arrangements.get(i).set(k, "0");
                        }
                    }
                }
            }
        } else {
            System.out.println("Invalid code.");
        }
    }
}
package lab03.SistemaReservas;
import java.util.*;

public class Display {

    public static void printInfoH()  {
        System.out.printf("%-53s   %-25s\n", "H",  "Apresenta as opções do menu");
        System.out.printf("%-53s   %-25s\n", "I filename",  "Ler ficheiro com as informações sobre um voo");
        System.out.printf("%-53s   %-25s\n", "M flight_code ",  "Exibir mapa das reservas de um voo");
        System.out.printf("%-53s   %-25s\n", "F flight_code num_seats_executive num_seats_tourist",  "Acresenta um novo voo");
        System.out.printf("%-53s   %-25s\n", "R flight_code class number_seats",  "Acresenta uma nova reserva a um voo");
        System.out.printf("%-53s   %-25s\n", "C reservation_code",  "Cancelar um reserva");
        System.out.printf("%-53s   %-25s\n", "Q",  "Terminar o programa");
        System.out.println();
    }

    public static void printInfoI(Voo voo, Aviao aviao, ArrayList<String> reservations) {

        System.out.println(voo);
        Gestao.addReservas(aviao, voo, reservations);
        System.out.println();
    }
    
    /*public void printInfoM(String filename, Voo voo, Reservas reserva) {

        System.out.printf("  ");
        for (int i = 0; i <= (voo.getNumFilasExecutiva()+voo.getNumFilasTuristica()); i++){
            System.out.printf("  %d", i);
        }
        
        for (String lugar:reserva.getLugaresReservas().keySet()){
            System.out.printf("\n");
            System.out.printf("%d ", lugar);
            for (int i = 0; i <(voo.getNumFilasExecutiva()+voo.getNumFilasTuristica()); i++){
                if (reserva.getLugaresReservas().get(lugar).get(i) == null){
                    System.out.printf("  ");
                }
                else{
                    System.out.printf("%s ", reserva.getLugaresReservas().get(lugar).get(i));
                }
            }
            System.out.printf("\n");
        }
    }/* */

    public static void printInfoF(Voo voo) {
        System.out.println("Novo voo acresentada com susseco!");
        System.out.println(voo+"\n");
    }  
    
    
    

    public static void printInfoC(String codigoReserva) {
        
        Gestao.cancelarReserva(codigoReserva);
    }
}
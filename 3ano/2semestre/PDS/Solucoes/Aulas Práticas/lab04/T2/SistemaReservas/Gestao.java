package lab03.SistemaReservas;

import java.util.*;

public class Gestao {
    
    static HashMap<Voo, ArrayList<Reservas>> reservas = new HashMap<Voo, ArrayList<Reservas>>();
    
    
    public static void addReservas(Aviao aviao, Voo codigoVoo, ArrayList<String> reservations){
        
        HashMap<String, ArrayList<Integer>> informacao = new HashMap<String, ArrayList<Integer>>();
        ArrayList<Integer> reservasTouristica = new ArrayList<Integer>();
        ArrayList<Integer> reservasExecutiva = new ArrayList<Integer>();
        
        if (Main.hasExecutive) {
            for (int i=3; i<reservations.size(); i+=2){
                if(reservations.get(i).equals("T")){
                    reservasTouristica.add(Integer.valueOf(reservations.get(i+1)));
                }
                else if(reservations.get(i).equals("E")){
                    reservasExecutiva.add(Integer.valueOf(reservations.get(i+1)));
                }
            }
        }

        else {
            for (int i=2; i<reservations.size(); i+=2){
                if(reservations.get(i).equals("T")){
                    reservasTouristica.add(Integer.valueOf(reservations.get(i+1)));
                }
                else if(reservations.get(i).equals("E")){
                    System.out.printf("Não foi possivel obter lugares para a reserva: %s %d\n", "E", Integer.valueOf(reservations.get(i+1)));
                }
            }
        }

        informacao.put("T", reservasTouristica);
        informacao.put("E", reservasExecutiva);
        verificaPossibilidadeReserva(aviao, informacao, codigoVoo);
    }

    public static void verificaPossibilidadeReserva(Aviao aviao, HashMap<String, ArrayList<Integer>> informacao, Voo voo) {
        
        int[][] mapaExecutiva = aviao.getMapaExecutiva();
        int[][] mapaTouristica = aviao.getMapaTouristica();

        ArrayList<Reservas> reservas2 = new ArrayList<Reservas>();

        for (String classe: informacao.keySet()) {
            int numLugaresDispoExec = aviao.getLugaresExecutiva();
            int numLugaresDispoTour = aviao.getLugaresTuristica();
            
            if (classe.equals("E")) {
                for (int i = 0; i < informacao.get("E").size(); i++) {
                    
                    int numLugaresNecessarios = informacao.get("E").get(i);
                    int numLugaresOcupados = 0;
                    
                    if (numLugaresNecessarios > numLugaresDispoExec) {
                        System.out.printf("Não foi possivel obter lugares para a reserva: %s %d\n", "E", numLugaresNecessarios);
                        continue;
                    }

                    int j = 0;
                    int k = 0;

                    boolean allSeated = false;
                    do {
                        
                        if (mapaExecutiva[j][k] == 0) {
                            mapaExecutiva[j][k] = 1;
                            numLugaresOcupados++;
                        
                            if (numLugaresOcupados == numLugaresNecessarios) {
                                Reservas reserva = new Reservas(voo.getCodigo(), "E", numLugaresNecessarios);
                                mapaExecutiva[j][k] = reserva.getNumReserva();
                                reservas2.add(reserva);
                                reservas.put(voo, reservas2);
                                allSeated = true;
                                break;

                            } 

                            else {
                                if (k == aviao.getNumLugFilaExecutiva() - 1) {
                                    k = 0;
                                    j++;
                                } 
                                
                                else {
                                    k++;
                                }
                            }

                        } else {
                            if (k == aviao.getNumLugFilaExecutiva() - 1) {
                                k = 0;
                                j++;
                            } else {
                                k++;
                            }
                        
                            if (numLugaresNecessarios - numLugaresOcupados > aviao.getNumLugFilaExecutiva() * aviao.getNumFilasExecutiva() - (j * aviao.getNumLugFilaExecutiva() + k)) {
                                for (int a = 0; a < numLugaresOcupados; a++) {
                                    mapaExecutiva[j][k-a] = 0;
                                }
                                break;
                            }
                        }

                    } while (!allSeated);

                    if (!allSeated) {
                        System.out.printf("Não foi possivel obter lugares para a reserva: %s %d\n", "E", numLugaresNecessarios);
                    } 
                }
            }

            if (classe.equals("T")) {
                for (int i = 0; i < informacao.get("T").size(); i++) {
                    int numLugaresNecessarios = informacao.get("T").get(i);
                    int numLugaresOcupados = 0;
                    if (numLugaresNecessarios > numLugaresDispoTour) {
                        System.out.printf("Não foi possivel obter lugares para a reserva: %s %d\n", "T", numLugaresNecessarios);
                        continue;
                    }

                    int j = 0;
                    int k = 0;

                    boolean allSeated = false;
                    do {
                        
                        if (mapaTouristica[j][k] == 0) {
                            mapaTouristica[j][k] = 1;
                            numLugaresOcupados++;
                        
                            if (numLugaresOcupados == numLugaresNecessarios) {
                                Reservas reserva = new Reservas(voo.getCodigo(), "T", numLugaresNecessarios);
                                mapaTouristica[j][k] = reserva.getNumReserva();
                                reservas2.add(reserva);
                                reservas.put(voo, reservas2);
                                allSeated = true;
                                break;
                            } else {
                                if (k == aviao.getNumLugFilaTuristica() - 1) {
                                    k = 0;
                                    j++;
                                } else {
                                    k++;
                                }
                            }
                        } else {
                            if (k == aviao.getNumLugFilaTuristica() - 1) {
                                k = 0;
                                j++;
                            } else {
                                k++;
                            }
                        
                            if (numLugaresNecessarios - numLugaresOcupados > aviao.getNumLugFilaTuristica() * aviao.getNumFilasTuristica() - (j * aviao.getNumLugFilaTuristica() + k)) {
                                for (int a = 0; a < numLugaresOcupados; a++) {
                                    mapaTouristica[j][k-a] = 0;
                                }
                                break;
                            }
                        }

                    } while (!allSeated);

                    if (!allSeated) {
                        System.out.printf("Não foi possivel obter lugares para a reserva: %s %d\n", "T", numLugaresNecessarios);
                    } 
                }
            }
        }
    }


    public static void cancelarReserva(String codigoReserva){
        for(Voo v: reservas.keySet()) {
            ArrayList<Reservas> r1 = reservas.get(v);
            for (int i = 0; i < r1.size(); i++) {
                Reservas r = r1.get(i);
                if (r.getCodigo().equals(codigoReserva)) {
                    System.out.println(r + " Foi cancelada com sucesso...");
                    r1.remove(r);
                    break;
                }
            }
        }
    }
}
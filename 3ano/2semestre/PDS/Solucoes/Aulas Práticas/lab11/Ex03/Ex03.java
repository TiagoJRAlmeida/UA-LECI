package lab11.Ex03;

import java.util.ArrayList;
import java.util.Scanner;

public class Ex03 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Livro> list = new ArrayList<>();
        list.add(new Livro("Java Anti-Stress", 978085753, 2006, "Omodionah", new Inventario()));
        list.add(new Livro("A Guerra dos Padroes", 978142812, 2000, "Jorge Omel", new Inventario()));
        list.add(new Livro("A Procura da Luz", 978997198, -400, "Khumatkli", new Inventario()));

        System.out.println("*** Biblioteca ***");
        for (int i = 0; i < list.size(); i++)
            System.out.println(i + 1 + "\t" + list.get(i).toString());
        System.out.println("<livro>, <operação: (1)regista; (2)requisita; (3)devolve; (4)reserva; (5)cancela\n");

        while (sc.hasNextLine()) {
            String s = sc.nextLine();
            String[] idx = s.split(",");
            try {
                switch (Integer.parseInt(idx[1])) {
                    case 1:
                        list.get(Integer.parseInt(idx[0]) - 1).regista();
                        break;
                    case 2:
                        list.get(Integer.parseInt(idx[0]) - 1).requisita();
                        break;
                    case 3:
                        list.get(Integer.parseInt(idx[0]) - 1).devolve();
                        break;
                    case 4:
                        list.get(Integer.parseInt(idx[0]) - 1).reserva();
                        break;
                    case 5:
                        list.get(Integer.parseInt(idx[0]) - 1).cancelaReserva();
                        break;
                    default:
                        System.out.println("A operação não existe");
                }
            } catch (Exception e) {
                System.out.println("Comando inválido! <indice livro, operação>");
            }
            System.out.println("*** Biblioteca ***");
            for (int i = 0; i < list.size(); i++)
                System.out.println(i + 1 + "\t" + list.get(i).toString());
            System.out.println("<livro>, <operação: (1)regista; (2)requisita; (3)devolve; (4)reserva; (5)cancela\n");
        }
        ;
        sc.close();
    }
}

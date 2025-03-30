package lab11.Ex01;

import java.util.ArrayList;

public class Ex01 {
    public static void main(String[] args) {
        Telemovel t1 = new Telemovel("Samsung", " Exynos 990 da Samsung (7 nm)", 349.99, 128, 16);
        Telemovel t2 = new Telemovel("huawei", "Kirin 9000 da Huawei (5 nm)", 500.99, 256, 16);
        Telemovel t3 = new Telemovel("iphone", "Apple A14 Bionic (5 nm)", 899.99, 256, 24);
        Telemovel t4 = new Telemovel("Asus", "Qualcomm Snapdragon™ 680", 320.99, 256, 32);
        Telemovel t5 = new Telemovel("nokia", " Snapdragon 865 da Qualcomm (7 nm)", 150.79, 56, 8);
        Telemovel t6 = new Telemovel("huawei 2.0", "Snapdragon 888 da Qualcomm (5 nm)", 850.76, 128, 32);

        ArrayList<Telemovel> telemoveis1 = new ArrayList<>();
        telemoveis1.add(t1);
        telemoveis1.add(t2);
        telemoveis1.add(t3);
        ArrayList<Telemovel> telemoveis2 = new ArrayList<>();
        telemoveis2.add(t4);
        telemoveis2.add(t5);
        telemoveis2.add(t6);
        ArrayList<Telemovel> telemoveis3 = new ArrayList<>();
        telemoveis3.add(t2);
        telemoveis3.add(t4);
        telemoveis3.add(t6);


        Revista r1 = new Revista(new BubbleSort(), telemoveis1);
        Revista r2 = new Revista(new InsertionSort(), telemoveis2);
        Revista r3 = new Revista(new QuickSort(), telemoveis3);

        System.out.println("----------BubbleSort-----------------------------------------");
        System.out.println("\t Nome: ");
        r1.sort("nome");
        for (Telemovel tel : telemoveis1)
            System.out.println("\t\t\t" + tel);
        System.out.println("\t Preco: ");
        r1.sort("preco");
        for (Telemovel tel : telemoveis1)
            System.out.println("\t\t\t" + tel);
        System.out.println("\t Processador: ");
        r1.sort("processador");
        for (Telemovel tel : telemoveis1)
            System.out.println("\t\t\t" + tel);
        System.out.println("\t Memoria: ");
        r1.sort("memoria");
        for (Telemovel tel : telemoveis1)
            System.out.println("\t\t\t" + tel);
        System.out.println("----------------------------------------------------------");

        System.out.println("----------InsertionSort-----------------------------------------");
        System.out.println("\t Nome: ");
        r2.sort("nome");
        for (Telemovel tel : telemoveis2)
            System.out.println("\t\t\t" + tel);
        System.out.println("\t Preco: ");
        r2.sort("preco");
        for (Telemovel tel : telemoveis2)
            System.out.println("\t\t\t" + tel);
        System.out.println("\t Processador: ");
        r2.sort("processador");
        for (Telemovel tel : telemoveis2)
            System.out.println("\t\t\t" + tel);
        System.out.println("\t Memoria: ");
        r2.sort("memoria");
        for (Telemovel tel : telemoveis2)
            System.out.println("\t\t\t" + tel);
        System.out.println("----------------------------------------------------------");

        System.out.println("----------QuickSort-----------------------------------------");
        System.out.println("\t Nome: ");
        r3.sort("nome");
        System.out.println("\t\tsorting array using quick sort strategy");
        for (Telemovel tel : telemoveis3)
            System.out.println("\t\t\t" + tel);
        System.out.println("\t Preco: ");
        r3.sort("preco");
        System.out.println("\t\tsorting array using quick sort strategy");
        for (Telemovel tel : telemoveis3)
            System.out.println("\t\t\t" + tel);
        System.out.println("\t Processador: ");
        r3.sort("processador");
        System.out.println("\t\tsorting array using quick sort strategy");
        for (Telemovel tel : telemoveis3)
            System.out.println("\t\t\t" + tel);
        System.out.println("\t Memoria: ");
        r3.sort("memoria");
        System.out.println("\t\tsorting array using quick sort strategy");
        for (Telemovel tel : telemoveis3)
            System.out.println("\t\t\t" + tel);
        System.out.println("----------------------------------------------------------");
    }
}

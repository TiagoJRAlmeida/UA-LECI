package lab06.Ex01;

import java.util.List;

public class Ex01 {
    public static void main(String[] args) {
        System.out.println("\nAlinea 1");

        // Sweets
        System.out.println("\n-Sweets");

        Database baseDados = new Database();

        Employee employee1 = new Employee("André Oliveira", 196570, 8643);
        Employee employee2 = new Employee("Duarte Cruz", 231456, 9657);
        Employee employee3 = new Employee("Gonçalo Ferreira", 937586, 3425);
        Employee employee4 = new Employee("Tomás Rasinhas", 239756, 5276);

        baseDados.addEmployee(employee1);
        baseDados.addEmployee(employee2);
        baseDados.addEmployee(employee3);
        baseDados.addEmployee(employee4);

        Employee[] listaEmployees = baseDados.getAllEmployees();

        for (int i = 0; i < listaEmployees.length; i++) {
            System.out.println(listaEmployees[i]);
        }

        baseDados.deleteEmployee(239756);
        baseDados.deleteEmployee(196570);

        listaEmployees = baseDados.getAllEmployees();
        System.out.println("\nDepois da remoção de Employees\n");

        for (int i = 0; i < listaEmployees.length; i++) {
            System.out.println(listaEmployees[i]);
        }

        // Petiscos
        System.out.println("\n-Petiscos");

        Registos registo = new Registos();

        Empregado empregado1 = new Empregado("Tiago", "Silva", 1, 3467);
        Empregado empregado2 = new Empregado("António", "Antunes", 2, 2345);
        Empregado empregado3 = new Empregado("Mariana", "Maria", 3, 8765);
        Empregado empregado4 = new Empregado("Pedro", "João", 4, 9567);

        registo.insere(empregado1);
        registo.insere(empregado2);
        registo.insere(empregado3);
        registo.insere(empregado4);

        if (registo.isEmpregado(1)) {
            System.out.println("Empregado com codigo 1 pertence ao Registo");
        } else {
            System.out.println("Empregado com codigo 1 não pertence ao Registo");
        }

        registo.remove(1);

        if (registo.isEmpregado(1))
            System.out.println("Empregado com codigo 1 pertence ao Registo");
        else
            System.out.println("Empregado com codigo 1 não pertence ao Registo");

        List<Empregado> listaEmpregados = registo.listaDeEmpregados();

        for (int i = 0; i < listaEmpregados.size(); i++) {
            System.out.println(listaEmpregados.get(i));
        }


        System.out.println("\nalínea 2");

        Adapter baseDadosAdapter = new AdapterSweets(baseDados);
        Adapter registosAdapter = new AdapterPetiscos(registo);

        JuncaoDados joinBaseDados = new JuncaoDados(baseDadosAdapter, registosAdapter);

        System.out.println("\n-joinBaseDados");
        System.out.println("Dados da base de dados conjunta:\n");
        joinBaseDados.printAll();
        System.out.println();

        joinBaseDados.addEmpregado(new Empregado("João", "Domingues", 5, 94726));
        joinBaseDados.addEmpregado(new Empregado("Miguel", "Miranda", 6, 837457));
        joinBaseDados.addEmpregado(new Empregado("Sofia", "Cruz", 70, 9474673));
        joinBaseDados.addEmpregado(new Empregado("João", "António", 200, 748463));

        joinBaseDados.removeEmpregado(1);
        joinBaseDados.removeEmpregado(200);

        System.out.println();

        if (joinBaseDados.isEmpregado(200)) {
            System.out.println("O Empregado com código 200 pertence à joinBaseDados");
        } else {
            System.out.println("Oempregado com código 200 não pertence à joinBaseDados");
        }

        if (joinBaseDados.isEmpregado(5)) {
            System.out.println("O Empregado com código 5 pertence à joinBaseDados");
        } else {
            System.out.println("O Empregado com código 5 não pertence à joinBaseDados");
        }

        if (joinBaseDados.isEmpregado(70)) {
            System.out.println("O Empregado com código 70 pertence à joinBaseDados");
        } else {
            System.out.println("O Empregado com código 70 não pertence à joinBaseDados");
        }

        System.out.println();

        System.out.println("Dados da base de dados conjunta depois:\n");
        joinBaseDados.printAll();

        

    }
}

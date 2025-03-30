package lab06.Ex01;

import java.util.ArrayList;
import java.util.List;

public class Registos {
    // Data elements
    private ArrayList<Empregado> empregados; //Stores the employees

    public Registos() {
        empregados = new ArrayList<>();
    }

    public void insere(Empregado emp) {
        // Code to insert employee
        if (!isEmpregado(emp.codigo())) {
            empregados.add(emp);
        }
    }

    public void remove(int codigo) {
        // Code to remove employee
        for (int i=0; i<empregados.size(); i++) {
            if (empregados.get(i).codigo() == codigo) {
                empregados.remove(i);
            }
        }
    }

    public boolean isEmpregado(int codigo) {
        // Code to find employee
        for (int i=0; i<empregados.size(); i++) {
            if (empregados.get(i).codigo() == codigo) {
                return true;
            }
        }
        return false;
    }

    public List<Empregado> listaDeEmpregados() {
        // Code to retrieve collection
        return empregados;
    }

    @Override
    public String toString() {
        return "Registos " + empregados;
    }
}
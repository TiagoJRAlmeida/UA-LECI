package lab08.Ex02;

import java.util.ArrayList;

public class Insurance {
    private ArrayList<Employee> aderentes;

    public Insurance() {
        this.aderentes = new ArrayList<>();
    }

    public void regist(Employee employee) {
        this.aderentes.add(employee);
    }

    public ArrayList<Employee> getAderentes() {
        return this.aderentes;
    }
}

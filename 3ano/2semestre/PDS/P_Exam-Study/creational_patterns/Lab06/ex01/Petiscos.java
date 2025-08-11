import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

class Empregado { 
    private String nome; 
    private String apelido; 
    private int codigo; 
    private double salario; 
    
    public Empregado(String nome, String apelido, int codigo, double salario) { 
        this.nome = nome; 
        this.apelido = apelido; 
        this.codigo = codigo; 
        this.salario = salario; 
    } 
    public String apelido() { 
        return apelido; 
    } 
    public String nome() { 
        return nome; 
    } 
    public int codigo() { 
        return codigo; 
    } 
    public double salario() { 
        return salario; 
    } 

    public String toString(){
        return String.format("Empregado %s %s --> Numero: %d; Salario: %.2f", this.nome, this.apelido, this.codigo, this.salario);
    }
} 
    
class Registos { 
    // Data elements 
    private ArrayList<Empregado> empregados; // Stores the employees 
    
    public Registos() { 
        empregados = new ArrayList<>(); 
    } 
    
    public void insere(Empregado emp) { 
        // Code to insert employee 
        if (!empregados.contains(emp)){
            empregados.add(emp);
        }
    } 
    
    public void remove(int codigo) { 
        // Code to remove employee 
        Iterator<Empregado> it = empregados.iterator();
        while (it.hasNext()){
            if (it.next().codigo() == codigo){
                it.remove();
                break;
            }
        }
    } 
    
    public boolean isEmpregado(int codigo) { 
        // Code to find employee 
        for (Empregado emp : empregados){
            if (emp.codigo() == codigo){
                return true;
            }
        }
        return false;
    } 
    
    public List<Empregado> listaDeEmpregados() { 
        // Code to retrieve collection 
        return empregados;
    } 

}
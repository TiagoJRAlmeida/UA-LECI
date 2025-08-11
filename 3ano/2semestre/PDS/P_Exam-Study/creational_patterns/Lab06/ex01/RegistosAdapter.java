public class RegistosAdapter implements PstAdapter {
    private Registos registos;
    
    public RegistosAdapter(Registos reg){
        this.registos = reg;
    } 
    
    public void addEmployee(Object emp){
        if (emp instanceof Empregado){
            registos.insere((Empregado)emp);
        }
    }

    public void removeEmployee(long code){
        registos.remove((int) code);
    }

    public boolean isEmployee(long code){
        return registos.listaDeEmpregados().stream().anyMatch(emp -> (long)emp.codigo() == code);
    }

    public void showEmployees(){
        for (Empregado emp : registos.listaDeEmpregados()){
            System.out.println(emp);
        }
    }  
}

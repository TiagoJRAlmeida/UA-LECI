package ex01;

public class Employee implements Worker{
    private String name;
    
    public Employee(String name){
        this.name = name;
    }

    public String getName(){
        return this.name;
    }

    public void start(Date d){
        System.out.printf("Employee %s starts working at %s\n", this.name, d.toString());
    }

    public void terminate(Date d){
        System.out.printf("Employee %s stops working at %s\n", this.name, d.toString());
    }

    public void work(){
        System.out.printf("Employee %s works...\n", this.name);
    }
}

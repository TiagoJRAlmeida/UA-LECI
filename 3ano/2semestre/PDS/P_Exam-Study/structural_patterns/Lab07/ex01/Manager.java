package ex01;

public class Manager extends WorkerDecorator {
    private Worker worker;

    public Manager(Worker worker){
        super(worker);
    }

    @Override
    public void work(){
        super.work();
        manage();
    }

    public void manage(){
        System.out.printf("Manager %s manages...\n", this.getName());
    }
}

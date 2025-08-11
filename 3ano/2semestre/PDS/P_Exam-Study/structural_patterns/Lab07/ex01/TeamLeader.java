package ex01;

public class TeamLeader extends WorkerDecorator {
    private Worker worker;

    public TeamLeader(Worker worker){
        super(worker);
    }

    @Override
    public void work(){
        super.work();
        plan();
    }

    public void plan(){
        System.out.printf("TeamLeader %s plans...\n", this.getName());
    }
}

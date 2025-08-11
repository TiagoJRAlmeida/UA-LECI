package ex01;

public class TeamMember extends WorkerDecorator{
    private Worker worker;

    public TeamMember(Worker worker){
        super(worker);
    }

    @Override
    public void work(){
        super.work();
        colaborate();
    }

    public void colaborate(){
        System.out.printf("TeamMember %s colaborates...\n", this.getName());
    }
}

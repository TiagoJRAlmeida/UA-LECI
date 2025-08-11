package ex01;

public abstract class WorkerDecorator implements Worker {
    private Worker worker;

    public WorkerDecorator(Worker worker){
        this.worker = worker;
    }

    public String getName(){
        return worker.getName();
    }

    public void start(Date d){
        worker.start(d);
    }

    public void terminate(Date d){
        worker.terminate(d);
    }

    public void work(){
        worker.work();
    }
}

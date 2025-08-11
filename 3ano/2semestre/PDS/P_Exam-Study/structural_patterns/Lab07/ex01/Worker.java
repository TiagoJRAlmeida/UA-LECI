package ex01;

interface Worker{
    public String getName();
    public void start(Date d);
    public void terminate(Date d);
    public void work();
}
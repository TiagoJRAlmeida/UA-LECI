import java.util.ArrayList;
import java.util.List;

public class StudentAdm {
    private Student student;
    private List<Monitor> observers = new ArrayList<>();

    public StudentAdm(Student studnt) {
        this.student = studnt;
    }

    public void addScore(String className, double score) {
        student.addScore(className, (Double) score);
        notifyObservers(score, this.student);
    }

    public Student getStudent() {
        return student;
    }

    public void attach(Monitor monitor) {
        observers.add(monitor);
    }

    private void notifyObservers(double score, Student student) {
        for (Monitor obs : observers) {
            obs.update(score, student);
        }
    }
}









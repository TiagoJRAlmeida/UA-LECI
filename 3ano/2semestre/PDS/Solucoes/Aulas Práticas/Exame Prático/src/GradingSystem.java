import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

// GradingSystem class
public class GradingSystem implements Iterable<StudentAdm> {
    List<StudentAdm> studentsAdm = new ArrayList<>();
    List<Professor> professors = new ArrayList<>();
    List<Director> directors = new ArrayList<>();

    // Add a student to the system
    // The director of student's course is added as Monitor
    public StudentAdm addStudent(Student student) {
        StudentAdm studentAdm = new StudentAdm(student);
        studentsAdm.add(studentAdm);
        addDirector(student.getCourse());
        return studentAdm;
    }   

    // Add a director to the system
    // The director is added as monitor of the students in the same course
    public void addDirector(Course course) {
        for (StudentAdm studentAdm : studentsAdm) {
            if (studentAdm.getStudent().getCourse() == course) {
                for (Director director : directors) {
                    if (director.getStudentAdm() == studentAdm) {
                        return;
                    }
                }
                Director director = new Director(studentAdm, course);
                studentAdm.attach(director);
                directors.add(director);
            }
        }
    } 

    public void addProfessor(Professor professor) {
        for (StudentAdm studentAdm : studentsAdm) {
            studentAdm.attach(professor);
        }
        
        professors.add(professor);
    }


    public List<Director> getDirectors() {
        return directors;
    }

    public List<Professor> getProfessors() {
        return professors;
    }

    @Override
    public Iterator<StudentAdm> iterator() {
        return new GradingSystemIterator(this);
    }
}
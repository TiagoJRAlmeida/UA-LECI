public class Director extends Monitor {
    private Course degreeName;

    public Director (StudentAdm student, Course degree) {
        this.adm = student;
        this.degreeName = degree;
        if (this.degreeName == student.getStudent().getCourse()) {
            student.attach(this);
        } else {
            System.out.println("Error: Director's course must be the same as student's course");
            return;
        }
    }

    public Course getCourseName() {
        return degreeName;
    }

    public StudentAdm getStudentAdm() {
        return adm;
    }

    public double calcMedia() {
        return adm.getStudent().getOverallGrade();
    }

    @Override
    public void update(double score, Student student) {
        System.out.println(this.degreeName + " Director reports that student " + this.adm.getStudent() + " has changed the overall grade: " + this.calcMedia());
    }
}

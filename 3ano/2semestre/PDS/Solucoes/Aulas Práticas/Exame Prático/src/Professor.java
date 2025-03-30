public class Professor extends Monitor {
    private String className;
    private String name;

    public Professor(StudentAdm adm, String name, String className) {
        this.adm = adm;
        this.name = name;
        this.className = className;
        adm.attach(this);
    }

    public String getName() {
        return name;
    }

    public String getClassName() {
        return className;
    }

    @Override
    public void update(double score, Student student){
        System.out.println("Professor " + this.name + " of " + this.className + " class evaluated " + student + " with score: " + score);
    }

}

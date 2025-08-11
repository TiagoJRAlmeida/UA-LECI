package ex01;

public class Date {
    protected int day; 
    protected int month; 
    protected int year;

    public Date(int day, int month, int year){
        this.day = day;
        this.month = month;
        this.year = year;
    }

    public int getDay() {
        return day;
    }

    public int getMonth() {
        return month;
    }

    public int getYear() {
        return year;
    }

    public String toString(){
        return String.format("%d:%d:%d", this.day, this.month, this.year);
    }
}

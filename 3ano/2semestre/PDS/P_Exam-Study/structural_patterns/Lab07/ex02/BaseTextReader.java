package ex02;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class BaseTextReader implements TextReader {
    private File file;
    private Scanner fileScanner;

    public BaseTextReader(File file) {
        this.file = file;
        try {
            this.fileScanner = new Scanner(file);
        }
        catch(FileNotFoundException e){
            System.err.println("ERROR: " + e);
        }
    }

    public boolean hasNext(){
        return fileScanner.hasNextLine();
    }

    public String Next(){
        return fileScanner.nextLine();
    } 


}

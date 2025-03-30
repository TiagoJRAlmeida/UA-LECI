package lab06.Ex02;

import java.io.File;
import java.util.*;
import java.io.PrintWriter;
import java.io.IOException;

public class ContactsTxt extends ContactsImport {
    private File file;

    public ContactsTxt(File file) {
        super(file);
        this.file = file;
    }

    public List<Contact> loadContacts() {
        ArrayList<Contact> list = new ArrayList<>();
        try {
            Scanner sc = new Scanner(file);
            String line;
            while (sc.hasNextLine()) {
                line = sc.nextLine();
                if (line.matches("\\D+\t\\d+")) {
                    String[] data = line.split("\t");
                    list.add(new Contact(data[0], Integer.parseInt(data[1])));
                }
            }
            sc.close();
        } catch (IOException e) {
            e.printStackTrace();
        }

        return list;
    }

    public boolean saveContacts(List<Contact> list) {
        try {
            PrintWriter out = new PrintWriter(file);
            for (Contact c : list)
                out.println(c.toString());
            out.close();
        } catch (IOException e) {
            e.printStackTrace();
            return false;
        }

        return true;
    }
}

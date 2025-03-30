package lab06.Ex02;

import java.io.File;
import java.io.IOException;
import java.util.List;

public class ContactsImport implements ContactsStorageInterface {

    private File file;
    private String file_type;

    public ContactsImport(File file) {
        this.file = file;
        this.file_type = file.getName().substring(file.getName().lastIndexOf(".") + 1);
    }

    @Override
    public List<Contact> loadContacts() {
        ContactsStorageInterface store = null;

        try {
            switch (file_type) {
                case "txt":
                    store = new ContactsTxt(file);
                    break;
                case "bin":
                    store = new ContactsBin(file);
                    break;
                default:
                    throw new IOException("File type not supported");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        return store.loadContacts();
    }

    @Override
    public boolean saveContacts(List<Contact> list) {
        ContactsStorageInterface store = null;

        try {
            switch (file_type) {
                case "txt":
                    store = new ContactsTxt(file);
                    break;
                case "bin":
                    store = new ContactsBin(file);
                    break;
                default:
                    throw new IOException("File type not supported");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        return store.saveContacts(list);
    }
}

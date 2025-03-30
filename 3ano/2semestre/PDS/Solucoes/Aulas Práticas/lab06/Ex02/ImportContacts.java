package lab06.Ex02;

import java.io.File;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class ImportContacts implements ContactsInterface {
    private List<Contact> contacts;

    public ImportContacts() {
        this.contacts = new ArrayList<>();
    }

    @Override
    public void openAndLoad(ContactsStorageInterface store) {
        this.contacts.addAll(store.loadContacts());
    }

    @Override
    public void saveAndClose() {
        if (contacts.size() != 0) {
            Scanner sc = new Scanner(System.in);
            System.out.print("Save as: ");
            File file = new File("lab06/Ex02/" + sc.nextLine());
            sc.close();
            ContactsStorageInterface storage = new ContactsImport(file);
            storage.saveContacts(contacts);
        } else {
            System.out.println("Empty contacts");
        }
    }

    @Override
    public void saveAndClose(ContactsStorageInterface store) {
        if (contacts.size() != 0) {
            store.saveContacts(contacts);
        }
    }

    @Override
    public boolean exist(Contact contact) {
        return contacts.contains(contact);
    }

    @Override
    public Contact getByName(String name) {
        for (Contact c : contacts) {
            if (c.getName().equals(name)) {
                return c;
            }
        }
        return null;
    }

    @Override
    public boolean add(Contact contact) {
        if (!contacts.contains(contact)) {
            contacts.add(contact);
            return true;
        }
        return false;
    }

    @Override
    public boolean remove(Contact contact) {
        if (contacts.contains(contact)) {
            contacts.remove(contact);
            return true;
        }
        return false;
    }
}

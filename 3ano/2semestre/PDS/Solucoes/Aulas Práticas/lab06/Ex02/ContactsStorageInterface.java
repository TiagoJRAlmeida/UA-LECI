package lab06.Ex02;

import java.util.List;

public interface ContactsStorageInterface {
    public List<Contact> loadContacts();

    public boolean saveContacts(List<Contact> list);
}

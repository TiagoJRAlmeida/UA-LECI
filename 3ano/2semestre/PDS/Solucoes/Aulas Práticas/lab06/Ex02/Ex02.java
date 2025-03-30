package lab06.Ex02;

import java.io.File;

public class Ex02 {
    public static void main(String[] args) {

        ImportContacts contacts = new ImportContacts();

        File file1 = new File("lab06/Ex02/list1.txt");
        File file2 = new File("lab06/Ex02/list2.bin");

        ContactsImport storageImp2 = new ContactsImport(file2);
        contacts.saveAndClose(storageImp2);
        contacts.openAndLoad(storageImp2);

        ContactsImport storageImp1 = new ContactsImport(file1);
        contacts.openAndLoad(storageImp1);

        Contact c1 = new Contact("Andre Oliveira", 123455789);
        Contact c2 = new Contact("Rafael Botelho", 685856886);

        assert contacts.exist(c1) == true;
        assert contacts.exist(c2) == false;

        Contact c3 = contacts.getByName("Duarte Cruz");
        assert c3.equals(c1) == true;

        contacts.add(c2);
        assert contacts.exist(c2) == true;

        contacts.saveAndClose();

        contacts.remove(c2);
        assert contacts.exist(c2) == false;

    }
}

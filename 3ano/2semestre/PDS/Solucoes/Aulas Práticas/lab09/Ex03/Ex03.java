package lab09.Ex03;

import java.util.ArrayList;
import java.util.Collection;

public class Ex03 {
    public static void main(String[] args) {
        Collection<String> list = new ArrayList<>();
        CommandInvoker invoker = new CommandInvoker();

        Command add1 = new AddCommand<>(list, "Boas pessoal voces sabem que fala");
        Command add2 = new AddCommand<>(list, "mekie mekie mekie pa");
        invoker.setCommand(add1);
        invoker.executeCommand();
        invoker.setCommand(add2);
        invoker.executeCommand();
        printList(list);

        invoker.undoCommand();
        Command add3 = new AddCommand<>(list, "boas boas boas");
        invoker.setCommand(add3);
        invoker.executeCommand();
        printList(list);

        invoker.undoCommand();
        invoker.undoCommand();
        printList(list);

        Command add4 = new AddCommand<>(list, "Boas pessoal voces sabem que fala");
        Command add5 = new AddCommand<>(list, "mekie mekie mekie pa");
        Command add6 = new AddCommand<>(list, "boas boas boas");
        Command add7 = new AddCommand<>(list, "Entao pa ta tudo");
        invoker.setCommand(add4);
        invoker.executeCommand();
        invoker.setCommand(add5);
        invoker.executeCommand();
        invoker.setCommand(add6);
        invoker.executeCommand();
        invoker.setCommand(add7);
        invoker.executeCommand();
        printList(list);

        Command remove1 = new RemoveCommand<>(list, "mekie mekie mekie pa");
        Command remove2 = new RemoveCommand<>(list, "Boas pessoal voces sabem que fala");
        invoker.setCommand(remove1);
        invoker.executeCommand();
        invoker.setCommand(remove2);
        invoker.executeCommand();
        printList(list);

        invoker.undoCommand();
        printList(list);
    }

    private static void printList(Collection<String> list) {
        for (String s : list)
            System.out.println(s);
        System.out.println();
    }
}

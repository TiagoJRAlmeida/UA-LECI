package lab09.Ex03;

public class CommandInvoker {
    private Command command;
    private CommandHistory history = new CommandHistory();
    
    public void setCommand(Command command) {
        this.command = command;
    }
    
    public void executeCommand() {
        command.execute();
        history.push(command);
    }

    public void undoCommand() {
        if (history.isEmpty()) {
            return;
        } else {
            Command commandToUndo = history.pop();
            commandToUndo.undo();
        }
    }
}

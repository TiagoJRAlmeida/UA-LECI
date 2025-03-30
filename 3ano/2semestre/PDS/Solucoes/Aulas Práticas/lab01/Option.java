package lab01;

public class Option {
    public String opt;
    public String arg;

    /// Constructor
    public Option(String flag, String opt) {
        this.opt = flag;
        this.arg = opt;
    }

    /// Getters
    public String getOpt() {
        return opt;
    }

    public String getArg() {
        return arg;
    }
}
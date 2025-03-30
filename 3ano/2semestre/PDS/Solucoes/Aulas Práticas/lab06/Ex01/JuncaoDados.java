package lab06.Ex01;

public class JuncaoDados {
    //Dados
    private Adapter registos;
    private Adapter database;

    //Constructor
    public JuncaoDados(Adapter registos, Adapter database) {
        this.registos = registos;
        this.database = database;
    }

    //Adiciona um empregado
    public void addEmpregado(Empregado empregado) {
        // Verifica se o empregado já existe
        if (registos.isEmpregado(empregado.codigo()) || database.isEmpregado(empregado.codigo())) {
            System.out.println("codigo:" + empregado.codigo() + " já existe");
        } else {
            // Adiciona o empregado aleatoriamente ao registos ou à database
            if (Math.random() < 0.5) {
                registos.addEmpregado(empregado);
            } else {
                database.addEmpregado(empregado);
            }
        }
    }

    //Remove um empregado
    public void removeEmpregado(int codigo) {
        // Verifica se o empregado existe
        if (isEmpregado(codigo)) {
            // Verifica se o empregado está no registos ou na database
            if (registos.isEmpregado(codigo)) {
                registos.removeEmpregado(codigo);
            } else {
                database.removeEmpregado(codigo);
            }
        } else {
            System.out.println("codigo:" + codigo + " não existe");
        }
    }

    //Lista todos os empregados
    public void printAll() {
        registos.listaEmpregados();
        database.listaEmpregados();
    }

    //Verifica se existe um empregado com o código passado
    public boolean isEmpregado(int codigo) {
        return registos.isEmpregado(codigo) || database.isEmpregado(codigo);
    }
}

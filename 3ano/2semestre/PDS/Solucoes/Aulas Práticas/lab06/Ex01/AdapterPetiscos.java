package lab06.Ex01;

import java.util.List;

public class AdapterPetiscos implements Adapter {
    // Registos
    private Registos registos;

    // Constructor
    public AdapterPetiscos(Registos registos) {
        this.registos = registos;
    }

    @Override
    // Adiciona um empregado
    public void addEmpregado(Empregado empregado) {
        registos.insere(empregado);
    }

    @Override
    // Remove um empregado atrvés de um código
    public void removeEmpregado(int codigo) {
        registos.remove(codigo);
    }

    @Override
    // Verifica se existe um empregado com o código passado
    public boolean isEmpregado(int codigo) {
        return registos.isEmpregado(codigo);
    }

    @Override
    // Lista todos os empregados
    public void listaEmpregados() {
        // Cria uma lista de empregados
        List<Empregado> empregados = registos.listaDeEmpregados();

        // Percorre a lista e imprime cada empregado
        for (int i = 0; i < empregados.size(); i++) {
            System.out.println(empregados.get(i));
        }
    }
}

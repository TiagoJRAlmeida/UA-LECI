package lab06.Ex01;

public interface Adapter {
    public void addEmpregado (Empregado empregado);
    public void removeEmpregado(int codigo);
    public boolean isEmpregado (int codigo);
    public void listaEmpregados();
}

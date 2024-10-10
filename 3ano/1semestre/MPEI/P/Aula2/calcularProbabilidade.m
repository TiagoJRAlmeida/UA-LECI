function probSimulacao = calcularProbabilidade(n,m)

experiencias = randi(m, n, 1e6);
casosFavoraveis = 0;
for k=1:1e6
    if length(unique(experiencias(:,k))) < n
        casosFavoraveis = casosFavoraveis + 1;
    end
end

probSimulacao = casosFavoraveis/1e6;

end
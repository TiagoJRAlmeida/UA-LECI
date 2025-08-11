function incidence_matrix = create_incidence_matrix(dataset)
    articles_text = dataset(1:end, 2);
    words_vector = strjoin(articles_text);
    unique_words = unique(split(words_vector));
    
    num_articles = length(articles_text);
    num_unique_words = length(unique_words);
    incidence_matrix = zeros(num_articles, num_unique_words);
    
    for i = 1:num_articles
        % Palavras do artigo atual
        article_words = split(articles_text(i));
        for j = 1:num_unique_words
            if any(strcmp(article_words, unique_words{j}))
                % Palavra presente no artigo
                incidence_matrix(i, j) = 1;
            end
        end
    end
end
function category = get_category(article, category_probabilities, unique_words, categories_list, word_category_probabilities)
    log_category_probabilities = log(category_probabilities);

    article_words = split(lower(article)); 
    words_in_article = intersect(article_words, unique_words);

    log_probabilities = zeros(5, 1);

    for c = 1:5
        log_probabilities(c) = log_category_probabilities(c);

        [is_in_vocab, word_indices] = ismember(words_in_article, unique_words);
        word_indices = word_indices(is_in_vocab);
        if ~isempty(word_indices)
            word_probs = word_category_probabilities(word_indices, c);
            word_probs(word_probs == 0) = 1e-10; 
            log_probabilities(c) = log_probabilities(c) + sum(log(word_probs));
        end
    end

    [~, max_index] = max(log_probabilities);
    category = categories_list{max_index};
end
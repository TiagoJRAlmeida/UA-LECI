function [category_probabilities, unique_words, categories_list, word_category_probabilities] = train_naive_bayes(training_dataset)
    articles_text = training_dataset(2:end, 2);
    words_vector = strjoin(articles_text);

    unique_words = unique(split(words_vector));
    information_matrix = zeros(size(articles_text,1),size(unique_words,1));

    for i = 1:size(articles_text,1)
        for j = 1:size(unique_words,1)
            information_matrix(i,j) = count(articles_text{i},unique_words(j));
        end
    end

    category_information = categorical(training_dataset(2:end, 3));
    categories_list = categories(category_information);
    category_counts = countcats(category_information);

    total_articles = sum(category_counts);
    category_probabilities = category_counts / total_articles;

    num_words = numel(unique_words);
    num_categories = numel(categories_list);
    word_category_probabilities = zeros(num_words, num_categories);

    for c = 1:num_categories
        articles_of_category = category_information == categories_list{c};
        category_word_counts = sum(information_matrix(articles_of_category, :), 1);
        total_words_in_category = sum(category_word_counts);
        word_category_probabilities(:, c) = category_word_counts / total_words_in_category;
    end
end

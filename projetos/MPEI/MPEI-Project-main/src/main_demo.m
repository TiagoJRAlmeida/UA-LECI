%% MAIN File - Logic for the final APP

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Pre-application setup
clc;
% Read the articles file
dataset = readcell('../dataset/BBC_News_Test.csv');
dataset = dataset(1:200, :);
article_count = size(dataset, 1) - 1;

% Train the naive Bayes
training_dataset = readcell('../dataset/BBC_News_Train.csv');
training_dataset = training_dataset(1:200, :);
[category_probabilities, unique_words, categories_list, word_category_probabilities] = train_naive_bayes(training_dataset);
fprintf("Training complete\n")

% Initialize cell arrays for each category
sport_articles = {};
tech_articles = {};
business_articles = {};
entertainment_articles = {};
politics_articles = {};

% Loop through the articles and classify them
for i = 2:article_count + 1
    category = get_category(dataset{i, 2}, category_probabilities, unique_words, categories_list, word_category_probabilities);
    if strcmp(category, 'sport')
        sport_articles = [sport_articles; dataset(i, :)];
    elseif strcmp(category, 'tech')
        tech_articles = [tech_articles; dataset(i, :)];
    elseif strcmp(category, 'business')
        business_articles = [business_articles; dataset(i, :)];
    elseif strcmp(category, 'entertainment')
        entertainment_articles = [entertainment_articles; dataset(i, :)];
    elseif strcmp(category, 'politics')
        politics_articles = [politics_articles; dataset(i, :)];
    end
end
fprintf("Category attribution complete\n")

% Create incidence matrix for each category
sport_articles_incidence_matrix = create_incidence_matrix(sport_articles);
tech_articles_incidence_matrix = create_incidence_matrix(tech_articles);
business_articles_incidence_matrix = create_incidence_matrix(business_articles);
entertainment_articles_incidence_matrix = create_incidence_matrix(entertainment_articles);
politics_articles_incidence_matrix = create_incidence_matrix(politics_articles);

% Initialize cell arrays for each category
sport_articles_signatures = {};
tech_articles_signatures = {};
business_articles_signatures = {};
entertainment_articles_signatures = {};
politics_articles_signatures = {};

for i = 1:length(sport_articles_incidence_matrix(:, 1))
    sport_articles_signatures{i} = generate_signature(sport_articles_incidence_matrix(i, :));
end

for i = 1:length(tech_articles_incidence_matrix(:, 1))
    tech_articles_signatures{i} = generate_signature(tech_articles_incidence_matrix(i, :));
end

for i = 1:length(business_articles_incidence_matrix(:, 1))
    business_articles_signatures{i} = generate_signature(business_articles_incidence_matrix(i, :));
end

for i = 1:length(entertainment_articles_incidence_matrix(:, 1))
    entertainment_articles_signatures{i} = generate_signature(entertainment_articles_incidence_matrix(i, :));
end

for i = 1:length(politics_articles_incidence_matrix(:, 1))
    politics_articles_signatures{i} = generate_signature(politics_articles_incidence_matrix(i, :));
end
fprintf("Signatures creation complete\n")

% Bloom filter parameters
p = 0.01; % Desired false positive rate
m = article_count; % Number of objects to insert into the bitmap
n = round(-((m * log(p)) / (log(2)^2))); % Optimal bitmap size
k = round((n / m) * log(2)); % Optimal number of hash functions

% Initialize Bloom filters
articles_ids = dataset(2:end, 1);
articles_bitmap = bloom_filter(articles_ids, n, k);
read_articles_bitmap = zeros(1, n);

fprintf("Setup Complete")
input("\n\nPrecione enter para continuar.\n") 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Main menu loop
while true
    clc;
    fprintf("======== Menu de operações ========\n\n" + ...
        "  1- Mostrar artigos aleatórios\n" + ...
        "  2- Pesquisar por categoria\n" + ...
        "  3- Mostrar artigos lidos\n" + ...
        "  4- Sair\n" + ...
        "\n===================================\n");

    escolha = input("Escolha uma operação: ");

    switch escolha
        case 1
            read_articles_bitmap = mostrar_artigos_recomendados(dataset, articles_bitmap, read_articles_bitmap, n, k, category_probabilities, unique_words, categories_list, word_category_probabilities);
        case 2
            read_articles_bitmap = pesquisar_por_categoria(dataset, articles_bitmap, read_articles_bitmap, n, k, sport_articles, tech_articles, business_articles, entertainment_articles, politics_articles, ...
                        sport_articles_signatures, tech_articles_signatures, business_articles_signatures, entertainment_articles_signatures, politics_articles_signatures, ...
                        category_probabilities, unique_words, categories_list, word_category_probabilities);
        case 3
            read_articles_bitmap = mostrar_artigos_lidos(dataset, articles_bitmap, read_articles_bitmap, n, k, category_probabilities, unique_words, categories_list, word_category_probabilities);
        case 4
            fprintf("Saindo da aplicação.\n");
            break;
        otherwise
            fprintf("Opção inválida. Tente novamente.\n");
    end
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Functions

function new_bitmap = mostrar_artigos_recomendados(dataset, articles_bitmap, read_articles_bitmap, n, k, category_probabilities, unique_words, categories_list, word_category_probabilities)
    clc;
    fprintf("===================================\n\n");
    random_indexes = randperm(size(dataset, 1) - 1, 10); 
    for i = 1:10
        artigo_id = dataset{random_indexes(i) + 1, 1};
        artigo_texto = dataset{random_indexes(i) + 1, 2};
        palavras = strsplit(artigo_texto);
        primeiras_20_palavras = palavras(1:min(20, numel(palavras)));
        texto_final = strjoin(primeiras_20_palavras, ' ');
        article_categoty = get_category(artigo_texto, category_probabilities, unique_words, categories_list, word_category_probabilities);
        fprintf('ArticleID: %d | Category: %s\nText: %s\n\n', artigo_id, article_categoty, texto_final);
    end
    fprintf("===================================\n");
    new_bitmap = submenu_ler_artigo(dataset, articles_bitmap, read_articles_bitmap, n, k, category_probabilities, unique_words, categories_list, word_category_probabilities);
end

function new_bitmap = submenu_ler_artigo(dataset, articles_bitmap, read_articles_bitmap, n, k, category_probabilities, unique_words, categories_list, word_category_probabilities)
    fprintf("======== Menu de operações ========\n\n" + ...
        "   1- Ler um artigo   \n" + ...
        "   2- Voltar ao menu inicial  \n" + ...
        "\n===================================\n");

    escolha = input("Escolha uma operação: ");

    if escolha == 1
        new_bitmap = ler_artigo(dataset, articles_bitmap, read_articles_bitmap, n, k, category_probabilities, unique_words, categories_list, word_category_probabilities);
    else
        new_bitmap = read_articles_bitmap;
    end
end

function new_bitmap = ler_artigo(dataset, articles_bitmap, read_articles_bitmap, n, k, category_probabilities, unique_words, categories_list, word_category_probabilities)
    ler_artigo_id = input("Indique o ID do artigo: ");
    if in_bloom_filter(ler_artigo_id, articles_bitmap, n, k)
        for i = 2:size(dataset, 1)
            if dataset{i, 1} == ler_artigo_id
                clc;
                new_bitmap = add_to_bitmap(ler_artigo_id, read_articles_bitmap, n, k);
                article_categoty = get_category(dataset{i, 2}, category_probabilities, unique_words, categories_list, word_category_probabilities);
                fprintf('ArticleID: %d | Category: %s\nText: %s\n\n', ler_artigo_id, article_categoty, dataset{i, 2});
                input("\nPrecione enter para voltar.\n") 
                return;
            end
        end
    end
    new_bitmap = read_articles_bitmap;
    input("\nPrecione enter para voltar.\n") 
    fprintf("ID do artigo não existe.\n");
end

function new_bitmap = mostrar_artigos_lidos(dataset, articles_bitmap, read_articles_bitmap, n, k, category_probabilities, unique_words, categories_list, word_category_probabilities)
    clc;
    read_articles = 0;
    for i = 2:size(dataset, 1)
        if in_bloom_filter(dataset{i, 1}, read_articles_bitmap, n, k)
            read_articles = read_articles + 1;
            artigo_id = dataset{i, 1};
            artigo_texto = dataset{i, 2};
            palavras = strsplit(artigo_texto);
            primeiras_20_palavras = palavras(1:min(20, numel(palavras)));
            texto_final = strjoin(primeiras_20_palavras, ' ');
            article_categoty = get_category(artigo_texto, category_probabilities, unique_words, categories_list, word_category_probabilities);
            fprintf('ArticleID: %d | Category: %s\nText: %s\n\n', artigo_id, article_categoty, texto_final);
        end
    end
    if read_articles == 0
        fprintf("Nenhum artigo foi lido ainda.\n");
        new_bitmap = read_articles_bitmap;
        input("\nPrecione enter para voltar.\n")
    else
        new_bitmap = submenu_ler_artigo(dataset, articles_bitmap, read_articles_bitmap, n, k);
    end
end

function new_bitmap = pesquisar_por_categoria(dataset, articles_bitmap, read_articles_bitmap, n, k, sport_articles, tech_articles, business_articles, entertainment_articles, politics_articles, ...
                                 sport_articles_signatures, tech_articles_signatures, business_articles_signatures, entertainment_articles_signatures, politics_articles_signatures, ...
                                 category_probabilities, unique_words, categories_list, word_category_probabilities)

    clc;
    fprintf("======= Pesquisa por Categoria =======\n\n");
    chosen_category = input("Digite a categoria para pesquisar (sport, tech, business, entertainment, politics): ", 's');

    % Select articles and signatures for the chosen category
    switch chosen_category
        case 'sport'
            category_articles = sport_articles;
            category_signatures = sport_articles_signatures;
        case 'tech'
            category_articles = tech_articles;
            category_signatures = tech_articles_signatures;
        case 'business'
            category_articles = business_articles;
            category_signatures = business_articles_signatures;
        case 'entertainment'
            category_articles = entertainment_articles;
            category_signatures = entertainment_articles_signatures;
        case 'politics'
            category_articles = politics_articles;
            category_signatures = politics_articles_signatures;
        otherwise
            fprintf("Categoria inválida. Tente novamente.\n");
            input("\nPressione Enter para voltar ao menu inicial.\n");
            new_bitmap = read_articles_bitmap;
            return;
    end

    % Separate read and unread articles
    unread_articles = {};
    unread_signatures = {};
    read_signatures = {};
    for i = 1:size(category_articles, 1)
        article_id = category_articles{i, 1};
        if ~in_bloom_filter(article_id, read_articles_bitmap, n, k)
            unread_articles = [unread_articles; category_articles(i, :)];
            unread_signatures = [unread_signatures; category_signatures{i}];
        else
            read_signatures = [read_signatures; category_signatures{i}];
        end
    end

    if isempty(unread_articles)
        fprintf("Nenhum artigo não lido encontrado na categoria '%s'.\n", chosen_category);
        input("\nPressione Enter para voltar ao menu inicial.\n");
        new_bitmap = read_articles_bitmap;
        return;
    end

    % Compute Jaccard distances between unread and read articles using signatures
    similarity_scores = zeros(size(unread_signatures, 1), 1);
    for i = 1:size(unread_signatures, 1)
        min_distance = inf;
        for j = 1:size(read_signatures, 1)
            distance = Jdistance(unread_signatures{i}, read_signatures{j});
            if distance < min_distance
                min_distance = distance;
            end
        end
        similarity_scores(i) = min_distance;
    end

    % Sort unread articles by similarity
    [~, sorted_indexes] = sort(similarity_scores);
    sorted_articles = unread_articles(sorted_indexes, :);

    % Display top 10 most similar articles
    num_articles = min(10, size(sorted_articles, 1));
    fprintf("\nArtigos mais similares na categoria '%s':\n\n", chosen_category);
    for i = 1:num_articles
        article_id = sorted_articles{i, 1};
        article_text = sorted_articles{i, 2};
        palavras = strsplit(article_text);
        primeiras_20_palavras = palavras(1:min(20, numel(palavras)));
        texto_final = strjoin(primeiras_20_palavras, ' ');
        fprintf('ArticleID: %d \nText: %s\n\n', article_id, texto_final);
    end

    % Submenu to read an article or return
    while true
        fprintf("======== Menu de operações ========\n\n" + ...
                "   1- Ler um artigo   \n" + ...
                "   2- Voltar ao menu inicial  \n" + ...
                "\n===================================\n");

        escolha = input("Escolha uma operação: ");

        if escolha == 1
            new_bitmap = ler_artigo(dataset, articles_bitmap, read_articles_bitmap, n, k, category_probabilities, unique_words, categories_list, word_category_probabilities);
            break;
        elseif escolha == 2
            new_bitmap = read_articles_bitmap;
            break;
        else
            fprintf("Opção inválida. Tente novamente.\n");
        end
    end
end



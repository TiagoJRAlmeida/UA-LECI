function signature = generate_signature(incidence_vector)

    num_words = length(incidence_vector);

    hash_codes = zeros(100, num_words);
    for j = 1:num_words
        if incidence_vector(j) > 0
            word_hashes = multiple_hash(num2str(j), 100);
            hash_codes(:, j) = word_hashes(:);
        else
            hash_codes(:, j) = inf;
        end
    end
    signature = min(hash_codes, [], 2)';
end
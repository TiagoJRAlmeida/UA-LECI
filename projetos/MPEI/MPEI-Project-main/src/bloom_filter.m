function bloom_filter_table = bloom_filter(conjunto, n, k)
    bloom_filter_table = zeros(1, n);
    for i = 1:size(conjunto, 1)
        elem_hashes = multiple_hash(conjunto{i}, k);
        for z = 1:k
            idx = mod(elem_hashes(z), n) + 1;
            bloom_filter_table(idx) = 1;
        end
    end
end
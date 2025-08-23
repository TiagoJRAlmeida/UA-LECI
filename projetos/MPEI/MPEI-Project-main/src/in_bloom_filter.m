function output = in_bloom_filter(element, bloom_filter_table, n, k)
    elem_hashes = multiple_hash(element, k);
    probably_yes = 0;
    for i = 1:k
        idx = mod(elem_hashes(i), n) + 1;
        if bloom_filter_table(idx) == 1
            probably_yes = probably_yes + 1;
        end
    end
    if probably_yes == k
        output = 1;
    else
        output = 0;
    end
end
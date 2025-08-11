function new_bitmap = add_to_bitmap(elem, bitmap, n, k)
    elem_hashes = multiple_hash(elem, k);
    for z = 1:k
        idx = mod(elem_hashes(z), n) + 1;
        bitmap(idx) = 1;
    end
    new_bitmap = bitmap;
end
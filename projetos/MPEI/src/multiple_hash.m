function hash = multiple_hash(str,k)
    if(nargin<2), k=1; end
    hash = zeros(1, k);
    hash(1) = string2hash(str,'sdbm');
    if k > 1
        for i = 2:k
            hash(i) = string2hash(num2str(hash(i - 1)),'sdbm');
        end
    end
end
function distance = Jdistance(C1, C2)
    distance = 1 - length(intersect(C1,C2))/ length(union(C1,C2));
end
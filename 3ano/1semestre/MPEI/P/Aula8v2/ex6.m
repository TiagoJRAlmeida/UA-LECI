%% a

T = [
        0.8     0       0       0.3     0;
        0.2     0.6     0       0.2     0;
        0       0.3     1       0       0;
        0       0.1     0       0.4     0;
        0       0       0       0.1     1;
    ];
 
%% b

x0 = [1;0;0;0;0];
res = zeros(5, 100);
for i = 1 : 100
    res(:,i) = T^i * x0;
end

plot(1:100,res(2, :))

%% c

T = [
        0.8     0       0       0.3     0;
        0.2     0.6     0       0.2     0;
        0       0.3     1       0       0;
        0       0.1     0       0.4     0;
        0       0       0       0.1     1;
    ];

n = 1:100;
x0 = [1;0;0;0;0];

for i = 1 : 100
    res(:,i) = T^i * x0;
end

plot(1:100,res(3, :))
hold
plot(1:100,res(5, :))


%% d

    % 1 2 4 3 5
T = [
        0.8     0       0.3     0     0;
        0.2     0.6     0.2     0     0;
        0       0.1     0.4     0     0;
        0       0.3     0       1     0;
        0       0       0.1     0     1;
    ];
Q = [
        0.8     0       0.3;
        0.2     0.6     0.2;
        0       0.1     0.4;
    ];  

%% e

Q = [
        0.8     0       0.3;
        0.2     0.6     0.2;
        0       0.1     0.4;
    ];  

F = inv(eye(size(Q)) - Q)

% f

t = sum(F)

%% g
Q = [
        0.8     0       0.3;
        0.2     0.6     0.2;
        0       0.1     0.4;
    ];  
R = [
        0   0.3     0;
        0   0       0.1;
    ];

F = inv(eye(size(Q)) - Q);

B = R * F

fprintf("Probabilidade de obsorcao do Estado 3 %f\n", B(1, 1));
fprintf("Probabilidade de obsorcao do Estado 5 %f\n", B(2, 1));
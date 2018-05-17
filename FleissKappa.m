%Search project, Fleiss' kappa statistic
%% A) Calculate Fleiss' kappa statistic to measure group agreement on the relevance of chatbot answers
N = 20;
n = 4;
k = 3;

Answers = [2 2 2 0 1 1 2 2 2 2 0 0 0 0 1 2 0 0 1 1;
    1 2 2 0 2 2 2 2 2 2 0 0 0 0 1 2 0 0 1 1;
    1 2 1 0 2 1 2 2 2 2 1 0 0 0 0 1 0 0 1 0;
    2 2 2 0 2 2 2 2 2 2 0 0 0 0 0 1 0 0 1 0];

P = [];

for i=1:N
    p_0 = 0;
    p_1 = 0;
    p_2 = 0;
    for j=1:n
        if Answers(j,i)==0
            p_0 = p_0+1;
        elseif Answers(j,i)==1
            p_1 = p_1+1;
        else
            p_2 = p_2+1;
        end
    end
    p_0 = p_0/(N*n);
    p_1 = p_1/(N*n);
    p_2 = p_2/(N*n);
    P(1,i) = p_0;
    P(2,i) = p_1;
    P(3,i) = p_2;
end
p0 = sum(P(1,:));
p1 = sum(P(2,:));
p2 = sum(P(3,:));

P = [];
for i=1:N
    ni0 = 0;
    ni1 = 0;
    ni2 = 0;
    for j=1:n
        if Answers(j,i)==0
            ni0 = ni0+1;
        elseif Answers(j,i)==1
            ni1 = ni1+1;
        else
            ni2 = ni2+1;
        end
    end
    nij_square_sum = (ni0^2)+(ni1^2)+(ni2^2);
    num = nij_square_sum - n;
    denom = n*(n-1);
    P(i) = num/denom;
end
Pbar = sum(P)/N;
Pbar_e = (p0^2)+(p1^2)+(p2^2);
kappa = (Pbar-Pbar_e)/(1-Pbar_e)
%% B) Precision calculation by averaging the individual precisions of the four group members
Precision1 = 0;
for i=1:length(Answers)
    if Answers(1,i)>0
        Precision1 = Precision1 +1;
    end
end
Precision1 = Precision1/N;

Precision2 = 0;
for i=1:length(Answers)
    if Answers(2,i)>0
        Precision2 = Precision2 +1;
    end
end
Precision2 = Precision2/N;

Precision3 = 0;
for i=1:length(Answers)
    if Answers(3,i)>0
        Precision3 = Precision3 +1;
    end
end
Precision3 = Precision3/N;

Precision4 = 0;
for i=1:length(Answers)
    if Answers(4,i)>0
        Precision4 = Precision4 +1;
    end
end
Precision4 = Precision4/N;

Precision = (Precision1 + Precision2 + Precision3 + Precision4)/4;
Precision
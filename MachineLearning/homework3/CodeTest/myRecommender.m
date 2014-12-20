function [ U, V ] = myRecommender( rateMatrix, lowRank )
    % Please type your name here:
    name = 'bhatia, parminder';
    disp(name); % Do not delete this line.

    % Parameters
    maxIter = 450; % Choose your own.
    learningRate = 0.00025; % Choose your own.
    regularizer = 0.03; % Choose your own.
    
    % Random initialization:
    [n1, n2] = size(rateMatrix);
    U = rand(n1, lowRank) / lowRank;
    V = rand(n2, lowRank) / lowRank;

    % Gradient Descent:
    
%    derivativesU = zeros(n1, lowRank);
%    derivativesV = zeros(n2, lowRank);
    
    % IMPLEMENT YOUR CODE HERE.
    
    limit = 10e-3;    
    F = 10;
    iterations = 1;    
    
    while (F > limit && iterations <= maxIter)
    %for iterations=1:maxIter
        
        %hypo = U*V';    
        %dU
        derivativesU = (1-2*learningRate*regularizer)*U + 2*learningRate*((rateMatrix - U*V').*(rateMatrix > 0))*V;
        derivativesV = (1-2*learningRate*regularizer)*V + 2*learningRate*(((rateMatrix - U*V').*(rateMatrix > 0))')*U;
        learningRate = learningRate -  0.0000002;
        if (iterations/100)*100 ==iterations
            regularizer = regularizer + .002;
        end
   
         
        
      
        U = derivativesU;
        V = derivativesV;
        F= sum(sum(((U*V' - rateMatrix).*(rateMatrix > 0)).^2)); 
       
        iterations = iterations + 1;
        
    end     
end
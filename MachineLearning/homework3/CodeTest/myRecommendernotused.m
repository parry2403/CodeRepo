function [ U, V ] = myRecommendernotused( rateMatrix, lowRank )
    % Please type your name here:
    name = 'Bhatia, Parminder';
    disp(name); % Do not delete this line.

    % Parameters
    maxIter = 600; % Choose your own.
    learningRate = 0.000003; % Choose your own.
    regularizer = 3; % Choose your own.
    
    % Random initialization:
    [n1, n2] = size(rateMatrix);
    U = rand(n1, lowRank) / lowRank;
    V = rand(n2, lowRank) / lowRank;
    r =1.2;
    % Gradient Descent:
    
    %derivativesU = zeros(n1, lowRank);
    %derivativesV = zeros(n2, lowRank);
    
    % IMPLEMENT YOUR CODE HERE.
    
    limit = 10e-3;    
    F = limit + 10;
    iterations = 1;    
    
    while (F > limit && iterations <= maxIter)
    %for iterations=1:maxIter
      
        derivativesU = (1-2*learningRate*regularizer)*U + 2*learningRate*((rateMatrix - U*V').*(rateMatrix > 0))*V;
        derivativesV = (1-2*learningRate*regularizer)*V + 2*learningRate*(((rateMatrix - U*V').*(rateMatrix > 0))')*U;
      
        
       
        
        F1 = sum(sum(((U*V' - rateMatrix).*(rateMatrix > 0)).^2)); 
        if (F1 <= F)
            U = derivativesU;
            V = derivativesV;
            learningRate = r * learningRate;
        else
            learningRate =.5*learningRate;
          %  r = r - .01
        end
                    
        iterations = iterations + 1;
        F = F1;
        
    end     
end
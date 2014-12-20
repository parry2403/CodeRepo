function [ class, centroid ] = mykmeans( pixels, K )
%
% Your goal of this assignment is implementing your own K-means.
%
% Input:
%     pixels: data set. Each row contains one data point. For image
%     dataset, it contains 3 columns, each column corresponding to Red,
%     Green, and Blue component.
%
%     K: the number of desired clusters. Too high value of K may result in
%     empty cluster error. Then, you need to reduce it.
%
% Output:
%     class: the class assignment of each data point in pixels. The
%     assignment should be 1, 2, 3, etc. For K = 5, for example, each cell
%     of class should be either 1, 2, 3, 4, or 5. The output should be a
%     column vector with size(pixels, 1) elements.
%
%     centroid: the location of K centroids in your result. With images,
%     each centroid corresponds to the representative color of each
%     cluster. The output should be a matrix with size(pixels, 1) rows and
%     3 columns. The range of values should be [0, 255].
%     
%
% You may run the following line, then you can see what should be done.
% For submission, you need to code your own implementation without using
% the kmeans matlab function directly. That is, you need to comment it out.
    m = 100; % number of data points; 
    % fix the seed of the random number generator, so each time generate
    % the same random points; 
    randn('seed', 1);     
    x = pixels';
    
    % number of clusters; 
    cno = K;   
%	[class, centroid] = kmeans(pixels, K);

m = size(x, 2);
dim = size(pixels,2);
%%
% randomly initialize the cluster center; since the seed for function rand
% is not fixed, every time it is a different matrix; 

ind = randi(m, 1, cno);
rand('seed', sum(clock));
c = x(:,ind); 
c_old = c + 10; 
iteration = 15;
i = 1; 
% check whether the cluster centers still change; 
tic
myassignments = zeros(m,1);
%while ( norm(c - c_old, 'fro') > 1e-4)
for l = 1:iteration
    % record previous c;
     if norm(c - c_old, 'fro') < 1e-5
        break
     end
     
    c_old = c; 
    
    % assign data points to current cluster; 
    for j = 1:m % loop through data points; 
        tmp_distance = zeros(1, cno); 
        for k = 1:cno % through centers; 
            tmp_distance(k) = sum(abs((x(:,j) - c(:,k)))); % norm(x(:,j) - c(:,k)); 
        end
        [~,k_star] = min(tmp_distance); % ~ ignores the first argument; 
        P(j, :) = zeros(1, cno); 
        P(j, k_star) = 1; 
    end
        
    % adjust the cluster centers according to current assignment;     
    cstr = {'r.', 'b.', 'g.', 'r+', 'b+', 'g+'};
    obj = 0; 
    for k = 1:cno
        idx = find(P(:,k)>0); 
        nopoints = length(idx);  
        if (nopoints == 0) 
            % a cener has never been assigned a data point; 
            % re-initialize the center; 
             c(:,k) = x(:,randi(m));  
        else
            cen = x * P(:,k) ./ nopoints;   
            mini = Inf ;
            for j=1:nopoints
                %idx(j)
                if mini > sum(sum(abs(x(:,idx(j)) - cen)))
                    mini = sum(sum(abs(x(:,idx(j)) - cen)));
                    c(:,k) = x (:,idx(j));
                end
            end
            % equivalent to sum(x(:,idx), 2) ./ nopoints;            
         %   c(:,k) = x * P(:,k) ./ nopoints;         
         
     %     obj = obj + sum(sum(abs(x(:,idx) - repmat(c(:,k), 1, nopoints)))); 
    end
       
end   
i = i + 1;   
end
for i =1:m
 myassignments(i) = find(P(i,:)>0); 
end
centroid = c';
class = myassignments;
%[c,c']




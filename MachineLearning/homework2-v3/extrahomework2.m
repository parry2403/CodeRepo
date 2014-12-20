function [] = extrahomework2( )
% This is a simple example to help you evaluate your clustering algo implementation. You should run your code several time and report the best
% result. The data contains a 400*101 matrix call X, in which the last
% column is the true label of the assignment, but you are not allowed to
% use this label in your implementation, the label is provided to help you
% evaluate your algorithm. 
%
%
% Please implement your clustering algorithm in the other file, mycluster.m. Have fun coding!

data = load('nips.mat');


%IDX = topicmycluster(T,4);
IDX = topicmycluster(data.raw_count,6);
show_topics(IDX, data.wl);

end
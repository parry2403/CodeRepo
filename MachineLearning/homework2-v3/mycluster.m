function [ class ] = mycluster( bow, K )
%
% Your goal of this assignment is implementing your own text clustering algo.
%
% Input:
%     bow: data set. Bag of words representation of text document as
%     described in the assignment.
%
%     K: the number of desired topics/clusters. 
%
% Output:
%     class: the assignment of each topic. The
%     assignment should be 1, 2, 3, etc. 
%
% For submission, you need to code your own implementation without using
% any existing libraries

% YOUR IMPLEMENTATION SHOULD START HERE!
topics = K;
docs = size(bow,1);
words = size(bow,2);
% class = zeros(docs,1);
prior = 1/K*ones(1,K);
%likelihood = 1/K*ones(words,K);
%likelihood = randn(words,K);
likelihood = rand(words,K);
likelihood = likelihood./repmat(sum(likelihood),words,1);
expDoc = 1/docs*ones(docs,K);




%Expectation

for counter = 1:100
  %  for doc = 1:docs 
  %      den =0;
  %      for topic = 1:topics
   %         num = prior(1,topic);
    %        for word = 1:words
    %           num = num * (likelihood(word,topic)^bow(doc,word));
    %        end
           
    %        num = num * prod((likelihood(:,topic).^(bow(doc,:)')));
       
     %       expDoc(doc,topic) = num;
            
      %      den = den + num;
      %   end
 %       for topic = 1:topics
  %         expDoc(doc,topic) =  expDoc(doc,topic)/den;
  %      end
      %  expDoc(doc,:) =  expDoc(doc,:)/den;

   % end 
   % end
 %  for doc = 1:docs 
 %       size(likelihood(:,:));
 %       size(repmat(bow(doc,:)',1,topics));
 %       a =likelihood(:,:).^repmat(bow(doc,:)',1,topics);
 %       size(prod(a)) ;
 %       c= prior(1,:).*prod(a);
  %      size(c);
  %      size(sum(c));
  %      expDoc(doc,:) = c/sum(c);
      %  a =repmat(a',[1,1,words]);
  % end

        a =repmat(likelihood(:,:),1,1,docs).^permute(repmat(bow(:,:)',1,1,topics),[1 ,3 ,2]);
      
        l = reshape(prod(a),4,400);
        c= (repmat(prior(1,:),docs,1)').*l;
       
        expDoc = c'./repmat(sum(c),4,1)';
      %  size(a)
    % s   b = permute(repmat(expWord',[1,1,docs]),[1,3,2]);
    %   posterior = b.*a;

    %disp(sum(expDoc(1,:)));


    %Maximization


    
       %  for word = 1:words
         %    num = 0;
           %  for doc = 1:docs 
            %    num = num + (expDoc(doc,topic)*bow(doc,word));
            % end
            
        %     likelihood(word,topic) = sum(expDoc(:,topic).*bow(:,word));
        %     den = den +  sum(expDoc(:,topic).*bow(:,word));
        % end
     for topic = 1:topics 
        likelihood(:,topic) = (expDoc(:,topic)'*bow(:,:))';
         likelihood(:,topic) =  likelihood(:,topic)/sum(likelihood(:,topic));
     end
       prior(1,:) = sum(expDoc(:,:))/docs;
           %   for word = 1:words
       %      likelihood(word,topic) =   likelihood(word,topic)/den;
       %  end 
  %   for topic = 1:topics
           
         %    for doc = 1:docs 
         %       num = num + (expDoc(doc,topic));
         %    end
       %      prior(1,:) = sum(expDoc(:,:))/docs;
 
   %  end
 end
% 
% disp(expDoc);
[c,class] = max(expDoc,[],2);
end


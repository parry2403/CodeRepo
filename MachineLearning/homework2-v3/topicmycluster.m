function [ class ] = topicmycluster( bow, K )
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
expWord = randn(words,K);
expDoc = randn(docs,K);
posterior = randn(K,docs,words);

expWord = expWord./repmat(sum(expWord),words,1);
expDoc = expDoc./repmat(sum(expDoc),docs,1);

%Expectation
 
min =  1e-6
for counter = 1:25
    counter
 %   for doc = 1:docs 
  %      for word = 1:words
   %         den =0;
        %    for topic = 1:topics
        %        posterior(topic,doc,word) =prior(1,topic)*expDoc(doc,topic)*expWord(word,topic);
        %        den  = den + posterior(topic,doc,word) ;
        %    end
          %      size(posterior(:,:,:))
          %      size(prior)
           %     size(expDoc)
           %     size(expWord)
                
            %    posterior(:,doc,word) =prior(1,:)*expDoc(doc,:)*expWord(word,:);
            %    den  = den + posterior(topic,doc,word) ;
          %  end
          %  for topic = 1:topics
    %         den  = sum( posterior(:,doc,word));
     %        posterior(:,doc,word)  =  posterior(:,doc,word)/(1e-6 + den);
          %  end
     %   end
     %   size( prior(1,:))
     %   size(expDoc(:,:)')
     %   size(repmat(prior(1,:),docs,1).*expDoc(:,:))
        a =repmat(prior(1,:),docs,1).*expDoc(:,:);
        
        a =repmat(a',[1,1,words]);
      %  size(a)
        b = permute(repmat(expWord',[1,1,docs]),[1,3,2]);
        posterior = b.*a;
        for topic = 1:topics
            den  = sum(sum( posterior(topic,:,:)));
            posterior(topic,:,:)  =  posterior(topic,:,:)/(min + den);
        end



    

    %disp(sum(expDoc(1,:)));


    %Maximization


     for topic = 1:topics
         den =0;
      %   for word = 1:words
      %       num = 0;
      %       for doc = 1:docs 
      %          num = num + (posterior(topic,doc,word)*bow(doc,word));
       %      end
             
       %      expWord(word,topic) = num;
       %      den = den + num;
      %   end
     %    size(reshape( posterior(topic,:,:),docs,words));
     %   size( sum(reshape( posterior(topic,:,:),docs,words).*bow));
       %  for word = 1:words
       %      expWord(word,topic) =   expWord(word,topic)/(1e-6 + den);
       %  end 
         a =sum(reshape( posterior(topic,:,:),docs,words).*bow);
         b = sum(reshape( posterior(topic,:,:),docs,words).*bow,2);
         
         den = sum(a);
         expWord(:,topic) =  a/(min + den);
         expDoc(:,topic) =   b/(min +den);
         prior(1,topic) = den;
     end
   %  for topic = 1:topics
   %      den =0;
   %      for doc = 1:docs 
   %          num = 0;
   %          for word = 1:words
   %             num = num + (posterior(topic,doc,word)*bow(doc,word));
   %          end
   %          expDoc(doc,topic) = num;
   %          den = den + num;
   %      end
        % for doc = 1:docs
        %     expDoc(doc,topic) =   expDoc(doc,topic)/(1e-6 +den);
        % end 
     %    expDoc(:,topic) =   expDoc(:,topic)/(1e-6 +den);
         
    % end
   %  den =0;
   %  for topic = 1:topics
         
   %      for doc = 1:docs 
   %          num = 0;
   %          for word = 1:words
   %             num = num + (posterior(topic,doc,word)*bow(doc,word));
   %          end
   %      end
   %      prior(1,topic) = num;
   %      den =den+num;
   %  end
  %   for topic = 1:topics
   %     prior(1,topic) = prior(1,topic)/(1e-6 +den);
   %  end
     prior(1,:) = prior(1,:)/(min +sum( prior(1,:)));
     
 end
% 
% disp(expDoc);
class = expWord;
%[c,class] = max(expDoc,[],2);
end


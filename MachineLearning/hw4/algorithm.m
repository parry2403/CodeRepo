function prob = algorithm(q,price_move)

% plot and return the probability

seq = size(price_move,1);
emission = zeros(2,2);
emission(1,1)=q;
emission(2,2)=q;
emission(1,2)=1-q;
emission(2,1)=1-q;
ini=zeros(2,1);
ini(1,1)=.2;
ini(2,1)=.8;
p=.8;
transmission = zeros(2,2);
transmission(1,1)=p;
transmission(2,2)=p;
transmission(1,2)=1-p;
transmission(2,1)=1-p;
alpha = zeros(2,seq);
if price_move(1)==1
    alpha(1,1)=log(ini(1,1)*emission(1,1));
    alpha(2,1)=log(ini(2,1)*emission(2,1));
end
if price_move(1)==-1
    alpha(1,1)=log(ini(1,1)*emission(1,2));
    alpha(2,1)=log(ini(2,1)*emission(2,2));
end
for iter=2:seq
    if price_move(iter)==1
        a = log(exp(alpha(1,iter-1)))+log(transmission(1,1))+  log(emission(1,1));
        b= log(exp(alpha(2,iter-1)))+log(transmission(1,2))+log(emission(1,1));
        max1= max(a,b);
        min1=min(a,b);
        alpha(1,iter)=max1 +log(exp(min1-max1)+1);
     
        a = log(exp(alpha(1,iter-1)))+log(transmission(2,1))+  log(emission(2,1));
        b= log(exp(alpha(2,iter-1)))+log(transmission(2,2))+log(emission(2,1));
        max1= max(a,b);
        min1=min(a,b);
        alpha(2,iter)=max1 +log(exp(min1-max1)+1);
    end
    if price_move(iter)==-1
        a = log(exp(alpha(1,iter-1)))+log(transmission(1,1))+  log(emission(1,2));
        b= log(exp(alpha(2,iter-1)))+log(transmission(1,2))+log(emission(1,2));
        max1= max(a,b);
        min1=min(a,b);
        alpha(1,iter)=max1 +log(exp(min1-max1)+1);
     
        a = log(exp(alpha(1,iter-1)))+log(transmission(2,1))+  log(emission(2,2));
        b= log(exp(alpha(2,iter-1)))+log(transmission(2,2))+log(emission(2,2));
        max1= max(a,b);
        min1=min(a,b);
        alpha(2,iter)=max1 +log(exp(min1-max1)+1);
    end
end
alpha;

beta = zeros(2,seq);
if price_move(1)==1
    beta(1,seq)=0;
    beta(2,seq)=0;
end
if price_move(1)==-1
    beta(1,seq)=0;
    beta(2,seq)=0;
end
for iter=seq:-1:2
    if price_move(iter)==1
        a = log(exp(beta(1,iter)))+log(transmission(1,1))+log(emission(1,1));
        b=  log(exp(beta(2,iter)))+log(transmission(1,2))+log(emission(2,1));
        max1= max(a,b);
        min1=min(a,b);
        beta(1,iter-1)=max1 +log(exp(min1-max1)+1);
    %    beta(1,iter-1)=log(exp(beta(1,iter))*transmission(1,1)*emission(1,1)+exp(beta(2,iter))*transmission(1,2)*emission(2,1));
    %    beta(2,iter-1)=log(exp(beta(1,iter))*transmission(2,1)*emission(1,1)+exp(beta(2,iter))*transmission(2,2)*emission(2,1));
        a = log(exp(beta(1,iter)))+log(transmission(2,1))+log(emission(1,1));
        b=  log(exp(beta(2,iter)))+log(transmission(2,2))+log(emission(2,1));
        max1= max(a,b);
        min1=min(a,b);
        beta(2,iter-1)=max1 +log(exp(min1-max1)+1);
    end
    if price_move(iter)==-1
        a = log(exp(beta(1,iter)))+log(transmission(1,1))+log(emission(1,2));
        b=  log(exp(beta(2,iter)))+log(transmission(1,2))+log(emission(2,2));
        max1= max(a,b);
        min1=min(a,b);
        beta(1,iter-1)=max1 +log(exp(min1-max1)+1);
        a = log(exp(beta(1,iter)))+log(transmission(2,1))+log(emission(1,2));
        b=  log(exp(beta(2,iter)))+log(transmission(2,2))+log(emission(2,2));
        max1= max(a,b);
        min1=min(a,b);
        beta(2,iter-1)=max1 +log(exp(min1-max1)+1);
        %  beta(1,iter-1)=log(exp(beta(1,iter))*transmission(1,1)*emission(1,2)+exp(beta(2,iter))*transmission(1,2)*emission(2,2));
     %  beta(2,iter-1)=log(exp(beta(1,iter))*transmission(1,1)*emission(1,2)+exp(beta(2,iter))*transmission(2,2)*emission(2,2));
    end

end
beta;
joint = zeros(2,seq);
for iter=1:seq
        joint(1,iter)=alpha(1,iter)+beta(1,iter);
        joint(2,iter)=alpha(2,iter)+beta(2,iter);
end
joint;

probs = zeros(2,seq);
for iter=1:seq
       % p_x =  
        probs(1,iter)=joint(1,iter)-log(exp(alpha(1,seq)) +exp(alpha(2,seq)));
        probs(2,iter)=joint(2,iter)-log(exp(alpha(1,seq)) +exp(alpha(2,seq)));
end
exp(probs(1,:))
plot(1:seq,exp(probs(1,:)))

a=0;
b=10;
n = 2.^(1:10);
f = @(x)cos(2*x);
actual = sin(20)/2;
errors = zeros(10,1);
for i=1:10
    preds(i,1) = Simpson(f,a,b,n(i)); 
    errors(i,1)= abs(actual - Simpson(f,a,b,n(i))); 
end

ratios = zeros(10,1);
for j=2:10
   ratios(j,1)=errors(j-1)/errors(j); 
end
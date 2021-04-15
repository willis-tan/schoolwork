function I = Simpson(f,a,b,n)
    %UNTITLED Summary of this function goes here
    %Detailed explanation goes here
    k = n/2;
    h = (b-a)/n;
    sum1 = 0;
    sum2 = 0;
    for i = 2:k
        sum1 = sum1 + f(a+(2*i-2)*h);
    end
    for j = 1:k
        sum2 = sum2 + f(a+(2*j-1)*h);
    end
    I = h*( f(a)+2*sum1+4*sum2+f(b) )/3;
end


# example
a = 2;
b <- 3;

mySecFun<-function(v,M) 
{
    u=c(0,0,0,0);
    for(i in 1:length(v))
    {
      u[i]=myFirstFun(v[i]);
    }
    return(u);
}

Sqv=mySecFun(v);
Sqv;

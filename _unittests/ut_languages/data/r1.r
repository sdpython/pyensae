# example
a = 2;
b <- 3;

mySecFun<-function(v,M) 
{
    u=c(0,0,0,0);
    for(i in 1:length(v))
    {
      if (i == 1) {
        u[i]=myFirstFun(v[i]);
        }
        else  {
            u[i]=mySecondFun(v[i])+2;
            u[i+1]=myThirdFun(v[i]);
        }
    }
    return(u);
}

Sqv=mySecFun(v);
Sqv;

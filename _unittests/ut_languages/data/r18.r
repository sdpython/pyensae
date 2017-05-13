nb=function(y=1930) {
    debut=1816
    MatDFemale=matrix(D$Female,nrow=111)
    colnames(MatDFemale)=debut+0:198
    cly=(y-debut+1):111
    deces=diag(MatDFemale[:,cly[cly%in%1:199]])
    return(c(B$Female[B$Year==y],deces))
}

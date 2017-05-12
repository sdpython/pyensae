## some comments

"test.machine.chouette.something" <- function()
{
    ## some other comment
    func <- function(infile, csch, predmod)
    {
        impnode <- zoo.test(
            infile = "$infile"
            , dot = "$dotdot"
            , csch = csch
            )
        obj <- waouh(
            impnode, nono, trnode
            , inputs = list(infile = infile)
            , outputs = list(predmod = predmod)
            )

        ## one
        ## comment
        exjs <- epr(unclass(tojs(obj)))
        exjs <- epr(tojs(obj))
        exjs <- epr(obj)
    }

    env(func) <- asNamespace("namesp")

    ## last
    bdf <- within(iris, param <- spec == "setosa")
    bf <- tempfile("bf", fet = ".txt")
    ds(bdf, btx, ow = TRUE)
}

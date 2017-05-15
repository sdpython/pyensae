onefunction <- function()
{
    df[["v"]] <- I(sapply(seq(nrow(df)), function(i, r) r[seq(i%%length(lett))], r))
}

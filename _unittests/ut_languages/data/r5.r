onefunc <- function()
{
    on.exit(if(file.exists(filename)) afunction(filename), add = TRUE)
}

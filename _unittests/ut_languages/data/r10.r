onefunction <- function()
{
    od <- tempfile("od", fileext = ".pdf") # ccc
    on.exit(if(file.exists(od)) ul(od), add = TRUE)
}

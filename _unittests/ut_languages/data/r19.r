some = function() 
{
	t <- bquote(list(a = !(age == .(whichAge))))
	r <- bquote(!(age == .(whichAge)))
}

set terminal pdf
set output 'errors4n3-zoom.pdf'
set yrange[0:0.08]
set xrange[2000:]
plot for[ i = 2:10] 'errors.dat' using 1:i title columnhead with lines
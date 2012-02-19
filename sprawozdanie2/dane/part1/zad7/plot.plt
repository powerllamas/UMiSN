set terminal pdf

set output "test.pdf"
set ylabel "Procent przypadk�w"
set xlabel "Pr�g akceptacji"
set key center top
set key box 
plot for [i = 2:4] 'test.dat' using 1:i with lines lw 3 title columnhead
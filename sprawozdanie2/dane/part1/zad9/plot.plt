set terminal pdf
set output "verify.pdf"
set ylabel "U�amek wszystkich klasyfikacji"
set xlabel "Stosunek wielko�ci zbioru weryfikuj�cego do ca�ego zbioru"
set key box right center
set yrange[-0.1:1.1]  
plot for [i = 2:4] "results.dat" using 1:i with lines title columnheader(i) lw 3
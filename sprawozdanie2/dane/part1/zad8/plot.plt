set terminal pdf
set output "damages.pdf"
set ylabel "Trafnoœæ klasyfikacji"
set xlabel "Liczba wyzerowanych wag"
unset key
set xrange [-1:13]
set yrange [0.65:]
set xtics 0,1.0,12
plot "results2.dat" using 1:2
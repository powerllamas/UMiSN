set style data histograms
set style histogram rowstacked
set style fill solid border 1
set terminal pdf
set output "bupa-rbf-mlp.pdf"
set boxwidth 0.75
set key outside
set yrange [0:1.1]
set xlabel "Rodzaj sieci"
set ylabel  "Czêœæ wszsytkich klasyfikacji"
#
plot 'bupa-rbf-mlp.dat' using 2:xticlabels(1) title column(2), for [i=3:4] '' using i title column(i)
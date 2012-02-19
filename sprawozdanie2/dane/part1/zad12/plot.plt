set style data histograms
set style histogram rowstacked
set style fill solid border 1
set terminal pdf
set output "compare.pdf"
set boxwidth 0.75
set key outside
set yrange [0:1.1]
set xlabel "Rodzaj sieci"
set ylabel  "Czêœæ wszsytkich klasyfikacji"
#
plot 'compare.dat' using 2:xticlabels(1) title column(2), '' using 3 title column(3)
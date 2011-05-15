#
set term svg
set output "p2t2-compare-sizes.svg"
set title "Średni rozmiar opisu danej reprezentacji danych"
set palette gray
set style data histogram
set auto x
#set yrange [0:100]
set style fill solid border -1
set boxwidth 0.8
plot for [i=2:4] "p2t2-compare-sizes.dat" u i:xtic(1) ti col
#

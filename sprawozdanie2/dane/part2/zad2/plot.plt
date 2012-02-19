set terminal pdf
set xrange[0:800]
set yrange[0:5]
set xlabel "Ilo�� mutacji"

set output "neurons.pdf"
set ylabel "Liczba neuron�w"
plot 'results.dat' using 1:3 with linespoints lw 2 notitle
unset output

set output "connections.pdf"
set ylabel "Liczba po��cze�"
plot 'results.dat' using 1:2 with linespoints lw 2 notitle

set output "combo.pdf"
set ylabel "Ilo��"
set xlabel "Pokolenie"
plot for [i = 2:3] 'results.dat' using 1:i with lines lw 2 title columnhead
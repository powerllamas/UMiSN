set terminal pdf
set xrange[0:200]

set output "brain_size.pdf"
set ylabel "Liczba neuron�w"
set xlabel "Pokolenie"
plot 'results.dat' using 1:3 with linespoints lw 2
unset output

set output "number_of_connections.pdf"
set ylabel "Liczba po��cze�"
set xlabel "Pokolenie"
plot 'results.dat' using 1:2 with linespoints lw 2

set output "combo.pdf"
set ylabel "Ilo��"
set xlabel "Pokolenie"
plot for [i = 2:3] 'results.dat' using 1:i with lines lw 2 title columnhead
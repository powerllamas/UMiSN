set terminal pdf
set output "proteins12.pdf"
set yrange [0:4]
set xrange [0:5]
unset tics
plot 'proteins12.dat' using 1:2:3 with labels notitle
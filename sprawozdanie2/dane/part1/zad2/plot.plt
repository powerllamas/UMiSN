set terminal pdf
set key left top
set key box 
set yrange [-0.5:1.5]
set xrange [-0.5:1.5]
set xlabel ""
set ylabel  ""

set output "separacja_xor_ukryta.pdf"

plot ((-3.618+6.897*x)/6.945) lw 3, ((2.762+5.514*x)/5.808) lw 3, 'points.dat' using 1:2:3 with labels notitle

set output "separacja_and.pdf"
set key right top
set yrange [-0.1:1.5]
set xrange [-0.1:1.5]
plot (-x + 9.51/6.28) lw 3, 'points.dat' using 1:2:3 with labels notitle


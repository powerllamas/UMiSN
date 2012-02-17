set encoding iso_8859_2
set terminal pdf
set boxwidth 0.9 relative
set style fill solid 1.0
unset key
set tics nomirror

set ylabel "Czas nauki [epoki]"
set xlabel "Algorytm"

    set output "epochs-pima.pdf"
    set yrange [0:70]
    plot "PIMA.dat" using 1:2:xticlabels(4) with boxes

    set output "epochs-iris.pdf"
    set yrange [0:220]
    plot "IRIS.dat" using 1:2:xticlabels(3) with boxes

set ylabel "B³±d ¶redniokwadratowy sieci"
    set output "epochs-pima-errors.pdf"
    set yrange[0:1]
    plot "PIMA.dat" using 1:3:xticlabels(4) with boxes
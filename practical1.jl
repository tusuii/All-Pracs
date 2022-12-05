# Practical 1:-  Implement Contour Plots.
using PlotlyJS  # dependency PlotlyJS


x = contour(
    z=[
        11      10.625      12.5       10.625     20
        5.625    6.25       8.125      11.25      15.625
        2.5      13.125      10.         8.125      12.5
        0.625    12.25       3.125      7.25       10.625
        5        0.625      2.5        5.625      10
    ]'
)
plot(x)


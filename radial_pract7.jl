using Surrogates
using LinearAlgebra
f = x -> x[1] * x[2]
lb = [1.0, 2.0]
ub = [10.0, 8.5]
x = sample(50, lb, ub, SobolSample())
y = f.(x)
my_radial_basis = RadialBasis(x, y, lb, ub)
approx = my_radial_basis((1.0, 1.4))

# using Surrogates
using Plots
f = x -> log(x) * x^2 + x^3
lb = 1.0
ub = 10.0
x = sample(50, lb, ub, SobolSample())
y = f.(x)
my_radial_basis = RadialBasis(x, y, lb, ub)
approx = my_radial_basis(5.4)
plot(x, y, seriestype=:scatter, label="Sampled points", xlims=(lb, ub), legend=:top)
plot!(f, label="True function", xlims=(lb, ub), legend=:top)
plot!(my_radial_basis, label="Surrogate function", xlims=(lb, ub), legend=:top)
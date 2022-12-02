#  practical 6c Adadelta 

abstract type DescentMethod end
mutable struct Adadelta <: DescentMethod
    γs # gradient decay
    γx # update decay
    ϵ # small value
    s # sum of squared gradients
    u # sum of squared updates
end

f(x) = x^4 - 14 * x^3 + 60 * x^2 - 70 * x

function step!(f, ∇f, x)
    g = ∇f(x)
    γs = 1
    γx = 1
    ϵ = 0.001
    s = 1
    u = 1

    s = γs * s + (1 - γs) * g .* g
    Δx = -(sqrt.(u) .+ ϵ) ./ (sqrt.(s) .+ ϵ) .* g
    u = γx * u + (1 - γx) * Δx .* Δx
    return x + Δx
end

using Flux
x = 0.1
∇f(x) = gradient(f, x)[1];

step!(f, ∇f, x)
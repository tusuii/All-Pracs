# CREDIT/REFERENCE :- https://www.jihongzhang.org/post/gradient-descent-via-julia/
# import Pkg; Pkg.add("RDatasets")
# import Pkg; Pkg.add("DataFrames")

using RDatasets
using DataFrames

mtcars = dataset("datasets", "mtcars")

function gradientDesc(x, y, learn_rate, conv_threshold, n, max_iter)
    β = rand(Float64, 1)[1]
    α = rand(Float64, 1)[1]
    ŷ = α .+ β .* x
    MSE = sum((y .- ŷ).^2)/n
    converged = false
    iterations = 0

    while converged == false
        # Implement the gradient descent algorithm
        β_new = β - learn_rate*((1/n)*(sum((ŷ .- y) .* x)))
        α_new = α - learn_rate*((1/n)*(sum(ŷ .- y)))
        α = α_new
        β = β_new
        ŷ = β.*x .+ α
        MSE_new = sum((y.-ŷ).^2)/n
        # decide on whether it is converged or not
        if (MSE - MSE_new) <= conv_threshold
            converged = true
            println("Optimal intercept: $α; Optimal slope: $β")
        end
        iterations += 1
        if iterations > max_iter
            converged = true
            println("Optimal intercept: $α; Optimal slope: $β")
        end
    end
end

#print(mtcars)
#gradientDesc(mtcars[:,:Disp], mtcars[:,:MPG], 0.0000293, 0.001, 32, 2500000)

gradientDesc(mtcars[:,:Disp], mtcars[:,:MPG], 0.0000293, 0.001, 32, 2500)
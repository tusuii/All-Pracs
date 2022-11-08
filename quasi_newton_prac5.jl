# import Pkg; Pkg.add("Optim")  #library used

function g!(storage, x)
    storage[1] = -2.0 * (1.0 - x[1]) - 400.0 * (x[2] - x[1]^2) * x[1]
    storage[2] = 200.0 * (x[2] - x[1]^2)
end

function h!(storage, x)
    storage[1, 1] = 2.0 - 400.0 * x[2] + 1200.0 * x[1]^2
    storage[1, 2] = -400.0 * x[1]
    storage[2, 1] = -400.0 * x[1]
    storage[2, 2] = 200.0
end

using Optim
f(x) = (1.0 - x[1])^2 + 100.0 * (x[2] - x[1]^2)^2
optimize(f, [0.0, 0.0], LBFGS())
optimize(f, g!, [0.0, 0.0], LBFGS())
optimize(f, g!, h!, [0.0, 0.0], LBFGS())
#Path finding using Ant Colony Optimization with an application
# import Pkg; Pkg.add("LightGraphs")


function ant_colony_optimization(G, lengths;
    m=1000, k_max=100, α=1.0, β=5.0, ρ=0.5,
    η=Dict((e.src, e.dst) => 1 / lengths[(e.src, e.dst)]
           for e in edges(G)))
    τ = Dict((e.src, e.dst) => 1.0 for e in edges(G))
    x_best, y_best = [], Inf
    for k in 1:k_max
        A = edge_attractiveness(G, τ, η, α=α, β=β)
        for (e, v) in τ
            τ[e] = (1 - ρ) * v
        end
        for ant in 1:m
            x_best, y_best = run_ant(G, lengths, τ, A, x_best, y_best)
        end
    end
    return x_best
end

ant_colony_optimization([1,4,5,8,7],5)
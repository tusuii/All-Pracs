P=Dict(0 => 100, 1 => 115, 2 => 145)
function padovan_topdown(n, P)
    if !haskey(P, n)
        P[n] = n < 3 ? 1 : padovan_topdown(n - 2, P) + padovan_topdown(n - 3, P)
    end
    return P[n]
end
function padovan_bottomup(n)
    for i in 3:n
        P[i] = P[i-2] + P[i-3]
    end
    return P[n]
end

println("padovan topdown -> " ,padovan_topdown(2))
println("padovan bottomup -> " ,padovan_bottomup(1))
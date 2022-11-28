function knapsack(v, w, w_max)
    n = length(v)
    y = Dict((0, j) => 0.0 for j in 0:w_max)
    for i in 1:n
        for j in 0:w_max
            y[i, j] = w[i] > j ? y[i-1, j] : max(y[i-1, j],y[i-1, j-w[i]] + v[i])
        end
    end
    x, j = falses(n), w_max
    for i in n:-1:1
        if w[i] ≤ j && y[i, j] - y[i-1, j-w[i]] == v[i]
            x[i] = true
            j -= w[i]
        end
    end
    return x
end

#                                          v to choose from  0+10+ 0+0 +40 => 50 (total)
println("0-1 knapsack problem:- ",knapsack([0,50,60,60,120],[0,10,15,20,40],50))
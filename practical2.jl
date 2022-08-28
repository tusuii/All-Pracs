#Practical 2 :- Implement Fibonacci and Golden section search.

f(x) = x^4 - 14*x^3 + 60x^2 - 70*x
function fbs(f, a, b, N, ϵ=0.01)
    function F(n)
        # We choose F₀=1, F₁=1, F₂=2, F₃=3, ...
        ϕ = (1 + √5) / 2
        Fₙ = (ϕ^(n + 1) - (1 - ϕ)^(n + 1)) / √5
        return Fₙ
    end
    ρ = 1 - F(N) / F(N + 1)
    d = (1 - ρ) * b + ρ * a
    fd = f(d)

    k = 1
    while k <= N
        c = ρ * b + (1 - ρ) * a
        fc = f(c)

        if (fc < fd)
            d, b, fd = c, d, fc
        else
            a, b = b, c
        end

        k = k + 1

        if k == N
            ρ = 0.50 - ϵ
        else
            ρ = 1 - F(N - k + 1) / F(N - k + 2)
        end

    end
    return a < b ? (a, b) : (b, a)
end

# function call
fibo = fbs(f, 0, 2, 4, 0.05)    
println(fibo)


# Golden search

function gss(f, a, b, N)
    # The golden ratio
    ϕ = (sqrt(5) - 1)/2.0
    ρ = 1-ϕ
    
    d = (1-ρ)*b + ρ*a
    fd = f(d)
    
    for i in 1:N
        c = ρ*b + (1-ρ)*a
        fc = f(c)
        
        if(fc < fd)
            d, b, fd = c, d, fc
        else 
            a, b = b, c
        end   
    end
    
    return a < b ? (a, b) : (b, a)
end

a, b = gss(f, 0.0, 2.0, 10)

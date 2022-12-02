# import Pkg; Pkg.add("AntColony")

using AntColony
distance_matrix = rand(50, 50)
typeof(distance_matrix)

aco(distance_matrix, is_tour = true)
aco(distance_matrix, start_node = 1, end_node = 50)
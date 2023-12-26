# https://rpubs.com/Rajeshree/1044169
# install.packages("tidyverse", type="source")
library(tidyverse)

head(billboard)

#pivot_longer(): Pivot data from wide to long
billboard_long <- billboard |> 
  pivot_longer(
    cols = starts_with('wk'),
    names_to = 'week',
    values_to = 'rank'
  )

billboard_long

#pivot_wider(): Pivot data from long to wide
billboard_long |> 
  pivot_wider(
    names_from = week,
    values_from = rank
  )

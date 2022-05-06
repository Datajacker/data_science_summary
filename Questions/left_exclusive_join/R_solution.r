library(dplyr)
df = anti_join(tb1, tb2, by = c('year', 'id'))
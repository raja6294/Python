theater = [[1, 0], [0, 1]]  # 1=Taken, 0=Empty

for r, row in enumerate(theater):   
  for c, seat in enumerate(row):      
    if seat == 1:        
      continue    
    print(f"Open: R{r}C{c}")
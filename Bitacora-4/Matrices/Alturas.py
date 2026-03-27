altitudes = [
    [1000, 5000, 10000, 12000],  
    [1500, 6000, 11000, 13000],  
    [2000, 5500, 10500, 12500]   
]

# altitud máxima de cada avión
for i in range(3):  
    max_altura = altitudes[i][0]
    
    for j in range(4): 
        if altitudes[i][j] > max_altura:
            max_altura = altitudes[i][j]
    
    print("Altitud máxima del avión", i+1, ":", max_altura, "metros")

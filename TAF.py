
file=open("Table de multiplication.txt","w+")
for i in range(10):
    file.write(f"\nla table de multiplication de {i+1}: \n")
    for j in range(10):
        file.write(f"{i+1} × {j+1} = {(i+1)*(j+1)}\n")
file.close()
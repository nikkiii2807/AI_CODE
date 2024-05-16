def objective_function(x,target):
    return (x**2)-target

def hill(target):
    current_sol=0.0
    epsilon=0.1
    while True:
        current_obj=objective_function(current_sol,target)
        if abs(current_obj)<epsilon:
            break
        if current_obj<0:
            current_sol+=0.001
        elif current_obj>0:
            current_sol-=0.001

    return current_sol

target=int(input("Enter target: "))
sol=hill(target)
print("The root of target is ",sol)
        
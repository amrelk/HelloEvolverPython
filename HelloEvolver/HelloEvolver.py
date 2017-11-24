from random import randint
def fitness(current,target):
    x = 0
    for ind in range(len(target)):
        x += abs(ord(target[ind])-ord(current[ind]))
    return x

def mutate(current):
    arr = [*current]
    ind = randint(0,len(current)-1)
    arr[ind] = chr(ord(arr[ind]) + randint(-1,1))
    return ''.join(arr)

def randomstring(length):
    string = []
    for i in range(length):
        string.append(chr(randint(32,126)))
    return ''.join(string)

def sort(pop, target):
    changed = True
    while changed:
        changed = False
        for i in range(len(pop) - 1):
            if fitness(pop[i],target) > fitness(pop[i+1],target):
                pop[i], pop[i+1] = pop[i+1], pop[i]
                changed = True
    return pop

def breed(a, b):
    newstr = []
    for i in range(len(a)):
        if randint(0,1) == 0:
            newstr.append(a[i])
        else:
            newstr.append(b[i])
    return ''.join(newstr)

targetstr = "Hello, World!"
popsize = 100
mutationrate = 0.02 #this does nothing - yet

lowestscore = 100
population = []
for i in range(popsize):
    population.append(randomstring(len(targetstr)))


while lowestscore > 0:
    sort(population, targetstr)
    for i in range(int(len(population)/2)-1):
        population[i+int(len(population)/2)] = breed(population[i],population[i+1])
    for i in range(len(population)):
        if randint(0,10) == 0:
            population[i] = mutate(population[i])
    sort(population, targetstr)
    lowestscore = fitness(population[0],targetstr)
    print(population[0], " : ", lowestscore)
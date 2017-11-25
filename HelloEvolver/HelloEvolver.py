from random import randint
import timeit

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
    
    if len(pop) < 2:
        return pop
    fitnesses = {}
    for i in range(len(pop)):
        fitnesses[pop[i]] = fitness(pop[i], target)

    # 1. get pivot (random element)
    pivot = pop[randint(0, len(pop) - 1)]

    # 2. put all smaller to left, into a group
    left = [e for e in pop if e is not pivot and fitnesses[e] <= fitnesses[pivot]]

    # 3. put all greater to right, into a group
    right = [e for e in pop if e is not pivot and fitnesses[e] > fitnesses[pivot]]

    # repeat for those 2 new groups
    return sort(left,target) + [pivot] + sort(right,target)

'''
    changed = True
    while changed:
        changed = False
        for i in range(len(pop) - 1):
            if fitnesses[pop[i]] > fitnesses[pop[i+1]]:
                pop[i], pop[i+1] = pop[i+1], pop[i]
                changed = True
    return pop
'''
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
mutationrate = 0 #the higher the number, the lower the mutation rate - I don't feel like calculating the actual relationship

lowestscore = 50
population = []
for i in range(popsize):
    population.append(randomstring(len(targetstr)))

'''
for i in population:
    print(i, " : ", fitness(i, targetstr))
population = sort(population, targetstr)
print("\n\n")
for i in population:
    print(i, " : ", fitness(i, targetstr))
'''

while lowestscore > 0:
    sort(population, targetstr)
    for i in range(int(len(population)/2)-1):
        population[i+int(len(population)/2)] = breed(population[i],population[i+1])
    for i in range(len(population)):
        if randint(0,mutationrate) == 0:
            population[i] = mutate(population[i])
    population = sort(population, targetstr)
    lowestscore = fitness(population[0],targetstr)
    print(population[0], " : ", lowestscore)

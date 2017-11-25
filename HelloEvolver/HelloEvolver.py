from random import randint
def asciidict(start,stop):
    ascii = {}
    for i in range(start, stop):
        ascii[chr(i)] = i
    return ascii;
def fitness(current,target):
    x = 0
    for ind in range(len(target)):
        i = ascii[target[ind]]-ascii[current[ind]]
        if i > 0:
            x += i
        else:
            x -= i
    return x
def mutate(current):
    arr = [*current]
    ind = randint(0,len(current)-1)
    arr[ind] = chr(ascii[arr[ind]] + randint(-1,1))
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
    pivot = pop[randint(0, len(pop) - 1)]
    left = [e for e in pop if e is not pivot and fitnesses[e] <= fitnesses[pivot]] #put all smaller to left, into a group
    right = [e for e in pop if e is not pivot and fitnesses[e] > fitnesses[pivot]] #put all greater to right, into a group
    return sort(left,target) + [pivot] + sort(right,target)
def breed(a, b):
    newstr = []
    for i in range(len(a)):
        if randint(0,1) == 0:
            newstr.append(a[i])
        else:
            newstr.append(b[i])
    return ''.join(newstr)

ascii = asciidict(10,150)
targetstr = "Hello, World!"
popsize = 1000
mutationrate = 3 #the higher the number, the lower the mutation rate - I don't feel like calculating the actual relationship

lowestscore = 50
population = []
for i in range(popsize):
    population.append(randomstring(len(targetstr)))

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

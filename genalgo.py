import random
import numpy as np

# Defining constants
ROWS = 6
COLS = 7
POPULATION_SIZE = 100
MUTATION_RATE = 0.1
NUM_GENERATIONS = 100

# Representing the Connect Four board as a numpy array
board = np.zeros((ROWS, COLS))

# Initializing the population of potential solutions
population = [np.random.randint(0, COLS, ROWS) for i in range(POPULATION_SIZE)]

def fitness(individual):
	# Evaluate the fitness of an individual by counting the number of 
	# connecting fours it has achieved
	fitness = 0
	for row in range(ROWS):
		for col in range(COLS):
			if individual[row] == col:
				fitness += 1
	return fitness

def crossover(parent1, parent2):
	# Perform crossover between two individuals to produce offspring
	crossover_point = np.random.randint(0, ROWS)
	offspring = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
	return offspring

def mutate(individual):
	# Perform mutation on an individual to introduce genetic diversity
	for i in range(ROWS):
		if np.random.uniform(0, 1) < MUTATION_RATE:
			individual[i] = np.random.randint(0, COLS)
	return individual

for generation in range(NUM_GENERATIONS):
	# Evaluate the fitness of each individual in the population
	fitness_vals = [fitness(individual) for individual in population]

	# Select the top individuals as parents for the next generation
	parents = [population[np.argmax(fitness_vals)] for i in range(POPULATION_SIZE//2)]

	# Generate offspring from the selected parents
	children = []
	for i in range(0, len(parents), 2):
		child1 = crossover(parents[i], parents[i+1])
		child2 = crossover(parents[i+1], parents[i])
		children.append(child1)
		children.append(child2)

	# Mutate some of the offspring to introduce genetic diversity
	for i in range(len(children)):
		children[i] = mutate(children[i])

	# Replace the old population with the new offspring
	population = children

# Get the best individual from the final generation
best_individual = population[np.argmax(fitness_vals)]

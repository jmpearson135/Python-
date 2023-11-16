# John Pearson
# CS 100 2020F Section 111
# HW 02, September 16, 2020

#1
grades = ['A', 'B', 'A', 'F', 'D', 'C', 'D', 'F', 'A', 'B']
#grades = ['B', 'A', 'B', 'F', 'C', 'F', 'D','A', 'A', 'F']
#second grades variable I commented out to swap and test to make sure if was counting properly
frequency = [grades.count('A'), grades.count('B'), grades.count('C'), grades.count('D'), grades.count('F')]
print(" Number of A's:",frequency[0],"\n","Number of B's:", frequency[1],"\n","Number of C's:", frequency[2],"\n","Number of D's:", frequency[3],"\n","Number of F's:", frequency[4])

#2
#A.
dog_breeds = ['Collie', 'Sheepdog', 'Chow', 'Chihuahua']

#B.
herding_dogs = dog_breeds[0:2]
print(herding_dogs)

#C.
tiny_dogs = dog_breeds[-1]
print(tiny_dogs)

#D.
print('Persian' in dog_breeds)

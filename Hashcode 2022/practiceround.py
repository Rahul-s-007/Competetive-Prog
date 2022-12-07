import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\output.txt","w")

# Read the number of clients
C = int(input())

# Create a set to store the ingredients
ingredients = set()

# Iterate over the clients
for i in range(C):
  # Read the ingredients the client likes
  arr = [str(x) for x in input().split()]
  L = int(arr[0])
  likes = set(arr[1::])
  #L = int(input())
  #likes = set(input().split()[1:])
  
  arr = [str(x) for x in input().split()]
  # Read the ingredients the client dislikes
  D = int(arr[0])
  dislikes = set(arr[1::])
  #D = int(input())
  #dislikes = set(input().split()[1:])

  # Update the set of ingredients
  ingredients = ingredients.union(likes).difference(dislikes)

# Print the number of ingredients and the list of ingredients
print(len(ingredients), *ingredients)
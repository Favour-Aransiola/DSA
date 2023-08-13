# Each graph is made up of nodes and edges
# It solves two questions:
#   Is there a path from A to B
#   What is the shortest path from A to B

# A Queue is a FIFO data structure.
# A Stack is a LIFO data structure.


from collections import deque, defaultdict




def firstBreadthSearch(graph,initial):
    searchQueue = deque()
    searchQueue+=graph[initial]
    searchedArray = []

    while searchQueue:
        person = searchQueue.popleft()
        print(searchQueue)
        if person not in searchedArray:
            print(person)
            if person =="1":
                print("Person found")
                return True
            else:
                searchQueue+=graph[person]
                searchedArray.append(person)
                
    return False





graph = defaultdict(list)
graph["you"] = ["a","b"]
graph["a"] =["1","2","3"]
graph["b"] = []
graph["1"] =[]
graph["2"]=[]
graph["3"]=[]

print(firstBreadthSearch(graph,"you"))
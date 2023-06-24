
import math

def dijkstra(graph, start):

    #intialize tent and confirm dict
    tentative={}
    confirmed={}
    #add start node and cost to comfrimed dict
    confirmed[start]=0
    #place start and neighbor on tent\
    for node, distance in graph[start].items():
        tentative[node]=distance
    #set next to the node added to confirm
    next = start
    #while tent dict still has nodes
    while tentative:
        shortest_distance=math.inf
        #select node from tent with lowest cost
        for node, distance in tentative.items():
            if distance < shortest_distance:
                shortest_distance=distance
                next = node

        #add lowest cost node to confirmed dict and update next
        confirmed[next]=shortest_distance
        #remove next node from tent
        tentative.pop(next)
        #plaqce next node neighbor on tent list
        for node, distance in graph[next].items():
            cost=confirmed[next]+distance
            #if neighbot not in tent, add to tent
            #if neihjbor in tent, update cost if nesseccary
            if node in confirmed:
                continue
            elif (node in tentative) and (cost < tentative[node]):
                tentative[node]=cost
            elif node not in tentative:
                tentative[node]=cost
    return confirmed



def main():
   
   graph={
      'A':{'B':5,'C':10},
      'B':{'A':5, 'C':3, 'D':11},
      'C': {'A':10, 'B':3, 'D':2},
      'D':{'B':11, 'C':2}
   }

   start_node = 'D'
   distances=dijkstra(graph, start_node)

   for node, distance in distances.items():
    print(f"{node} -> {distance}")

main()
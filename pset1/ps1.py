###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    total = []
    copy  = dict.copy(cows)
    sorted_list = sorted(cows.values(),reverse= True)
    totalcost = 0

    while(len(sorted_list)!=0):
        totalcost=0
        result = []
        for i in range(len(sorted_list)):
            if ((totalcost+sorted_list[i] )<= limit):
                totalcost+= sorted_list[i]
                for key in copy:
                    if(cows[key]==sorted_list[i]):
                        entry = key
                result.append(entry)
                del copy[entry]

        total.append(result)
        for i in result:
            if cows[i] in sorted_list:
                sorted_list.remove(cows[i])    
    return total


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.
    
    The brute force heuristic should follow the following method:
    1) Enumerate all possible combinations of trips the cows can take
    2) Return the list of trips which has the minimum number of trips and that doesn't break the constraint
    
    Parameters:
    cows - a dictionary of name (string), weight (float) pairs
    limit - weight limit of the spaceship
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
"""

    list = []
    for partition in get_partitions(cows.keys()):
        list.append(partition)
        
    z = []
    
    for i in range(len(list)):
        a = []        
        for j in range(len(list[i])):
            b = []
            for k in list[i][j]:
                b.append(cows[k])
            if sum(b) > limit:
                break
            a.append(list[i][j])
        
        if len(a) == len(list[i]):
            z.append(a)
            
    numTrips = []
    for tlist in z:
        numTrips.append(len(tlist))
    
    for tripsList in z:
        if len(tripsList) == min(numTrips):
            return tripsList

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    greedy_start = time.time()
    greedy_results = greedy_cow_transport(cows, limit = 10)
    greedy_end = time.time()
    print('Greedy Algorithm time:', greedy_end -greedy_start)
    brute_force_start = time.time()
    brute_force_results = brute_force_cow_transport(cows, limit = 10)
    brute_force_end = time.time()
    print('Brute force time:', brute_force_end - brute_force_start)
    print('Greedy Algorithm results:', greedy_results)
    print('Number of trips returned by Greedy Algorithm:', len(greedy_results))
    print('Brute Force Algorithm results:', brute_force_results)
    print('Number of trips returned by Brute Force Algorithm:', len(brute_force_results))


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=100
print(cows)

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))



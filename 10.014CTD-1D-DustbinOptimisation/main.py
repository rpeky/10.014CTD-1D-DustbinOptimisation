import time
import Graph

# Object generation
# graph id format
def generate_Graph(graphid):
    g = Graph.Graph(graphid)
    return g

#User input functions
#Terminal input output
def output_buildingdecision_query_userinput():
    while True:
        buildings = ['1', '2', '3', '5']
        b_choice = input('Buildings: 1, 2, 3, 5. Enter building choice: ')
        if b_choice in buildings:
            print('Selected building: Building {}'.format(b_choice))
            return output_listoffloorplans_query_userinput(b_choice)
        else:
            print ('Enter a valid building number (1, 2, 3, 5).')    


def output_listoffloorplans_query_userinput(b_choice):
    while True:
        f_choice = input('Enter floor choice: ')
        if f_choice.isnumeric():
            try:
                return output_choice_processed(b_choice,f_choice)
            except KeyError:
                print ('Enter a floor number from 2 to 7.')
        else:
            print('Enter a valid integer.')
            
def output_choice_processed(b_choice,f_choice):
    confirmation = ['y','Y','1','continue']
    choice_processed = "B" + b_choice + "_F" + f_choice + "_"
    c_processed = "Building " + b_choice + " Level " + f_choice
    print('Chosen Floor: ' + c_processed + ". Enter y to confirm, n to reselect.")
    if input('Confirm?\n') in confirmation:
        return choice_processed
    else:
        return output_buildingdecision_query_userinput()

#if graph exists
#write a function to display the possible points from the graph dictionary (can use the return startpoint fn in graph.py)
def startpoints(curr_graph):
    lift_start=curr_graph.return_startpoints()
    misc_start=curr_graph.return_allnodes()
    for node in misc_start:
        if node in lift_start:
            misc_start.remove(node)
    return 'Lifts:\n{}\nDustbins:\n{}\n'.format(lift_start,misc_start)

#write a function to use the above function's list of points to query starting point from user
    #   floorplan naming convention
    #   D_{LOCATION NAME} for dustbins
    #   R_{LOCATION DESC} for rooms approximated as one dustbin
    #   LIFT_{LOCATION}   for lift location
def query_startpoints(curr_graph):
    confirmation = ['y','Y','1','continue']
    while True:
        #check if 
        startpoint=input('\n------------------------------------------------------------------------------\
                         \nWhere would you like to begin? Please select from the following options:\n{}\n\
                         \nYou can copy and paste from the selection above using ctrl+c and ctrl+v!\n\nChoice: '.format(startpoints(curr_graph)))
        #limit options
        nodes = curr_graph.return_allnodes()       
        
        if startpoint in nodes:
            confirm=input('Start from {}? y/n\n'.format(startpoint))
            if confirm in confirmation:
                #return curr_graph.greedy_circuit(startpoint)3
                print("Floyd Warshall solution - shows every paths and distances:\n",curr_graph.floyd_warshall())
                print("-------------------")
                print("Dijkstra solution - shows shortest path from starting point:\n",curr_graph.pathfind_dijkstra(startpoint))
                print("-------------------")
                return curr_graph.greedy_circuit(startpoint)
            else:
                print('Please select a new startpoint.')
                continue
        else:
            print('Invalid input, please try again.')
            continue


def welcome_message():
    print('Welcome! Follow the instructions to obtain the path you need')
    #to make some intro message and how to use the software
    graphid = output_buildingdecision_query_userinput()
    curr_graph = generate_Graph(graphid)
    query_startpoints(curr_graph)
    print('The ancient one goes back to sleep')

def main():
    welcome_message()
    cont_list=['y','Y','1','continue']
    stop_list=['n','N','0','stop']
    while True:
        cont = input("Calculation has been completed! Continue?\ny - to choose another location\nn - to exit\ny/n: \n")
        try: 
            if cont in cont_list:
                print('Continuing!\n')
                clear = "\n"*100
                print(clear)
                welcome_message()
                
                    
            elif cont in stop_list:
                print('Stopping!\n')
                return
            else:
                raise ValueError
        except ValueError:
            print("Invalid Input! Try again :(")
            continue
    
    

if __name__ == "__main__":
    start=time.process_time()
    main()
    print(time.process_time()-start)

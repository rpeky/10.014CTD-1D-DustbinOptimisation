import time
import User
import Graph
import Jsonstuff

# Object generation
# graph id format
def generate_Graph(graphid):
    g = Graph.Graph(graphid)
    return g

# def generate_person():
#     u = User.User()
#     u.printtest()
#     return u

#User input functions
#Terminal input output
def output_buildingdecision_query_userinput():
    #fill up with building numbers, decide what data type to put in
    buildings = ['Building 1', 'Building 2']
    print(buildings)
    
    #to tell user what inputs to put in, do a try/except to account for mis-input
    #maybe simplify the options down to 1 for building 1, 2 for building 2 or something
    choice = input('Enter Building choice: ')
    
    #post process input choice to our decision format likely something B{}_ , return to be concatenated with floor
    choice_processed = 'B{}_'.format(choice)
    
    return output_listoffloorplans_query_userinput(choice_processed)

def output_listoffloorplans_query_userinput(building_choice):
    #to fill in with building floors
    dd_buildingfloors = []
    for i in range(2,8):
        dd_buildingfloors.append(i)
    print(dd_buildingfloors)
    
    #to tell user what inputs to put in, do a try/except to account for mis-input
    choice = input('Enter floor choice: ')


    #post process input choice to our decision format likely something F{}_ then concatenate with building choice
    #final form should be B{}_F{}_
    choice_processed = building_choice+'F{}_'.format(choice)
    return choice_processed

#if graph exists
#write a function to display the possible points from the graph dictionary (can use the return startpoint fn in graph.py)
def startpoints():
    lift_start=curr_graph.return_startpoints()
    misc_start=curr_graph.return_allnodes()
    for node in misc_start:
        if node in lift_start:
            misc_start.remove(node)
    return 'Lifts:{}\nBins:{}'.format(lift_start,misc_start)
    


#write a function to use the above function's list of points to query starting point from user
    #   floorplan naming convention
    #   D_{LOCATION NAME} for dustbins
    #   R_{LOCATION DESC} for rooms approximated as one dustbin
    #   LIFT_{LOCATION}   for lift location
def query_startpoints():
    while True:
        startpoint=input('Where would you like to begin? Please select from the following options:\n{}'.format(startpoints()))
        if startpoint in curr_graph.return_allnodes():
            confirm=input('Start from {}? y/n'.format(startpoint))
            if confirm=='y':
                return curr_graph.greedy_circuit(startpoint)
            else:
                print('Please select a new startpoint.')
                continue
        else:
            print('Invalid input, please try again.')
            continue


def welcome_message():
    print('test welcome message')
    #to make some intro message and how to use the software
    graphid = output_buildingdecision_query_userinput()
    curr_graph = generate_Graph(graphid)
    print(curr_graph.pathfind_dijkstra("D_LIBRARY"))

    #user = generate_person()
    print('welcomed')
    



def main():
    welcome_message()
    # Jsonstuff.check_filefolderexist()
    # Jsonstuff.check_floorplan_exist('aaab')
    # g=Graph.Graph('test')
    # l2=g.return_allnodes()
    # print('list of all nodes: \n{}'.format(l2))
    # l3=g.return_startpoints()
    # print('list of all startpoints: \n{}'.format(l3))
    # g.add_neighbour('D_PANTRY')
    # l2=g.return_allnodes()
    # print('list of all nodes: \n{}'.format(l2))
    # g.add_visit('D_PANTRY')
    # g.add_visit('D_PANTRY')
    # print(g.dd_graph)
    
    

if __name__ == "__main__":
    start=time.process_time()
    main()
    print(time.process_time()-start)

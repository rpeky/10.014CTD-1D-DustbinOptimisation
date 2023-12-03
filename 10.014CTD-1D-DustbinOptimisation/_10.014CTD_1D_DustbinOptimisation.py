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
    while True:
        buildings = ['1', '2', '3', '5']
        b_choice = input('Buildings: 1, 2, 3, 5. Enter building choice:')
        if b_choice in buildings:
            print('Selected building: Building {}'.format(b_choice))
            return output_listoffloorplans_query_userinput(b_choice)
        else:
            print ('Enter a valid building number (1, 2, 3, 5).')    

def output_listoffloorplans_query_userinput(b_choice):
    while True:
        f_choice = input('Enter floor choice:')
        if f_choice.isnumeric():
            try:
                return output_listoffloorplans_query_userinput(b_choice,f_choice)
            except KeyError:
                print ('Enter a floor number from 2 to 7.')
        else:
            print('Enter a valid integer.')
            
def output_listoffloorplans_query_userinput(b_choice,f_choice):
    choice_processed = "B" + b_choice + "F" + f_choice
    c_processed = "Building " + b_choice + " Level " + f_choice
    print('Chosen Floor: ' + c_processed + ". Enter 'Yes' to confirm, N to exit.")
    if input('Confirm?') == 'Yes':
        return choice_processed
    else:
        return output_buildingdecision_query_userinput(building_choice)



#write a function to display the possible points from the graph dictionary (can use the return startpoint fn in graph.py)
def startpoints():
    pass


#write a function to use the above function's list of points to query starting point from user
    #   floorplan naming convention
    #   D_{LOCATION NAME} for dustbins
    #   R_{LOCATION DESC} for rooms approximated as one dustbin
    #   LIFT_{LOCATION}   for lift location
def query_startpoints():
    pass

def welcome_message():
    print('test welcome message')
    #to make some intro message and how to use the software
    graphid = output_buildingdecision_query_userinput()
    curr_graph = generate_Graph(graphid)
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

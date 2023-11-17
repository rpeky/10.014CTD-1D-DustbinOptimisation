import time
import User
import Graph
import Jsonstuff

# Object generation
# graph id format
def generate_Graph(graphid):
    g = Graph.Graph()
    g.printtest()
    return g

def generate_person():
    u = User.User()
    u.printtest()
    return u

#User input functions
#Terminal input output
def output_buildingdecision_query_userinput():
    #fill up with building numbers, decide what data type to put in
    buildings = []
    print(buildings)
    
    #to tell user what inputs to put in, do a try/except to account for mis-input
    choice = input()
    
    #post process input choice to our decision format likely something B{}_ , return to be concatenated with floor
    choice_processed = None
    
    return output_listoffloorplans_query_userinput(choice_processed)

def output_listoffloorplans_query_userinput(building_choice):
    #to fill in with building floors
    dd_buildingfloors = []
    
    #to tell user what inputs to put in, do a try/except to account for mis-input
    choice = input()

    #post process input choice to our decision format likely something F{}_ then concatenate with building choice
    #final form should be B{}_F{}_
    choice_processed = None
    
    return choice_processed



def welcome_message():
    print('test welcome message')
    #to make some intro message and how to use the software
    graphid = output_listoffloorplans_query_userinput()
    curr_graph = generate_Graph(graphid)
    user = generate_person()
    print('welcomed')
    



def main():
    #welcome_message()
    Jsonstuff.check_filefolderexist()
    g=Graph.Graph('test')
    l2=g.return_allnodes()
    print('list of all nodes: \n{}'.format(l2))
    l3=g.return_startpoints()
    print('list of all startpoints: \n{}'.format(l3))
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

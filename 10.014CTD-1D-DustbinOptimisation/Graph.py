import Jsonstuff
import json
import os

class Graph():
    def __init__(self, graphid):
        
        #known attributes
        self.dd_graph=dict()
        self.g_id=graphid

        # validate needed folders exist for files
        Jsonstuff.check_filefolderexist()
        
        #check if graph has been created before, obtain fresh copy from master file
        if Jsonstuff.check_floorplan_exist(graphid):
            print('graph exist\n')
            self.dd_graph = Jsonstuff.extract_jsonfileasobj(graphid,0,0)
            print('current graph state: ')
            print(self.dd_graph)
            self.show_neighbour()
            self.add_visiteddictkey_setas0()
            print('\nStarting points:\n',self.return_startpoints())
            print('\nAll points:\n',self.return_allnodes())
            
        #generate if file does not exist
        else:
            print('graph no exist\n')
            self.generate_data_firsttimeuse(graphid)
            print(self.dd_graph)
            self.show_neighbour()
            self.add_visiteddictkey_setas0()

        print('Graph created')
        
    def __del__(self):
        self.save_graph(self.g_id)
        print('Job completed, saving and deleting graph')
        
    #save in master folder
    def generate_data_firsttimeuse(self, graphid):
        
        self.create_floorplan(graphid)
        
        makenewfilename = graphid+"_floorplan.json"
        cwd = os.getcwd()
        newdir = os.path.join(cwd, 'FloorPlan_data_Master')
        full_path = os.path.join(newdir, makenewfilename)
        
        with open(full_path, 'w') as outfile:
            json.dump(self.dd_graph, outfile, sort_keys=False, indent=4, ensure_ascii=False) 
    

    #   floorplan naming convention
    #   D_{LOCATION NAME} for dustbins
    #   R_{LOCATION DESC} for rooms approximated as one dustbin
    #   LIFT_{LOCATION}   for lift location
         
    def create_floorplan(self, graphid):
        print('Floor plan generation for {}'.format(graphid))
        cont_list=['y','Y','1','continue']
        stop_list=['n','N','0','stop']
        
        while True:
            #show current graph state, initial is empty dict
            print('----------------------------------------------------------------')
            print('Current graph state: ')
            print(self.dd_graph)
            print('----------------------------------------------------------------')

            #start of loop, decide whether to add a vertex
            while True:
                cont = input('Continue adding vertex (dustbin) to graph? y/n\n')
                try: 
                    if cont in cont_list:
                        print('Continuing!\nEntering graph building tool')
                        break
                    
                    elif cont in stop_list:
                        print('Stopping!\nExiting graph building tool')
                        return
                    
                    else:
                        raise ValueError
                    
                except ValueError:
                    print("Invalid Input! Try again :(")
                    continue
            
            #add a vertex
            vtx = ''
            while True:
                vtx = input('Enter vertex ID to add to graph: ')
                #double check if data entered is correct
                try:
                    doublecheck = input('Confirm data entry? y/n\n')
                    #if correct, add new vertex/node, escape query loop
                    if doublecheck in cont_list:
                        if vtx in self.dd_graph.keys():
                            break
                        self.dd_graph[vtx]=dict()
                        break
                    #if misinput, re try by repeating the loop
                    elif doublecheck in stop_list:
                        continue
                    #TO IMPROVE ON THIS CATCH
                    else:
                        raise ValueError
                    
                except ValueError:
                    print('Invalid input! Try again :(\n')
                    continue     
            
            #add adjacent neighbours to vertex
            self.add_neighbour(vtx)
            
 
    def add_neighbour(self,vtx):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Adjacent neighbour creation tool for {}'.format(vtx))
        cont_list=['y','Y','1','continue']
        stop_list=['n','N','0','stop']
        
        while True:
            cfm_msg=input('Confirm adding neighbours to {} y/n:\n'.format(vtx))
            try:
                if cfm_msg in cont_list:
                    #continue adding neighbour until negative input causes break
                    while True:
                        #show current graph state
                        print('****************************************************************')
                        print('Current graph state: ')
                        print(self.dd_graph)
                        print('****************************************************************')
                        
                        #query for adjacent node/dustbin
                        adj_vtx = input("Enter adjacent vertex ID to add: ")
                        while True:
                            adj_vtx_dist = input("Enter distance to adjacent vertex: ")
                            #check for distance value, convert to float if possible, if not int/float re enter
                            try:
                                #break if valid value
                                if isinstance(float(adj_vtx_dist),float):
                                    adj_vtx_dist=float(adj_vtx_dist)
                                    break
                                else:
                                    raise ValueError
                            except ValueError:
                                print('Invalid input not a number! Try again :(\n')
                                continue  
                            
                        #confirm adjacent node name is correct    
                        try:
                            doublecheck = input('Confirm data entry? y/n\n')
                            #if valid, update dictionary with new data
                            if doublecheck in cont_list:
                                self.dd_graph[vtx].update({adj_vtx:adj_vtx_dist})
                                #undirected graph, so we can add the opposite as well
                                if adj_vtx not in self.dd_graph.keys():
                                    self.dd_graph[adj_vtx]=dict()
                                self.dd_graph[adj_vtx].update({vtx:adj_vtx_dist})
                                print('Graph Updated')
                                print('0000000000000000000000000000000000000000000000000000000000000000')
                                print('Current graph state: ')
                                print(self.dd_graph)
                                print('0000000000000000000000000000000000000000000000000000000000000000')
                                break
                    
                            elif doublecheck in stop_list:
                                print('Re-enter data')
                                continue
                            else:
                                raise ValueError
                    
                        except ValueError:
                            print('Invalid input! Try again :(\n')
                            continue
                        
                #if no more neighbours needed, end function    
                elif cfm_msg in stop_list:
                    return
                
                #raise error if unexpected input
                else:
                    raise ValueError
                
            except ValueError:
                print('Invalid input! Try again :(\n')
                continue
    
    def add_visiteddictkey_setas0(self):
        for i in self.dd_graph:
            self.dd_graph[i]['VISITED']=0
  

    def show_neighbour(self):
        for i in self.dd_graph:
            print('start        end         distance')
            for j in self.dd_graph[i]:
                print('{}       {}      {}'.format(i,j,self.dd_graph[i][j]))      
            print('-------------------------------------')
            
    def add_visit(self,vtx):
        self.dd_graph[vtx]['VISITED']+=1
                                    
    def remove_vertex(self, vtx):
        self.dd_graph.pop(vtx)
                
    def remove_adjvtx(self, vtx, adjvtx):
        self.dd_graph[vtx].pop(adjvtx)
    
    #to define start points as lifts, return list of L_ vertex
    def return_startpoints(self):
        KEYWORD_STARTPOINT = 'LIFT_'
        startpoint_list=[]
        for i in self.dd_graph:
            if KEYWORD_STARTPOINT in i:
                startpoint_list.append(i)
        return startpoint_list
    
    def return_allnodes(self):
        node_list=list(self.dd_graph.keys())
        return node_list
    
    #save in working folder
    def save_graph(self,graphid):
        makenewfilename = graphid+"_floorplan.json"
        cwd = os.getcwd()
        newdir = os.path.join(cwd, 'FloorPlan_data_Working')
        full_path = os.path.join(newdir, makenewfilename)
        with open(full_path, 'w') as outfile:
            json.dump(self.dd_graph, outfile, sort_keys=False, indent=4, ensure_ascii=False) 
            
    def change_graph_useworkingdata(self):
        #make a list of displayable graphs/file names
        #make a selectable list in the display 1. B1_F1_floorplan.json
        #                                      2. B1_F2_floorplan.json etc
        #maybe try some kind of enumerate list after getting the file names then format the strings
        #take input 
        self.display_availiable_graphs()
        #some error checking - try except loop
        selection = input()
        #some confirmation message
        self.dd_graph = Jsonstuff.extract_jsonfileasobj(selection,1,1)
        #print some confirmation message
            
    def pathfind_dijkstra(self, startpoint):
        pass
    
    def pathfind_athome(self):
        pass

    def pathfind_dijkstra(self, startpoint):
        pass
    
    def pathfind_athome(self):
        pass
    
    def display_availiable_graphs(self):
        pass
    
    def change_graph(self):
        pass
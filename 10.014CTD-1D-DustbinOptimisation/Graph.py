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
            self.dd_graph = Jsonstuff.extract_jsonfileasobj(graphid,0,0)
            print('current graph state: ')
            print(self.dd_graph)
            self.show_neighbour()
            self.add_visiteddictkey_setas0()
            print(self.dd_graph)
            
        #generate if does not exist
        else:
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
    
    def create_floorplan(self, graphid):
        print('Floor plan generation for {}'.format(graphid))
        cont_list=['y','Y',1,'continue']
        stop_list=['n','N',0,'stop']
        
        while True:
            print('current graph state: ')
            print(self.dd_graph)

            while True:
                cont = input('Do you want to continue? y/n\n')
                try: 
                    if cont in cont_list:
                        print('Continuing!\n')
                        break
                    
                    elif cont in stop_list:
                        print('Stopping!\n')
                        return
                    
                    else:
                        raise ValueError
                    
                except ValueError:
                    print("Invalid Input! Try again :(")
                    continue
                
            vtx = ''
            
            while True:
                vtx = input('Enter vertex ID: ')
                try:
                    doublecheck = input('Confirm data entry? y/n\n')
                    if doublecheck in cont_list:
                        self.dd_graph[vtx]=dict()
                        break
                    elif doublecheck in stop_list:
                        print('Re-enter data')
                        continue
                    #TO IMPROVE ON THIS CATCH
                    else:
                        raise ValueError
                    
                except ValueError:
                    print('Invalid input! Try again :(\n')
                    continue     
            
            #add neighbours
            while True:
                adj_vtx = input("Enter adjacent vertex ID: ")
                while True:
                    adj_vtx_dist = input("Enter distance to adjacent vertex: ")
                    try:
                        if isinstance(float(adj_vtx_dist),float):
                            adj_vtx_dist=float(adj_vtx_dist)
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print('Invalid input not a number! Try again :(\n')
                        continue  
                        
                
                try:
                    doublecheck = input('Confirm data entry? y/n\n')
                    
                    if doublecheck in cont_list:
                        self.dd_graph[vtx].update({adj_vtx:adj_vtx_dist})
                        
                        
                        ct=False
                        while True:
                            more_neighbour = input('Add another neighbour? y/n\n')
                            try:
                                if more_neighbour in cont_list:
                                    ct=True
                                    print('current graph state:\n')
                                    print(self.dd_graph)
                                    break
                                elif more_neighbour in stop_list:
                                    break
                                else:
                                    raise ValueError
                            except ValueError:
                                print('Invalid input! Try again :(\n')
                                continue  
                            
                        if(ct):
                            continue
                        
                        break
                    
                    elif doublecheck in stop_list:
                        print('Re-enter data')
                        continue
                    else:
                        raise ValueError
                    
                except ValueError:
                    print('Invalid input! Try again :(\n')
                    continue
                
    def add_visiteddictkey_setas0(self):
        for i in self.dd_graph:
            self.dd_graph[i]['VISITED']=0
            print(self.dd_graph)
                
    def show_neighbour(self):
        for i in self.dd_graph:
            for j in self.dd_graph[i]:
                print(i,j,self.dd_graph[i][j])
                
    def add_neighbour(self,vtx):
        pass
                                    
    def remove_vertex(self, vtx):
        self.dd_graph.pop(vtx)
                
    def remove_adjvtx(self, vtx, adjvtx):
        self.dd_graph[vtx].pop(adjvtx)
    
    def return_startpoints(self):
        
        pass
    
    def return_allnodes(self):
        node_list=self.dd_graph.keys()
        return node_list
    
    #save in working folder
    def save_graph(self,graphid):
        
        makenewfilename = graphid+"_floorplan.json"
        cwd = os.getcwd()
        newdir = os.path.join(cwd, 'FloorPlan_data_Working')
        full_path = os.path.join(newdir, makenewfilename)
        with open(full_path, 'w') as outfile:
            json.dump(self.dd_graph, outfile, sort_keys=False, indent=4, ensure_ascii=False) 

    
    def printtest(self):
        print('printtest')
    
    
        


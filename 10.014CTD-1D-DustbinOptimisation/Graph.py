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
            print('\nAdjacent relationship: \n')
            self.show_neighbour()
            
            print('\nStarting points:\n',self.return_startpoints())
            print('\nAll points on graph:\n',self.return_allnodes())
            print('\nChanging Graph source to working set\n')
            self.change_graph_useworkingdata(graphid)
            self.add_visiteddictkey_setas0()
            print('\nChanged')
            
            #offer options
            
        #generate if file does not exist
        else:
            print('graph no exist :(\n')
            self.generate_data_firsttimeuse(graphid)
            print(self.dd_graph)
            self.show_neighbour()
            self.add_visiteddictkey_setas0()
            self.change_graph_useworkingdata(graphid)

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
            print('{:20s}{:18s}{:15s}'.format('Start', 'End', 'Distance'))
            for j in self.dd_graph[i]:
                print('{:20s}{:15s}{:10.1f}'.format(i,j,self.dd_graph[i][j]))      
            print('----------------------------------------------')
            
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
            
    #semi debug tool, currently used to swap from master copy to working copy to reduce chance of overwriting recorded floor data        
    def change_graph_useworkingdata(self, graphid):
        #make a list of displayable graphs/file names
        #make a selectable list in the display 1. B1_F1_floorplan.json
        #                                      2. B1_F2_floorplan.json etc
        #maybe try some kind of enumerate list after getting the file names then format the strings
        #take input 
        #some error checking - try except loop
        #selection = input()
        #some confirmation message
        self.dd_graph = Jsonstuff.extract_jsonfileasobj(graphid,1,1)
        #print some confirmation message

## path finding stuff
    def pathfind_dijkstra(self, startpoint):
        djk_dict = dict()
        # generate a dictinonary of distance values
        vtxs = set(self.dd_graph.keys())
        for vtx in vtxs:
            if (vtx == startpoint):
                djk_dict[vtx] = (0,[])
            else:
                djk_dict[vtx] = (float('inf'),[])
        # keep track of visited and unvisited vertices
        visited_vtxs = set()

        # Start pathfinding
        current_vtx = startpoint
        while True:
            # Mark current vertex as visited
            visited_vtxs.add(current_vtx)

            # Get list of adjacent vertices
            adj_vtxs = [i for i in self.dd_graph[current_vtx].keys() if i in vtxs]

            # Update distances of adjacent vertices
            for adj_vtx in adj_vtxs:
                old_dist = djk_dict[adj_vtx][0]
                old_path = djk_dict[adj_vtx][1]
                new_dist = djk_dict[current_vtx][0] + self.dd_graph[current_vtx][adj_vtx]
                new_path = djk_dict[current_vtx][1] + [current_vtx]
                if new_dist < old_dist:
                    djk_dict[adj_vtx] = (new_dist,new_path)

            # Unvisited vertex with minimum distance is visited next
            current_vtx = None
            current_vtx_dist = float('inf')
            for vtx, tuptup in djk_dict.items():
                if vtx not in visited_vtxs and tuptup[0] < current_vtx_dist:
                    current_vtx = vtx
                    current_vtx_dist = tuptup[0]
            if current_vtx == None:
                break

        return djk_dict
    
    #for unlimited space in rubbish cart, solutions = number of starting nodes, unlikely to have two destinations with the same distance
    #greedy solution involves taking the shortest distance to the next unvisited dustbin
    #debug - startpoint "LIFT_SERVICE"
    def greedy_circuit(self, startpoint):
        #since set maintains order, we create a set of the order to visit
        #sol={startpoint}
        
        #total number of dustbins on floor = total vertex - lifts, to check if solution is a hamitonian cycle
        start_point_lift=self.return_startpoints()
        set_maxvisits = len(self.return_allnodes()) - len(start_point_lift)
        
        curr_pos = startpoint
        tour = []
        self.dd_graph[curr_pos]["VISITED"]+=1 
        totaldist=0
        

        while True:
            dd_djksol = self.pathfind_dijkstra(curr_pos)
            #find neighbours, remove visited tracker from list since not a dustbin
            neigh_list = list(self.dd_graph[curr_pos])
            neigh_list = [i for i in neigh_list if i!="VISITED"]
            shortest_dist = float('inf')
            tovisit=None

            #greedy search for nearest unvisited dustbin
            for i in dd_djksol.keys():
                # print("###############")
                # print(dd_djksol)
                # print(i, dd_djksol[i][0], shortest_dist, self.dd_graph[i],i[:4])
                # print("dist check: ",dd_djksol[i][0]<shortest_dist)
                # print("check not visited",self.dd_graph[i]["VISITED"]==0)
                # print("check if is not lift",i[:4]!="LIFT")
                # print("check if is not curr position",i!=curr_pos)
                
                if dd_djksol[i][0]<shortest_dist and self.dd_graph[i]["VISITED"]==0 and i[:4]!="LIFT" and i!=curr_pos:
                    shortest_dist=dd_djksol[i][0]
                    tovisit=i
                # print(shortest_dist)
                # print(tovisit)
                    
            #add to tour
            if tovisit is not None:
                #print(tour)
                #self.dd_graph[tovisit]["VISITED"] += 1
                path_to_nearest = dd_djksol[tovisit][1]
                #print(path_to_nearest)
                #walk  of shame to revisit dustbins
                for visit in path_to_nearest:
                    self.dd_graph[visit]["VISITED"] += 1
                tour += path_to_nearest
                #print(tour)
                #sol.add(tovisit)
                curr_pos = tovisit
                totaldist += shortest_dist
                
            #if nothing else, path find to nearest lift
            else:
                #print("returning to lift")
                shortest_dist = float('inf')
                tovisit = None
                dd_djksol = self.pathfind_dijkstra(curr_pos)
                l_lift = self.return_startpoints()
    
                for i in l_lift:
                    # Update the conditions inside the loop
                    if dd_djksol[i][0] < shortest_dist:
                        shortest_dist = dd_djksol[i][0]
                        tovisit = i
    
                if tovisit is not None:
                    self.dd_graph[tovisit]["VISITED"] += 1
                    path_to_nearest = dd_djksol[tovisit][1] + [tovisit]
                    for visit in path_to_nearest:
                        self.dd_graph[visit]["VISITED"] += 1
                    tour += path_to_nearest
                    #sol.add(tovisit)
                    totaldist += shortest_dist    
                break        
                    
            
            #print(sol)        
            # print(dd_djksol)
            # print(neigh_list)
            # print(shortest_dist)
            # print(tovisit)
            # print(tour)
            
            
            
        #     print("____________")
            
        # print(len(tour))
        res = (tour, totaldist)
        print(res)
        return res

    def floyd_warshall(self):
        vtxs = set(self.dd_graph.keys())
        vtx_count = len(vtxs)
        num_to_vtx = {i: vtx for i, vtx in enumerate(vtxs)}
        vtx_to_num = {vtx: i for i, vtx in enumerate(vtxs)}

        # Construct adjacency matrix
        dist_matrix = [[float('inf') for j in range(vtx_count)] for i in range(vtx_count)]
        prev_matrix = [[None for j in range(vtx_count)] for i in range(vtx_count)]
        for vtx, info in self.dd_graph.items():
            vtx_num = vtx_to_num[vtx]
            for adj_vtx, dist in info.items():
                adj_vtx_num = vtx_to_num[adj_vtx]
                if adj_vtx in self.dd_graph:
                    dist_matrix[vtx_num][adj_vtx_num] = self.dd_graph[vtx][adj_vtx]
                    prev_matrix[vtx_num][adj_vtx_num] = vtx_num
            dist_matrix[vtx_num][vtx_num] = 0
            prev_matrix[vtx_num][vtx_num] = vtx_num

        # k is the intermediate node between i and j
        for k in range(vtx_count):
            for i in range(vtx_count):
                for j in range(vtx_count):
                    old_dist = dist_matrix[i][j]
                    new_dist = dist_matrix[i][k] + dist_matrix[k][j]
                    if old_dist > new_dist:
                        dist_matrix[i][j] = new_dist
                        prev_matrix[i][j] = prev_matrix[k][j]

                        # Convert matrix back into dict
        dist_dict = {}
        path_dict = {}
        for i, row in enumerate(dist_matrix):
            vtx = num_to_vtx[i]
            dist_dict[vtx] = {}
            path_dict[vtx] = {}
            for j, dist in enumerate(row):
                adj_vtx = num_to_vtx[j]
                dist_dict[vtx][adj_vtx] = dist
                if prev_matrix[i][j] == None:
                    path_dict[vtx][adj_vtx] = []
                else:
                    path_dict[vtx][adj_vtx] = [adj_vtx]
                    while i != j:
                        j = prev_matrix[i][j]
                        path_dict[vtx][adj_vtx] = [num_to_vtx[j]] + path_dict[vtx][adj_vtx]
        fw_dict = {
            'dist': dist_dict,
            'path': path_dict
        }
        return fw_dict

    def pathfind_travelling_salesman_problem(self, startpoint):
        fw_dict = self.floyd_warshall()
        min_dist_graph = fw_dict['dist']
        min_dist_paths = fw_dict['path']

        def tsp(start, vtxs):
            # base case
            if len(vtxs) == 1:
                vtx = vtxs.pop()
                dist = min_dist_graph[start][vtx]
                path = [start, vtx]
                return dist, path
            info = []
            for vtx in vtxs:
                old_dist, old_path = tsp(vtx, vtxs - {vtx})
                new_dist = old_dist + min_dist_graph[start][vtx]
                new_path = [start] + old_path
                info.append((new_dist, new_path))
            return min(info, key=lambda x: x[0])

        vtxs = set(min_dist_graph.keys()) - {startpoint}
        dist, path = tsp(startpoint, vtxs)
        path_with_subpaths = [((i, j), min_dist_paths[i][j][1:-1]) for i, j in zip(path, path[1:])]
        tsp_dict = {
            'dist': dist,
            'path': path_with_subpaths
        }
        return tsp_dict

    def display_availiable_graphs(self):
        pass
    
    def change_graph(self):
        pass
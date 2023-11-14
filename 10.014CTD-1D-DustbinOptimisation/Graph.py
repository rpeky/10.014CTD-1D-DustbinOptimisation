import Jsonstuff
import json
import os

class Graph():
    def __init__(self, graphid):
        
        #known attributes
        self.dd_graph=dict()

        # validate needed folders exist for files
        Jsonstuff.check_filefolderexist()
        
        #check if graph has been created before, obtain fresh copy from master file
        if Jsonstuff.check_floorplan_exist(graphid):
            self.dd_graph = Jsonstuff.extract_jsonfileasobj(graphid,0,0)
        #generate if does not exist
        else:
            self.generate_data_firsttimeuse(graphid)
            


        print('Graph created')
        
    def __del__(self):
        self.save_graph()
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
    
    def create_floorplan(self):
        print('Floor plan generation for {}')
        while True:
            pass
            
    
    
    def return_startpoints(self):
        pass
    
    
    #save in working folder
    def save_graph(self):
        
        return
    
    def printtest(self):
        print('printtest')
    
    
        


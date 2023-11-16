import json
import os


#checks if folders exist, edit as more files are needed

    # Json file naming convention ==> B{}_F{}_floorplan.json, fill {} with building and floor number

    # __ index __               __file name template__                      __folder name__             __additional comments__
    #      0                    _floorplan.json                             FloorPlan_data_Master       first generation template
    #      1                    _floorplan.json                             FloorPlan_data_Working      working copy to overwrite


def check_filefolderexist():
    listoffolders_toexist = ['FloorPlan_data_Master', 'FloorPlan_data_Working']

    for folder in listoffolders_toexist:
        if not os.path.isdir(folder):
            print('making folder: {}'.format(folder))
            os.mkdir(folder)
        else:
            print('folder: {} exists'.format(folder))


def check_floorplan_exist(graphid):
    filename = str(graphid)+'_floorplan.json'
    cwd = os.getcwd()
    newdir = os.path.join(cwd, 'FloorPlan_data_Master')
    full_path = os.path.join(newdir, filename)
    return os.path.isfile(full_path)



def extract_jsonfileasobj(identifier, indextoload_suffix, indextoload_folder):
    filesuffix = [
        '_floorplan.json',
        '_floorplan.json'
        ]

    listoffolders_toexist = [
        'FloorPlan_data_Master', 
        'FloorPlan_data_Working'
        ]
    
    filename = str(identifier) + str(filesuffix[indextoload_suffix])
    cwd = os.getcwd()
    newdir = os.path.join(cwd, listoffolders_toexist[indextoload_folder])
    full_path = os.path.join(newdir, filename)
    f = open(full_path)
    return json.load(f)





#! /usr/bin/python
import os
import errno


def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
            
            
def compose_path(base, folder_name):
	return base +"/" + folder_name            

def make_main(folder, projectName):
	mainFile = folder + "/" + projectName + ".cpp"
	out_file = open(mainFile,"w")
	out_file.write("""
#include <iostream>
	
using namespace std;

int main (int argc, char*argv[]){
	return 0;
}
""")
	out_file.close()

def create_meta(root_folder, project_name):
	meta_info = '''
{
    "NAME" : "''' + project_name + '''",
    "VERSION" : "0.0.0",
    
    "DEPENDENCIES" : [
    ],
    
    "__BOX_INSTRUCTIONS__" : [
                                {   "FROM" : "include",
                                    "TO"   : "include",
                                    "FILTER" : "*"
                                }    
    ],
    "__UNBOX_INSTRUCTIONS__" : [
                                {   "FROM" : "include",
                                    "TO"   : "include-ext/''' + project_name + '''",
                                    "FILTER" : "*"
                                }    
    ]
        
    
}
'''
	with open(compose_path(root_folder, "meta.json"), "w" ) as f:
		f.write(meta_info)


            
if __name__ == "__main__":
	prjname = raw_input("project name: ")
	
	#determining project folder
	prjPath = os.getcwd() +"/"+ prjname
	prjDoc = compose_path(prjPath, "doc")
	prjSrcBase = compose_path(prjPath, "source")
	prjHeader = compose_path(prjPath, "include")
	prjHeaderEx= compose_path(prjPath, "include-ext")
		
	try:
		print "creating project folder at:", prjPath
		make_sure_path_exists(prjPath)
		print "DONE"
		
		print "creating project documentation folder at:", prjDoc
		make_sure_path_exists(prjDoc)
		print "DONE"
		
		print "creating project source folder at:"
		print prjSrcBase
		make_sure_path_exists(prjSrcBase)
		print "DONE"
		
	
		print prjHeader
		make_sure_path_exists(prjHeader)
		print "DONE"

		print prjHeader
		make_sure_path_exists(prjHeaderEx)
		print "DONE"

	except OSError as exception:	
		print "FAIL"
		
	
	make_main(prjSrcBase, prjname)
	create_meta(prjPath, prjname)	
		

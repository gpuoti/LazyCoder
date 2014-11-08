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


def make_gradle(folder, projectName):
	build = folder + "/build.gradle"
	f = open(build, "w")
	f.write ("""apply plugin: 'cpp'

executables {
	""")
	
	f.write(projectName)
	f.write("""
}

sources {
	""")
	f.write(projectName)
	f.write("""{
			
	}	
}	""")
	
	f.close


            
if __name__ == "__main__":
	prjname = raw_input("project name: ")
	
	#determining project folder
	prjPath = os.getcwd() +"/"+ prjname
	prjDoc = compose_path(prjPath, "doc")
	prjSrcBase = compose_path(prjPath, "src")
	prjSrc = compose_path(prjSrcBase, prjname)
	prjCpp = compose_path(prjSrc, "cpp")
	prjHeader = compose_path(prjSrc, "header")
		
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
		
		print prjSrc
		make_sure_path_exists(prjSrc)
		print "DONE"
		
		print prjCpp
		make_sure_path_exists(prjCpp)
		print "DONE"
				
		print prjHeader
		make_sure_path_exists(prjHeader)
		print "DONE"

	except OSError as exception:	
		print "FAIL"
		
	
	make_main(prjCpp, prjname)
	make_gradle(prjPath, prjname)
		
		

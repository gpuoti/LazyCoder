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
	pch_name = projectName + '_pch.h'
	mainFile = folder + "/" + projectName + ".cpp"
	out_file = open(mainFile,"w")
	out_file.write('''
#include "''' + pch_name + '''"
#include <iostream>
	
using namespace std;

int main (int argc, char*argv[]){
	return 0;
}
''')
	out_file.close()

def make_pch_support_files(folder, project_name):
	pch_name = project_name + '_pch'
	decl_file = folder + "/" + pch_name + ".h"
	def_file = folder + "/" + pch_name + ".cpp"

	with open(decl_file, 'w') as f:
		f.write('''
#pragma once

#include <stdio.h>
#include <tchar.h>
''')

	with open(def_file, 'w') as f:
		f.write('#include "'+ pch_name + '.h"')

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
	make_pch_support_files(prjPath, prjname)
		

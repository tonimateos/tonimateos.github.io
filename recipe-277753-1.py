#!/usr/bin/python2

def searchreplace(path,search,replace,exts=None):

    import fileinput, glob, string, sys, os
    from os.path import join
    #r replace a string in multiple files
    #filesearch.py

    print "HOOOLA"
    files = glob.glob(path + "/*")
    if files is not []:
        for file in files:
            if os.path.isfile(file):
                if exts is None or exts.count(os.path.splitext(file)[1]) is not 0:
                    for line in fileinput.input(file, inplace=1):
                        line = line.replace(search,replace)
                        sys.stdout.write(line)

#searchreplace("maldives/","index.html","index.shtml")
#searchreplace("maldives/images/","index.html","index.shtml")
#searchreplace("maldives/thumnails/","index.html","index.shtml")
searchreplace("worship","Art.html","worship.shtml")
searchreplace("worship/Gods","Art.html","worship.shtml")
searchreplace("worship/Gods/images","Art.html","worship.shtml")
searchreplace("worship/Gods/thumbnails","Art.html","worship.shtml")


def fullpath():
    # finding the path
    print 'sys.argv[0] = ', sys.argv[0]
    pathname = os.path.dirname(sys.argv[0])
    print 'path = ', pathname
    print 'full path = ', os.path.abspath(pathname)
    
if __name__ == "__main__":
    import sys, os
    fullpath()
    
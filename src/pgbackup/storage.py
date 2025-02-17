def local(infile,out):
    outfile.write(infile.read())
    outfile.close()
    infile.close()
# -*- coding: UTF-8 -*-
f = open("orgs.txt", "r")
for x in f:
  outfile = (str(x).replace(" ","").replace(",","").replace("-","").replace(".","").replace("/","").replace("°",""))
  outfile = outfile.strip()
  print ("include::participanting-organizations/"+outfile+".adoc[]")
  print ("")

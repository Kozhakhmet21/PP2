import re
a='TheSpain'
x=re.search("The.+Spain$",a) # + degen isdegen elementterdyn arasynda hotya bir element bolu kerek.
if x:
    print("Yes")
else:
    print("No")
print(x)
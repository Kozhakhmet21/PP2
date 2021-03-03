import csv
with open("emp1.csv",mode='w') as emp_file:
    emp_wr=csv.writer(emp_file,quotechar='"',quoting=csv.QUOTE_MINIMAL)
    emp_wr.writerow(["Kozhakhmet","KBTU","December"])
    emp_wr.writerow(["Nursultan","Qonaev","October"])
    emp_wr.writerow(["Nazerke","MUA","April"])
    emp_wr.writerow(["Daulet","Qorqyt","November"])

    #csv file retynde oqu ushin ony .csv dep songysyn qaldyru kerek, ol onsyz csv file retynde oqymaidy.
    #Bul kezde delimiter="," degen kerek emes, onsyz gana jumys jasaidy.
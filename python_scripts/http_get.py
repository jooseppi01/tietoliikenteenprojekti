import pandas as pd

df = pd.read_csv('http://172.20.241.9/luedataa_kannasta_groupid_csv.php?groupid=61',        
                 delimiter = ';',
                 header = None,
                 names = ['number', 'timestamp', 'groupid', 'from_mac', 'to_mac', 'x', 'y', 'z', 'a', 'b', 'c'])        #Nimetään kolumnit.
                 
df.to_csv(r'C:\Users\Joona\Desktop\file3.csv')      #Tallennetaan tiedosto csv:nä.



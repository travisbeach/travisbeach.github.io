import csv


with open('2000.csv', 'rb') as data:
    reader = list(csv.reader(data, delimiter = ','))

    for row in reader:
    	# 1 New York City: JFK / LGA / EWR
    	if row[4]=="JFK" or row[4]=="LGA" or row[4]=="EWR":
    		row[4]="NYC"
    	if row[6]=="JFK" or row[6]=="LGA" or row[6]=="EWR":
    		row[6]="NYC"

    	# 2 Los Angeles: LAX / SNA / BUR
    	if row[4]=="LAX" or row[4]=="SNA" or row[4]=="BUR":
    		row[4]="LAX"
    	if row[6]=="LAX" or row[6]=="SNA" or row[6]=="BUR":
    		row[6]="LAX"
    	
    	# 3 Chicago: ORD / MDW
    	if row[4]=="ORD" or row[4]=="MDW":
    		row[4]="CHI"
    	if row[6]=="ORD" or row[6]=="MDW":
    		row[6]="CHI"

    	# 4 Dallas: DFW / DAL
    	if row[4]=="DFW" or row[4]=="DAL":
    		row[4]="DAL"
    	if row[6]=="DFW" or row[6]=="DAL":
    		row[6]="DAL"

    	# 5 Houston: IAH / HOU
    	if row[4]=="IAH" or row[4]=="HOU":
    		row[4]="HOU"
    	if row[6]=="IAH" or row[6]=="HOU":
    		row[6]="HOU"

    	# 6 Philadelphia: PHL
    	# 7 Washington DC: IAD / DCA
    	if row[4]=="IAD" or row[4]=="DCA":
    		row[4]="WAS"
    	if row[6]=="IAD" or row[6]=="DCA":
    		row[6]="WAS"

    	# 8 Miami: MIA / FLL / PBI
    	if row[4]=="MIA" or row[4]=="FLL" or row[4]=="PBI":
    		row[4]="MIA"
    	if row[6]=="MIA" or row[6]=="FLL" or row[6]=="PBI":
    		row[6]="MIA"

    	# 9 Atlanta: ATL
    	# 10 Boston: BOS
    	# 11 San Francisco: SFO / OAK
    	if row[4]=="SFO" or row[4]=="OAK":
    		row[4]="SFO"
    	if row[6]=="SFO" or row[6]=="OAK":
    		row[6]="SFO"

    	# 12 Phoenix: PHX
    	# 13 Riverside: ONT
    	# 14 Detroit: DFW
    	# 15 Seattle: SEA
    	# 16 Minneapolis: MSP
    	# 17 San Diego: SAN
    	# 18 Tampa: TPA
    	# 19 St. Louis: STL
    	# 20 Baltimore: BWI
    	# 21 Denver: DEN
    	# 22 Charlotte: CLT
    	# 23 Pittsburgh: PIT
    	# 24 Portlantd: PDX
    	# 25 San Antonio: SAT
    	# 26 Orlando: MCO
    	# 27 Sacramento: SMF
    	# 28 Cincinnati: CVG
    	# 29 Kansas City: MCI
    	# 30 Las Vegas: LAS
    	# 31 Cleveland: CLE
    	# 32 Columbus: CMH
    	# 33 Indianapolis: IND
    	# 34 San Jose: SJC
    	# 35 Austin: AUS
    	# 36 Nashville: BNA
    	# 37 Virginia Beach: ORF
    	# 38 Providence: PVD
    	# 39 Milwaukee: MKE
    	# 40 Jacksonville: JAX
    	# 41 Memphis: MEM
    	# 42 Oklahoma City: OKC
    	# 43 Louisville: SDF
    	# 44 Richmond: RIC
    	# 45 New Orleans: MSY
    	# 46 Raleigh: RDU
    	# 47 Hartford: BDL
    	# 48 Salt Lake City: SLC
    	# 49 Birmingham: BHM
    	# 50 Buffalo: BUF

    city_list = ["NYC", "LAX", "CHI", "DAL", "HOU", "PHL", "WAS", "MIA", "ATL", "BOS",
    			 "SFO", "PHX", "ONT", "DTW", "SEA", "MSP", "SAN", "TPA", "STL", "BWI",
    			 "DEN", "CLT", "PIT", "PDX", "SAT", "MCO", "SMF", "CVG", "MCI", "LAS", 
    			 "CLE", "CMH", "IND", "SJC", "AUS", "BNA", "ORF", "PVD", "MKE", "JAX",
    			 "MEM", "OKC", "SDF", "RIC", "MSY", "RDU", "BDL", "SLC", "BHM", "BUF"]

    with open ('2000citypair.csv', 'wb') as citypair:
		c = csv.writer(citypair, delimiter=',')
   		
   		for i in city_list:
   			lst = []
   			for j in city_list:
   				if i==j:
   					lst.append("/")
   				else:
		   			pair_sum = 0
		   			for row in reader:
		   				if row[4]== i and row[6]==j:
		   					pair_sum += int(float(row[0]))
		   				elif row[6]==i and row[4]==j:
		   					pair_sum += int(float(row[0]))
		   			if pair_sum > 12000:
						lst.append(pair_sum)
					else:
						lst.append(0)
			c.writerow(lst)


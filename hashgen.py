# #!/usr/local/bin/python3
# hashgen.py
# Dave Grainger / @elusivepeak January 2017
# Generates sample S3 object keys for dataset names in the S3 in-bucket
# 
# /[hash]/[origin class]-[origin id]/[year]-[month]-[day]-[hour]-[minute]/[dataset name]{.[start]}{-[extent}}
#
# hash is a random 4 digit hex number
# origin class is a single character identifying type of source
# 	s means sql
# origin is a dotted hierarchical name describing the datasource
# y,m,d,h,m are UTC time the representations extracted (or else time of extract) 
#
# Example for a sql origin type (c.f. DataVault)
# 	MyXero.dbo.Organisation   (database.schema.collection)
#

import random    	# for randint() function
import datetime		# for 'now'

# invent some sample sql origin datasources and dataset names
sqlorigins = {'MyXero.dbo.Organisation': 'SubscribedOrgs', 
				'MyXero.dbo.OrganisationDescription': 'OrganisationDetail',
				'Shard.dbo.Shardmonkey': 'OrgsByShard',
				'Payroll.dbo.Salary':'SalariedEmployees' ,
				'Payroll.dbo.AntonysSalary':'UnderpaidEmployees' }

# generate a few sample dataset names
for sample in sqlorigins:
	oclass='s'
	
	rand = random.randint(1,2**16)		# generate a 16-bit random integer

	et = datetime.datetime.now()		# take now as time of dataset extract
	edt = str(f'{et.year}-{et.month}-{et.day}-{et.hour}-{et.minute}')

	print(f'/{rand:04x}/{oclass}/{sample}/{edt}/{sqlorigins[sample]}.1-100000')

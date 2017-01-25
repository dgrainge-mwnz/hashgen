# #!/usr/local/bin/python3
# hashgen.py
# Dave Grainger / @elusivepeak January 2017
# Generates sample S3 object keys for dataset names in the S3 in-bucket
# 
# /[4 digit hash]/[origin type]-[origin id]/[year]-[month]-[day]-[hour]-[minute]/[dataset name]{.[start]}{-[extent}}
#
# origin is a dotted hierarchical name describing the datasource
#
# Example for a sql origin type (c.f. DataVault)
# 	MyXero.dbo.Organisation   (database.schema.collection)

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
	origintype='sql'
	
	rand = random.randint(1,2**16)		# generate a 16-bit random integer

	et = datetime.datetime.now()		# take now as time of dataset extract
	edt = str(f'{et.year}-{et.month}-{et.day}-{et.hour}-{et.minute}')

	print(f'/{rand:04x}/sql/{sample}/{edt}/{sqlorigins[sample]}.1-10000')

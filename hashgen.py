
#
# dataset origin name is a 4 dotted word name
#	type.source.schema.collection
#
# Example for a relational source (c.f. DataVault)
# 	relational.MyXero.dbo.Organisation
#
# Example for unstructured sources
# 	unstructured.sumo.p_users2.accesslogs
# 	unstructured.datadog.stream7.objectclassX
#
# Define "LAKE EPOCH" as 01/01/2017
# Calculate N the number of days since LAKE EPOCH that the extract dataset was produced
# Calculate the hash of <originname> + str(N)  e.g. today "MyXero.dbo.Organisation24"
# Truncate the hash to the right 2 bytes / 16 bits / 4 hex digits HHHH
# Dataset filename format
# 	HHHH-NNNN-originsource.schema.table-BBB
# where HHHH is righthand 16 bits (4 hex digits) of the hash
# where NNNN is number of days since lake epoch
# where BBB is the batch number (allows a big dataset to be broken down into batches)

# python example for generating name of some relational-origin datasets

datasetorigins = [	'MyXero.dbo.Organisation', 
			'MyXero.dbo.OrganisationDescription',
			'Shard.dbo.Shardmonkey',
			'Payroll.dbo.Salary',
			'Payroll.dbo.AntonysSalary']

# iterate for a sample range of dates 180-200 since epoch
for i in range(180,200):
	for j in range(1,5):       		# iterate across five origin dataset names
		hhhh = hex( hash(datasetorigins[j] + str(i)) &0xFFFF)
		datasetname = hhhh + "-" + datasetorigins[j] + "-001"
		print "Days since epoch",i, "	Datasetname", datasetname
			 


import json
import re
import os.path
from optparse import OptionParser

usage = "usage: file_join.py [options] arg1 arg2"
parser = OptionParser(usage=usage)
parser.add_option("-g", "--groupFile", dest="file1", default='/etc/group',
                  help="read file containing groups")
parser.add_option("-p", "--passwdFile", dest="file2", default='/etc/passwd',
                  help="read file containing password")

(options, args) = parser.parse_args()

if not os.path.isfile(options.file1):
	parser.error("options -fg is not a file.")

if not os.path.isfile(options.file2):
	parser.error("options -fp is not a file.")


file1 = options.file1
file2 = options.file2

groupfile = {}
pwdfile = {}


#read group file and split it into dictionary
with open(file1) as f:
	for line in f.read().splitlines():
		pattern = re.compile(".+:*:*:")
		if not pattern.match(line):
			continue

		#{groupID: groupList}
		groupfile[line.split(':')[2]]=line.split(':')[3].split(',')


#read password file and get uid, full_name, and groupID from it
with open(file2) as f:
	for line in f.readlines():
		pattern = re.compile(".+:*:*:*:*:")
		if not pattern.match(line):
			continue
		pwdtmp={}
		pwdtmp['uid']=line.split(':')[2]
		pwdtmp['full_name']=line.split(':')[4]
		pwdtmp['groupID']=line.split(':')[3]
		pwdfile[line.split(':')[0]]=pwdtmp


# get groupList from group file dictionary by joining using groupID. Remove groupID afterwards. 
for key in pwdfile.keys():
	pwdfile[key]['groups']=groupfile.get(pwdfile[key]['groupID'],"")
	pwdfile[key].pop('groupID')

#print json file
with open('result.json','w') as f:
	json.dump(pwdfile,f)





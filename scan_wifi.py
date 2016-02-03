#!/usr/bin/python2
#-*-coding: UTF-8 -*-
import subprocess
import time
def main():
	print "Hello Word"
	Scan =  subprocess.check_output(['iwinfo','apcli0','scan'])
	Scans = Scan.split('\n')
	for i in range(len(Scans)):
		Scans[i] = Scans[i].strip(' ')
	#print Scans

	print len(Scans)
	all = len(Scans)/6
	ap={}
	a = Scans[0]
	#print a[a.find(':'):]
	j = 0
	for i in range(0, len(Scans)-6, 6):
		ESSID = Scans[i+1] 
		Encryption =Scans[i+4]	
		ap.update( {j: {"ESSID": ESSID[8 :-1],"Encryption": Encryption[12 :]} } )
		j= j+1
	#print ap
	for i in ap:
		print str(i)+" "+ap[i]["ESSID"]+"  "+ap[i]["Encryption"]
	select = int(raw_input('number: '))
	key = raw_input('password :')
	subprocess.call(["uci","set","wireless.sta.ssid="+ap[select]["ESSID"] ])	
	subprocess.call(["uci","set","wireless.sta.key="+str(key) ])
	type=""
	if ap[select]["Encryption"].find("WPA2"):
		type="psk2"
	elif ap[select]["Encryption"].find("WPA"):
		type="psk"	
	if type!="":
		c = subprocess.check_output(["uci","set","wireless.sta.encryption="+type ])
		time.sleep(1)
		print c
if __name__=='__main__':
	main()

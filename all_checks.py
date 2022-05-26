#!/usr/bin/env python3
import sys
import os

def check_reboot():
	'''returns true if the computer has a pending reboot'''
	return os.path.exists("/run/reboot-required")

def main():
	if check_reboot():
		print("Pending Reboot.")
		sys.exit(1)
	if disk_check():
		print("Disk is full")
		sys.exit(1)
	print("everything ok")
	sys.exit(0)

main()

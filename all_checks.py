#!/usr/bin/env python3
import sys

def check_reboot():
	'''returns true if the computer has a pending reboot'''
	return os.path.exist("/run/reboot-required")

def main():
	if check_reboot():
		print("Pending Reboot.")
		sys.exit(1)
	print("everything ok")
	sys.exit(0)

main()

import socket
import os
import netifaces as nf
import re


def get_network():
	a = {}
	IP = nf.ifaddresses('wlo1')[2][0]['addr']
	default_gateway = nf.gateways()["default"][2][0]
	a["IP"] = IP
	a["Gateway"] = default_gateway

	MAC =  nf.ifaddresses('wlo1')[17][0]['addr']
	a["MAC"] = MAC

	mask = nf.ifaddresses('wlo1')[2][0]['netmask']
	a["MASK"] = mask

	broadcast = nf.ifaddresses('wlo1')[2][0]['broadcast']
	a["Broadcast"] = broadcast

	details = os.popen("ifconfig").read().split("MTU")
	end_index = details[-1].find(" ")
	mtu = details[-1][1:end_index]
	a["MTU"] = mtu

	name = nf.interfaces()[-1]
	a["Name"] = name

	ipconfig_cmd = os.popen("ifconfig").read()
	b = ipconfig_cmd.split("\n\n")

	a["Type"] = re.search("Link encap:(\w+)", b[-2]).group(1)


	return a
	
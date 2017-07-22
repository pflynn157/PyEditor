#!/usr/bin/python3
from os import getenv
from os.path import exists
from gen_settings import generate_settings
from xml_parser import XmlParser
import platform

class Settings():
	settingsPath = str("")
	parser = 0
	
	def winPath(self):
		path = str(getenv("USERPROFILE"))
		path+=str("\.py-editor\settings.xml")
		
	def unixPath(self):
		path = str(getenv("HOME"))
		path+=str("/.py-editor/settings.xml")
	
	def __init__(self):
		path = str("")
		if (platform.system()=="Windows"):
			path = self.winPath()
		else:
			path = self.unixPath()
		self.settingsPath = path
		if (exists(path)==False):
			generate_settings()
		self.parser = XmlParser(path)
			
	def getSetting(self, ID, defaultSetting):
		setting = str("")
		try:
			setting = self.parser.getElementData(ID)
		except Exception:
			setting = defaultSetting
		return setting
		
	def getAttributeSetting(self, ID, attrID, defaultSetting):
		setting = str("")
		try:
			setting = self.parser.getElementAttribute(ID,attrID)
		except Exception:
			setting = defaultSetting
		if (setting==None):
			setting = defaultSetting
		return setting
		
	def writeSetting(self,ID,value):
		self.parser.setElementValue(ID,value)
		
	def writeAttributeSetting(self,ID,attr,attrValue):
		self.parser.setElementAttribute(ID,attr,attrValue)

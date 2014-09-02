#coding:utf-8

import re

def ProcessMail(inputMail):
	isMatch = bool(re.match(r"^[a-zA-Z](([a-zA-Z0-9]*\.[a-zA-Z0-9]*)|[a-zA-Z0-9]*)[a-zA-Z]@([a-z0-9A-Z]+\.)+[a-zA-Z]{2,}$", inputMail,re.VERBOSE));
	return isMatch 
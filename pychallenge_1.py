#! /usr/bin/env python
# python challenge level1
from string import lowercase, maketrans
oldstr = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
alph_map = maketrans(lowercase, lowercase[2:]+lowercase[:2])  
print oldstr.translate(alph_map)
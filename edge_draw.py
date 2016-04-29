"""
values represent:
0=free path
1=blocked path
3=valid path
4=invalid path
5=goal
"""

mapp = [[]]

def first_look(cx, cy):
	global mapp
        rows = len(mapp)
        columns = len(mapp[0])
	if (not((cx < rows and cx >= 0) and (cy < columns and cy >= 0))):
		return False
	if (mapp[cx][cy]==5):
		return True
	if (mapp[cx][cy]!=0):
		return False
	mapp[cx][cy] = 3
	if (first_look(cx-1,cy) == True):
		return True
	if (first_look(cx,cy+1) == True):
		return True
	if (first_look(cx+1,cy) == True):
		return True
	if (first_look(cx,cy-1) == True):
		return True
	mapp[cx][cy] = 0
	return False
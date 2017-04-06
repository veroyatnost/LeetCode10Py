#coding=utf-8

# Given a collection of intervals, merge all overlapping intervals.

# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].
def merge(vs):
  if vs==[]:
    return vs
  vs.sort(key=lambda x:x[0])
  new=[]
  for i in range(len(vs)-1):
    if vs[i][1]<vs[i+1][0]:
      new.append(vs[i])
    else:
      vs[i+1]=[vs[i][0],max(vs[i][1],vs[i+1][1])]
  new.append(vs[-1])
  return new

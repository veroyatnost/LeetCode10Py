#coding = utf-8

#Given an array of strings, group anagrams together.

#For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 

#Return:
#[
#["ate", "eat", "tea"],
#["nat", "tan"],
#["bat"]
#]

def groupAnagrams(S):
  result={}
  for s in S:
    k=list(s)
    k.sort()
    k=str(k)
    if k in result:
      result[k].append(s)
    else:
      result[k]=[s]
  return [result[k] for k in result.keys()]

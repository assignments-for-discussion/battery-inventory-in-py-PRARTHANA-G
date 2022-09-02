
def count_batteries_by_usage(cycles):
  #define variable for buckets
  lowCount = 0
  mediumCount= 0
  highCount = 0
  #divide cycles into the various buckets by incrementing the values when a certain range is matched
  for i in range(len(cycles)):
    if cycles[i]<400:
      lowCount = lowCount+1
    elif cycles[i]>=400 and cycles[i]<=919:
      
      mediumCount = mediumCount+1
    else: 
      highCount = highCount+1
      
  return {
    "lowCount": lowCount,
    "mediumCount": mediumCount,
    "highCount": highCount
  }

  

def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])#list
  
  #debugging technique
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()

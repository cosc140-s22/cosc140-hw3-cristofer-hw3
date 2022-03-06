#######################################################
#
# COSC 140 Homework 3: URL checker
#
#######################################################

def urlchecker(url):
  list = url.split("://")
  if "/" not in list[1]:
    return False
  if not url.startswith("http://") and not (url.startswith("https://")):
    return False
  if url.count("?") >1 or url.count("#")>1 :
    return False 
  if ' ' in url:
    return False
  if url.count("#")==1 and url.count("?")==1:
      if (url.find("#") > url.find("?")):
        return False
  restOfUrl= list[1]
  list2= restOfUrl.split("/")
  #print(list2)
  hostname=list2[0]
  #print(hostname)
  if hostname=="":# if hostname is empty 
    return False
  if ":" in list2[1]:
    remainder=list2[1]
    if remainder[-1]!= "/":
      return False
  if ":" in hostname:
    list3= hostname.split(":")
    #print(list3)
    if not list3[1].isdigit():
      return False
  return True 


def testurl():
    urls = [ # valid
      ['https://example.com/', True],
      ['http://example.com/', True],
      ['http://example.com/?query', True],
      ['http://example.com/#fragment', True],
      ['http://example/', True],
      ['http://example/path/', True],
      ['http://example/path', True],
      ['https://example.com:3000/path#fragment?query', True],
      ['https://example.com/path#fragment?query', True],
      # invalid
      ['htt://example/', False],
      ['httpss://example/', False],
      ['https://example/:3000', False],
      ['https://example/?:3000?', False],
      ['https://example/?:3000#', False],
      ['https://example/xy z', False],
      ['https://example/xyz:', False],
      ['https://example', False],
    ]
    for url,expected in urls:
        if urlchecker(url) != expected:
            print(f"{url} is not valid, but your function claimed the opposite")
        else:
            print(f"{url} - ok")
          

testurl()
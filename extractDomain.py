"""
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:
kz
domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"

"""

# my solution
def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]


# code wars solution
# def domain_name(url):
#     url = url.replace("www.", "")
#     url = url.replace("https://", "")
#     url = url.replace("http://", "")

#     return url[0 : url.find(".")]


print(domain_name("www.google.com"))
print(domain_name("http://google.co.jp"))
print(domain_name("http://leet.com/kata"))
print(domain_name("nk70h7j3nhayy2wyg5cnz3af7wdug.name/warez/"))
print(domain_name("https://leet-CODE.com"))
print(domain_name("http://www.nlljw7035l3pd7m1w851y.name/"))


# long solution using library
# from urllib.parse import urlparse
# def domain_name(url):
#     print(urlparse(url), "\n")
#     netloc = urlparse(url).netloc
#     path = urlparse(url).path
#     if path and netloc:
#         if "www" in netloc:
#             print(netloc.split(".")[1])
#         else:
#             print(netloc.split(".")[0])
#     elif netloc:
#         if "www" in netloc:
#             print(netloc.split(".")[1])
#         else:
#             print(netloc.split(".")[0])
#     else:
#         if "www" in path:
#             print(path.split(".")[1])
#         else:
#             print(path.split(".")[0])

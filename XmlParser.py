"""This program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the
comment counts from the XML data, compute the sum of the numbers in the file.
ACTUAL DATA : http://py4e-data.dr-chuck.net/comments_1189780.xml (Sum ends with 64) """


# importing necessary packages
import ssl
import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error


# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# Enter http://py4e-data.dr-chuck.net/comments_1189780.xml as URL
url = input("\nEnter URL : ")                               # prompts user for the URL on which scrapping is to be done

try:                                                        # try to open URL, parse XML, and fetch all NUMBER(s)
    data = urllib.request.urlopen(url, context=ctx).read()  # open the url (comprising of XML) // similar to open() in file-handling
    print("\nRetrieving :", url)                            # display the retrieved URL
    print("\nRetrieved :", len(data), "characters")         # display number of characters extracted
    
    tree = ET.fromstring(data)                              # fetch the parent node (COMMENTINFO) of COMMENTS
    lst = tree.findall("comments/comment")                  # within that parent node list all COMMENT tags
    # To make this code a little simpler, we can use an XPath selector string to look through
    # the entire tree of XML for any tag named 'count' with the following line of code:
    # lst = tree.findall('.//count') to find every count tag in the XML file
    # then write: num = int(item.text) instead of num = int(item.find("count").text) at line no. 39

except Exception as e:                                      # catch exception upon opening/parsing/fetching failure
    print(e)                                                # display error message
    quit()                                                  # quits the program execution

    
print("\nNumbers are :", end=" ")                           # display the fetched numbers
num_list = list()                                           # create an empty list to store the fetched numbers


for item in lst:                                            # traversing through the list of COMMENT tags
    try:                                                    # try to convert variables to integer // type-casting
        num = int(item.find("count").text)                  # (String)num is converted to (int)num
    except ValueError as e:                                  # catch exception upon type-casting failure
        print(e)                                            # display error message
        quit()                                              # quits the program execution

    num_list.append(num)                                    # add numbers to num_list one by one
    print(num, end=" ")                                     # display all numbers

    
# display the final result(s)
print("\n\nCount of numbers =", len(num_list))
print("\nSum of Numbers =", sum(num_list))
print("\nAverage of Numbers =", float(sum(num_list)/len(num_list)), "\n")

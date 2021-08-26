import requests

#filename.txt must cointain a url list 
f = open('filename.txt', 'r')
file_content = f.readlines()
PATH="C:\\"

for url in file_content:
    r = requests.get(url, stream=True)

    print('Beginning file download with urllib2...')
    filename = url.split("/")[-1].strip("\n")
    with open(PATH+filename, 'wb') as f:
        f.write(r.content)
f.close()
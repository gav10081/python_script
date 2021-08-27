from subprocess import call

PATH = "C:\\"

#Read the file list name
def readulrl():
    f = open('filename.txt', 'r')
    file_content = f.readlines()
    f.close()
    return file_content

if __name__ == '__main__':
    file_content=readulrl()
    for url in file_content:
        filename = PATH +url.split("/")[-1].strip("\n")
        call(["curl", url.strip("\n"), '-H', 'Connection: keep-alive', '-H', 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36', '-L', "-o", filename])

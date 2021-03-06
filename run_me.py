import subprocess
import yaml
import time

def translate(text):
    start_time = time.time()
    """
    Run translation model using config
    """
    with open('/home/ren/moses/moses-api/config.yaml', 'r') as f:
        doc = yaml.load(f)
    fileIn = doc['sample-models']['in']
    fileOut = doc['sample-models']['out']
    homeDir = doc['sample-models']['homeDir']
    runCommand = doc['sample-models']['command']
    status = 'Files successfully read'
    subprocess.call(['rm %s && rm %s' % (fileIn, fileOut)], shell=True)
    text8 = text.encode('utf8')
    inputFile = open(fileIn, 'w')
    inputFile.write(text8 + '\n')
    inputFile.close()
    subprocess.call([runCommand], cwd=homeDir, shell=True)
    readTranslate = open(fileOut, 'r')
    translatedText = readTranslate.read().decode('utf8')
    readTranslate.close()
    return translatedText.encode('utf8').rstrip()

def upload():
    """
    Tranlsate file
    """
    with open('translate_me.txt', 'r') as myfile:
    	text = myfile.read()
    text_t = translate(text)
    f = open('output.txt', 'w')
    f.write(text_t)
    f.close()

upload()

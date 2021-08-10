import os, yaml

homeDirectory = os.getenv('HOME')   

print('homeDirectory: %s' % homeDirectory)

configFile = os.path.join(
            os.path.join(
            os.path.join(
            os.path.join(
                homeDirectory, 
                '.chia'),
                'mainnet'),
                'config'),
                'config.yaml')

print('configFile: %s' % configFile)

with open(configFile, 'r') as stream:
    try:
        chiaConfiguration = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        
        print(exc)
        print('Chia configuration could not be read!')
        quit()

logFile = chiaConfiguration['farmer']['logging']['log_filename']

print('logFile: %s' % logFile)

# Chia Statistics

lineNumber = 0
with open(logFile, 'r') as stream:
    try:

        while True:

            lineNumber += 1
 
            logLine = stream.readline()
 
            if not logLine:
                break

            # Log line evaluation
            
            print("Line{}: {}".format(lineNumber, logLine.strip()))

    except:

        print('Log file could not be opened!')
        quit()

 


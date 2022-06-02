with open('deni_model/en-us.lm.bin', mode='rb') as file: # b is important -> binary
    fileContent = file.read()
    print(fileContent)

with open('deni_model/cmudict-en-us.dict', 'r') as file: # b is important -> binary
    filed = file.read()
    #print(filed)

with open('deni_model/deni/means', mode='rb') as file: # b is important -> binary
    ffiled = file.read()
    #print(ffiled)
import random
with open("e:\\InputFile.txt") as input_file ,open ("e:\\OutputFile.txt","w") as output_file:
        for line in input_file.readlines():
            scrmble_line_list =[]
            for word in line.strip().split(' '):
                if len(word) >3:
                    if word[-1]=='.' or word[-1]=='?' or word[-1]==';' or word[-1]=='!5':
                        word = word[0]+''.join(random.sample(word[1:-2],len(word)-3))+word[-2:]
                    else:
                        word = word[0]+''.join(random.sample(word[1:-1],len(word)-2))+word[-1]
                scrmble_line_list.append(word)
            scrmble_line=' '.join(scrmble_line_list)
            scrmble_line= scrmble_line + '\n'
            output_file.write(scrmble_line)
        input_file.close()
        output_file.close()
                                               

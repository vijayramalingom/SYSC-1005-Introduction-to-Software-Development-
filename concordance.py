import string
def build_concordance(filename):
    infile = open(filename, "r")
    line_count = 0
    line_hist = {}
    for line in infile:
        word_list = line.split()
        word_count_hist = {}
        line_count = line_count + 1
        for word in word_list:
            word = word.strip(string.punctuation).lower()
            if word != '':
                count = word_count_hist.get(word, 0)
                word_count_hist[word] = count + 1
                if word_count_hist[word] == 1:
                    lst = line_hist.get(word, [])
                    lst.append(line_count)
                    line_hist[word] = lst
    return line_hist

def aplhabetical_concordance():
    filename = input("Enter the Filename: ")
    hist = build_concordance(filename)
    for key,value in sorted(hist.items()):
        print(key, value)
        

aplhabetical_concordance()
                    
                
                 
        
    
    

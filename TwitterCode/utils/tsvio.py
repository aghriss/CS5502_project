import json

def read_tsv(file):
    print("\nReading",file)
    data = []
    f = open(file)
    for l in f.readlines():
        e = l.split()
        if len(e)==2:
            e = e+[file.split('/')[-1]]
        if len(e)>0:
            data.append(e)
    return data
    
def save_tsv(file, data):
    print("\nSaving",file)
    f= open(file,'w')
    for d in data:
        f.write("\t".join([str(dd) for dd in d])+"\n")
    f.close()
    return True
    
def read_dict(file):
    print("\nReading",file)
    return json.load(open(file))
def save_dict(file,dic):
    print("\nSaving",file)
    json.dump(dic, open(file,'w'))

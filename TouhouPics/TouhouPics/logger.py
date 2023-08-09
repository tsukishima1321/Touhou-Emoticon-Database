import time

def errorLog(e:Exception,t=""):
        f = open("errorlog.txt","a")
        f.write(time.asctime( time.localtime(time.time()))+"\n")
        f.write(repr(e)+"\n")
        f.write(t+"\n\n")
        f.close()

def reportLog(targetid:int,url:str,reason:str,detail=""):
        f = open("report.txt","a")
        f.write(time.asctime( time.localtime(time.time()))+"\n")
        f.write(reason+" "+str(targetid)+"  "+url+"\n"+detail+"\n")
        f.close()

def similarLog(id_main:int,url:str,ids,urls):
        f = open("similar.txt","a")
        f.write(time.asctime( time.localtime(time.time()))+"\n")
        f.write(str(id_main)+"  "+url+"\n")
        for i in range(0,len(ids)):
            f.write("    "+str(ids[i])+"  "+urls[i]+"\n")
        f.write("\n")
        f.close()
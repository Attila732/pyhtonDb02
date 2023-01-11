from dolgozo import Dolgozo

class Hr:
    def __init__(self):
        self.workerList=[]
    def readFile(self):
        file=open("dolgozok100.txt", "r",encoding="utf-8")
        row=file.readline()
        while row:
            row=file.readline()
            rowSp=row.split(":")
            if(len(rowSp)>1):
                worker=Dolgozo()
                worker.name=rowSp[0]
                worker.city=rowSp[1]
                worker.address=rowSp[2]
                worker.salary=rowSp[3]
                worker.bonus=rowSp[4]
                worker.born=rowSp[5]
                worker.hire=rowSp[6]

                self.workerList.append(worker)
        print(self.workerList[3])
    def countSzolnok(self):
        print("Szolnoki dolgozók")
        counter=0
        for i in self.workerList:
            if(i.city=="Szolnok" ):
                counter+=1
        print("{} fő van szolnokon".format(counter))    
    def ferencBonus(self):
        for worker in self.workerList:
            name=worker.name
            nameSp=name.split(" ")
            if nameSp[1]=="Ferenc":
                
                if worker.bonus=="0":
                    print("nincs bónusz")
                else:    
                    print(worker.name, worker.bonus)
                    
        file=open("ferencBonus.txt", "a", encoding="utf-8")
        file.write("Név,    emelt bónusz")
        if worker.bonus!="nincs bónusz":
            float(worker.bonus)*1.15
            file.write(worker.bonus)
            file.write(worker.name)
            
        file.close()
    def increaseFerencBonus(self):
         for worker in self.workerList:
            name=worker.name
            nameSp=name.split(" ")
            if nameSp[1]=="Ferenc":
                file=open("ferencBonus.txt", "a", encoding="utf-8")

                if worker.bonus!="0":
                    newBonus=int(worker.bonus)*1.15
                    bonus=str(newBonus)

                    file.write(worker.name)
                    file.write(", ")
                    file.write(bonus)
                    file.write("\n")
                file.close()            
                            
   
hr=Hr()
hr.readFile()      
hr.countSzolnok()       
#hr.ferencBonus()   
hr.increaseFerencBonus()

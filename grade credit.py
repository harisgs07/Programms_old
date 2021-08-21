def Sgpa(Grade,Credit):
    return [int(Grade[i])*int(Credit[i]) for i in range(len(Grade))]
Grade = input('Enter Grade Point space separately').split()
Credit = list(map(int,input('Enter Credit Point space separately').split()))
print (sum(Sgpa(Grade,Credit))/sum(Credit))


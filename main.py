def finder(n,k,t,numberOfGen):
  if(t==n):
    coincidence=0;
    for i in range(0,numberOfGen):
      if(genomes[i].find(''.join(findSequence))>-1):
        coincidence=coincidence+1
        index=i
    if(coincidence==1):
      combinations[index]=combinations[index]+''.join(findSequence)+'\n'
    return;
  for i in range(0,k):
    findSequence[t]=biologicalBasis[i];
    finder(n, k, t+1,numberOfGen);

print("/start");

genomes=[]
for i in range(1,4):
  with open("genome"+str(i)+".txt", 'r') as file:
      genomes.append(file.read().replace('\n', ''))

nameOfGenomes=["CovidU", "Flu", "CovidD"]


for i in range(0,len(genomes)):
  genomes[i]=genomes[i].replace(' ', '');
  for j in range(0,10):
    genomes[i]=genomes[i].replace(str(j), '');

# covidgentxt = open("covid.txt", "w")
# a = covidgentxt.write(genomeCovidU)
# covidgentxt.close()
    
biologicalBasis=''.join(set(''.join(genomes)));

combinations = ["" for i in range(len(genomes))]
print("input limit of the number of letters: ", end='')
numberOfGenomes=int(input())
print("searching...")

findSequence=["" for i in range(numberOfGenomes)]
for i in range(1, numberOfGenomes+1):
  finder(i,len(biologicalBasis),0,len(genomes))

print("unique combinations:\n")
for i in range (0,len(nameOfGenomes)):
  print(nameOfGenomes[i]+":\n"+combinations[i]);
print("/end")

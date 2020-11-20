from Bio import Entrez

Entrez.email = "seu.email@aqui.com"
BANCO = "biosample"

busca = Entrez.esearch(db=BANCO, term="human[ORGN] AND saliva AND exosome", retmax=3)
resultados = Entrez.read(busca)['IdList']

metadados_xml = Entrez.efetch(db=BANCO, id=resultados, retmode='xml')

# a análise do XML pode ser de diversos meios
# como o BeautifulSoup, por exemplo

from clases import Navie_Bayes
from clases import Document


myDocumento = Document("TablaGolf.txt")
myNavieBayes = Navie_Bayes(myDocumento.getMatriz(), myDocumento.getListaClases())
myNavieBayes.algoritmo()
myNavieBayes.mostrarValores()
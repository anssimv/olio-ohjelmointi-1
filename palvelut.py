import random


class Asiakas:
        """
        
        """

    def __init__(self, nimi, ika):
        pass


    def __luo_nro(self):
        pass

    def set_nimi(self, nimi):
        pass


    def set_ika(self, ika):
        pass


    def get_nimi(self):
        pass

    def get_ika(self):
        pass

    def get_asiakasnumero(self):
        pass


class palvelu:


    def __init__(self, tuotenimi):
        pass

    def lisaa_asikas(self, asiakas):
        pass

    def poista_asiakas(self, asiakas):
        pass
    
      
    def _luo_asiakasrivi(self, asiakas):
        pass

    def tulosta_asiakkaat(self):
        pass



class ParempiPalvelu(Palvelu):

    def __init__(self, tuotenimi):
        pass

























































"""
import random

   #   -=__        #=_   +=none 



class Asiakas:
    
    :ivar asiakkaan nimi: asiakkaan nimi
    :type: str
    :ivar asiakasnumero: koostuu numeroista, arvotaan random.randitilla
    :type: int[]
    :ivar: asiakkaan ikä: asiakkaan ikä
    :type: int
    

    #luo_nro
    def __init__(self, nimi, ika):
        self.__nimi = nimi
        self.__asiakasnro = luo_numero()
        self.__ika = ika


        
        
        
        
        
    
    def get_tiedot(asiakas):
        raise ValueError("Annettiin negatiivinen luku.")
        print(asiakas)
    
    
    
    

    def __get_asiakasnro():
        pass



    def luo_numero():
         
        ensimmainen_osa = random.randint(1, 99)
                
        toinen_osa = random.randint(1, 999)
            
        kolmas_osa = random.randint(1, 999)

        return f"{ensimmainen_osa}, _ {toinen_osa}, - {kolmas_osa}"
        






    class Palvelu:
        
        :ivar: Tuotenimi: minkä tuotteen asiakkaat listataan
        :type: str
        :ivar: asiakkaat: kertoo ketkä tuotetta käyttävät 
        :type: Asiakas[]
        
        def __init__(self, tuotenimi, asiakkaat):


            
            
            
            
        def tulosta_asiakkaat(Palvelu):
            print(Palvelu.asiakkaat)

            
            
            
            
            def get_luo_asiakasrivi(Asiakas):
                print(f"{nimi} ({asiakas_nro}) on {ika}-vuotias")

            
            :ivar: luo_asiakasrivi(Asiakas): perii luokasta Asiakas nimen, asiakasnumeron
            ja iän ja luo niistä tietorivin.
            :type: str
            :ivar: lisaa_asiakas
            

            :param: erotin: numeron osien väliin alitettava väliviiva
            :type: str
            :ivar: poista_asiakas(Asiakas): poistaa asiakkaan tiedot
            :type: [str]
            :ivar: tulosta_asiakkaat: tulostaa kaikkien asiakkaiden tiedot
            :type: str
            
            

        def poista_asiakas
            poistettava = (input("kenet poistetaan"))
            try: poistettava in edut:
                edut.pop(poistettava)

            except ValueError: ("asiakasta ei ole listassa")


        


        
            #def luo_asakasrivi(Asiakas):
    #palvelu
    #tuotenimi
                #pass






    class ParemiPalvelu(Palvelu):
#

        def __init__(self, edut):
            edut = []

        def lisaa_etu():
            edut.append(etu)


            :ivar: lisaa_etu: lisää edun listaan
            :type: str
     

        def poista_etu():
            poistettava = (input("Anna kokonaisluku: "))
            try: poistettava in edut:
                edut.pop(poistettava)

            except ValueError: ("Etua ei ole listassa")

            

            :ivar: poista_etu: poistaa edun listasta
            :type: str
  
        def tulosta_edut():
            print(edut)
       
            :IVAR: tulosta_edut: tulostaa edut
            :type: str

"""
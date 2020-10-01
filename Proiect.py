#
#   proiect final curs python
#

class catalog():
    caracteristici = []
    lista_obiecte = []
    clasa = dict()
    dictionar_preturi = dict()
    dictionar_consum = dict()
    dictionar_producatori = dict()
    x1,x2,x3,x4 = 0,0,0,0
    def __init__(self,pret,consum,producator,cod_produs):
        self.pret = pret
        self.consum = consum
        self.producator = producator
        self.cod_produs = cod_produs
        catalog.caracteristici += [[self.pret,self.consum,self.producator,self.cod_produs]]
    def sort_by_price(self):
        """Sorteaza dupa pret"""
        m = sorted(list(catalog.dictionar_preturi.values()))
        lista = []
        for x in m:
            for nume,pret in catalog.dictionar_preturi.items():
                if x == pret:
                    lista.append(nume)
        print(lista)
    def sort_by_consum(self):
        """Sorteaza dupa consum"""
        m = sorted(list(catalog.dictionar_consum.values()))
        lista = []
        for x in m:
            for nume,consum in catalog.dictionar_consum.items():
                if x == consum:
                    lista.append(nume)
        print(lista)
    def sort_by_manufacturer(self,producator):
        """Afiseaza o lista cu obiectele de la un anumit producator"""
        lista = []
        for nume,manufacturer in catalog.dictionar_producatori.items():
            if producator == manufacturer:
                lista.append(nume)
        print(lista)
    def sort_by_class(self,x):
        """Afiseaza obiectele din clasa Electrocasnice mari sau Electrocasnice mici"""
        print(catalog.clasa[x])

class Electrocasnice_mari(catalog):
    def __init__(self,adancime,latime,inaltime,pret,consum,producator,cod_produs):
        catalog.__init__(self,pret,consum,producator,cod_produs)
        self.adancime = adancime
        self.latime = latime
        self.inaltime = inaltime

class Electrocasnice_mici(catalog):
    def __init__(self,lungime_cablu,baterie,pret,consum,producator,cod_produs):
        catalog.__init__(self,pret,consum,producator,cod_produs)
        self.lungime_cablu = lungime_cablu
        self.baterie = baterie

class Frigider(Electrocasnice_mari):
    def __init__(self,adancime,latime,inaltime,pret,consum,producator,cod_produs,capacitate_congelator,capacitate_frigider):
        Electrocasnice_mari.__init__(self,adancime,latime,inaltime,pret,consum,producator,cod_produs)
        self.capacitate_congelator = capacitate_congelator
        self.capacitate_frigider = capacitate_frigider
        catalog.x1 += 1
        if catalog.x1 == 1 and 'Electrocasnice mari' not in catalog.clasa:
            catalog.clasa['Electrocasnice mari'] = [f'Frigider{catalog.x1}']
        else :
            catalog.clasa['Electrocasnice mari'] += [f'Frigider{catalog.x1}']
        catalog.lista_obiecte += [f'Frigider{catalog.x1}']
        catalog.dictionar_preturi[f'Frigider{catalog.x1}'] = self.pret
        catalog.dictionar_consum[f'Frigider{catalog.x1}'] = self.consum
        catalog.dictionar_producatori[f'Frigider{catalog.x1}'] = self.producator

class Aragaz(Electrocasnice_mari):
    def __init__(self,adancime,latime,inaltime,pret,consum,producator,cod_produs,nr_arzatoare):
        Electrocasnice_mari.__init__(self,adancime,latime,inaltime,pret,consum,producator,cod_produs)
        self.nr_arzatoare = nr_arzatoare
        catalog.x2 += 1
        if catalog.x2 == 1 and 'Electrocasnice mari' not in catalog.clasa:
            catalog.clasa['Electrocasnice mari'] = [f'Aragaz{catalog.x2}']
        else:
            catalog.clasa['Electrocasnice mari'] += [f'Aragaz{catalog.x2}']
        catalog.lista_obiecte += [f'Aragaz{catalog.x2}']
        catalog.dictionar_preturi[f'Aragaz{catalog.x2}'] = self.pret
        catalog.dictionar_consum[f'Aragaz{catalog.x2}'] = self.consum
        catalog.dictionar_producatori[f'Aragaz{catalog.x2}'] = self.producator

class Mixer(Electrocasnice_mici):
    def __init__(self,lungime_cablu,baterie,pret,consum,producator,cod_produs,rotatii_min):
        Electrocasnice_mici.__init__(self,lungime_cablu,baterie,pret,consum,producator,cod_produs)
        self.roatii_min = rotatii_min
        catalog.x3 += 1
        if catalog.x3 == 1 and 'Electrocasnice mici' not in catalog.clasa:
            catalog.clasa['Electrocasnice mici'] = [f'Mixer{catalog.x3}']
        else:
            catalog.clasa['Electrocasnice mici'] += [f'Mixer{catalog.x3}']
        catalog.lista_obiecte += [f'Mixer{catalog.x3}']
        catalog.dictionar_preturi[f'Mixer{catalog.x3}'] = self.pret
        catalog.dictionar_consum[f'Mixer{catalog.x3}'] = self.consum
        catalog.dictionar_producatori[f'Mixer{catalog.x3}'] = self.producator

class Fier_calcat(Electrocasnice_mici):
    def __init__(self,lungime_cablu,baterie,pret,consum,producator,cod_produs,rezervor):
        Electrocasnice_mici.__init__(self,lungime_cablu,baterie,pret,consum,producator,cod_produs)
        self.rezervor = rezervor
        catalog.x4 += 1
        if catalog.x4 == 1 and 'Electrocasnice mici' not in catalog.clasa:
            catalog.clasa['Electrocasnice mici'] = [f'Fier calcat{catalog.x4}']
        else:
            catalog.clasa['Electrocasnice mici'] += [f'Fier calcat{catalog.x4}']
        catalog.lista_obiecte += [f'Fier calcat{catalog.x4}']
        catalog.dictionar_preturi[f'Fier calcat{catalog.x4}'] = self.pret
        catalog.dictionar_consum[f'Fier calcat{catalog.x4}'] = self.consum
        catalog.dictionar_producatori[f'Fier calcat{catalog.x4}'] = self.producator

frigider1 = Frigider(0.60,0.54,1.46,799,2260,'Arctic','AD54240P','46L','177L')
frigider2 = Frigider(0.77,0.79,178.5,2800,2900,'Samsung','RT50K6335SL','125L','375L')
aragaz1 = Aragaz(0.60,0.60,0.85,1299,2000,'Beko','FSM62530DXMS',4)
aragaz2 = Aragaz(0.50,0.50,0.85,599,1600,'Arctic','AGM5500F',4)
mixer1 = Mixer(2.1,3000,400,200,'Daewoo','DHM100B',500)
mixer2 = Mixer(1.7,3100,550,225,'Bosch','MFQ36440',600)
fier_calcat1 = Fier_calcat(2,2500,300,250,'Philips','GC455440','1L')
fier_calcat2 = Fier_calcat(1.8,2400,860,350,'Tefal','GV7850E0','1.6L')

fier_calcat1.sort_by_price()
frigider2.sort_by_consum()
mixer2.sort_by_class('Electrocasnice mici')
aragaz1.sort_by_manufacturer('Arctic')
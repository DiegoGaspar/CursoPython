class Casa(object):


	def __init__(self, cor, altura, quartos):
		self.cor=cor
		self.altura=altura
		self.quartos=quartos

	def pintar(self, cor):
		self.cor=cor

	def aumenta_quartos(self, quartos):
		self.quartos=quartos

	def imprime_casa(self):
		print(self.cor, self.altura, self.quartos)	
			

m_casa = Casa(input('qual a cor'), input('Qual altura'), input('Quantos quartos'))

m_casa.imprime_casa()
print(m_casa.cor)

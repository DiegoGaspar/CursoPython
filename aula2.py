'''
Herança 
'''

class ContaBancaria(object):
	
	def __init__(self):
		self.saldo = 0

	def depositar(self,valor):
		self.saldo += valor
		self.consultarSaldo()
	
	def sacar(self,valor):
		self.saldo -= valor
		self.consultarSaldo()


	def consultarSaldo(self):
		print(self.saldo)			

class ContaPoupanca(ContaBancaria):
	def _consultarRentabilidade(self):
		return 1.6

	def rentabilidade(self):
		rentabilidade = self._consultarRentabilidade()
		if rentabilidade < 0.5:
			print('Consulte seu gerente ')
		else:
			print(rentabilidade)	


conta_bancaria = ContaPoupanca()
conta_bancaria.rentabilidade()
conta_bancaria.depositar(150)
conta_bancaria.sacar(75)
conta_bancaria.consultarSaldo()

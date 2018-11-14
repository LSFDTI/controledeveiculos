from django.db import models

# Create your models here.
class Casa(models.Model):
	nome = models.CharField(max_length = 150, blank = False, null = False)

	def __str__(self):
		return self.nome

class Marca(models.Model):
	marca = models.CharField(max_length=50,blank=False,null=False)

	def __str__(self):
		return self.marca

class Detran(models.Model):
	detran = models.CharField(max_length = 10, blank=False, null = False)

	def __str__(self):
		return self.detran
	
class Veiculo(models.Model):

	casa = models.ForeignKey(Casa,on_delete=models.CASCADE, verbose_name = 'pertence a')
	marca_veiculo = models.ForeignKey(Marca,on_delete=models.CASCADE)
	modelo = models.CharField(max_length=50,blank=False,null=False)
	ano = models.IntegerField(max_length=50,blank=False,null=False)
	placa =  models.CharField(max_length=50,blank=False,null=False)
	renavam =  models.IntegerField(max_length=50,blank=False,null=False)
	chassi =  models.CharField(max_length=50,blank=False,null=False)
	observação = models.CharField(max_length=50,blank=False,null=False)
	detran = models.ForeignKey(Detran,on_delete=models.CASCADE)
	documento = models.CharField(max_length=2,blank=False,null=False)

	def __str__(self):
		return self.marca_veiculo.marca


class Mese(models.Model):
	meses = models.CharField(max_length=50,blank=False,null=False)

class Seguro(models.Model):
	Veículo = models.ForeignKey(Veiculo,on_delete=models.CASCADE)
	seguradora = models.CharField(max_length=50,blank=False,null=False)
	data = models.DateField(null=False)
	apólice =  models.IntegerField(max_length=50,blank=False,null=False)
	valor =  models.DecimalField(max_digits=10,decimal_places=2)

	def __str__(self):
		return self.seguradora





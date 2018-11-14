from django.contrib import admin
from .models import Casa
from .models import Veiculo
from .models import Mese
from .models import Seguro
from .models import Marca
from .models import Detran

class VeiculoAdmin(admin.ModelAdmin):
	list_display = ('casa', 'modelo', 'placa', 'renavam')
	search_fields = ['modelo', 'casa__nome']
	list_filter = ['casa']





admin.site.register(Casa)
admin.site.register(Veiculo, VeiculoAdmin)
admin.site.register(Mese)
admin.site.register(Seguro)
admin.site.register(Marca)
admin.site.register(Detran)
from django.db import models

# Cadastro de Endereços
class Address(models.Model):
    street = models.CharField(max_length=255, verbose_name='Rua')
    number = models.CharField(max_length=10, verbose_name='Número')
    complement = models.CharField(max_length=255, verbose_name='Complemento')
    neighborhood = models.CharField(max_length=255, verbose_name='Bairro')
    city = models.CharField(max_length=255, verbose_name='Cidade')
    state = models.CharField(max_length=2, verbose_name='Estado')
    zip_code = models.CharField(max_length=10, verbose_name='CEP')

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __str__(self):
        return self.street

# Cadastro de Clientes: Empresas/Clubes
class Client(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')
    cnpj = models.CharField(max_length=18, unique=True, null=True, blank=False, verbose_name='CNPJ')
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='clients', verbose_name='Endereço')
    phone = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.name

# Cadastro de Quadras
class Quatrain(models.Model):
    SOCCER = 'soccer'
    VOLLEYBALL = 'volleyball'
    BASKETBALL = 'basketball'
    TENNIS = 'tennis'
    HANDBALL = 'handball'
    FUTSAL = 'futsal'
    BEACH_TENNIS = 'beach_tennis'
    SPORT_CHOICES = [
        (SOCCER, 'Soccer'),
        (VOLLEYBALL, 'Volleyball'),
        (BASKETBALL, 'Basketball'),
        (TENNIS, 'Tennis'),
        (HANDBALL, 'Handball'),
        (FUTSAL, 'Futsal'),
        (BEACH_TENNIS, 'Beach Tennis'),
    ]
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='quatrains')
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50, choices=SPORT_CHOICES, default=SOCCER)
    availability = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Quadra'
        verbose_name_plural = 'Quadras'

    def __str__(self):
        return f"{self.name} ({self.client.name})"

# Cadastro de Parceiros
class Partner(models.Model):
    name = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True, null=True, blank=False)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='partners', verbose_name='Endereço')
    phone = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Parceiro'
        verbose_name_plural = 'Parceiros'

    def __str__(self):
        return self.name

# Cadastro de Mídias dos Parceiros com localização relacionada às quadras ativas
class Media(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, related_name='partners')
    quatrain = models.ForeignKey(Quatrain, on_delete=models.CASCADE, related_name='quatrains')
    days = models.IntegerField(help_text="Número de dias de exibição")
    path = models.FileField(upload_to='medias/', help_text="Arquivo de mídia", verbose_name="Moldura", null=True, blank=False)

    class Meta:
        verbose_name = 'Mídia'
        verbose_name_plural = 'Mídias'

    def __str__(self):
        return f"Mídia de {self.partner.name} na quadra {self.quatrain.name}"

# Financeiro - Planos de Parceiros
class PlanPartner(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, related_name='plans')
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    class Meta:
        verbose_name = 'Plano de Parceiro'
        verbose_name_plural = 'Planos de Parceiros'

    def __str__(self):
        return f"{self.name} - {self.partner.name}"

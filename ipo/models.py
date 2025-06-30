from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    logo = models.URLField(blank=True, null=True)  # Placeholder logo URL

    def __str__(self):
        return self.name

class IPO(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='ipos')
    price_band = models.CharField(max_length=50)
    issue_size = models.CharField(max_length=100)
    issue_type = models.CharField(max_length=100)
    opening_date = models.DateField()
    closing_date = models.DateField()
    listing_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=50)
    ipo_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    listing_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    listing_gain = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cmp = models.DecimalField("Current Market Price", max_digits=10, decimal_places=2, blank=True, null=True)
    current_return = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.company.name} - {self.status}"

class Document(models.Model):
    ipo = models.ForeignKey(IPO, on_delete=models.CASCADE, related_name='documents')
    rhp = models.FileField(upload_to='docs/rhp/', blank=True, null=True)
    drhp = models.FileField(upload_to='docs/drhp/', blank=True, null=True)

    def __str__(self):
        return f"Documents for {self.ipo.company.name}"

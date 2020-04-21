from django.db import models

# Create your models here.
class prodDir(models.Model):
    """Model definition for prodDir."""

    # TODO: Define fields here
    prodName = models.CharField(max_length=100)
    numOfPieces = models.PositiveIntegerField(default=0)
    buyingPrice = models.DecimalField(max_digits=5, decimal_places=2)
    sellingPrice = models.DecimalField(max_digits=5, decimal_places=2)
    totalValue = models.DecimalField

    class Meta:
        """Meta definition for prodDir."""

        verbose_name = 'prodDir'
        verbose_name_plural = 'prodDirs'

    def __str__(self):
        """Unicode representation of prodDir."""
        return prodDir.prodName, prodDir.numOfPieces, prodDir.buyingPrice, prodDir.sellingPrice, prodDir.totalValue

class transHis(models.Model):
    """Model definition for transHis."""

    # TODO: Define fields here
    prodId = models.ForeignKey(prodDir, on_delete=models.CASCADE)
    transType = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        """Meta definition for transHis."""

        verbose_name = 'transHis'
        verbose_name_plural = 'transHis'

    def __str__(self):
        """Unicode representation of transHis."""
        return transHis.prodId, transHis.price, transHis.transType


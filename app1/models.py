from django.db import models

class Kurs(models.Model):
    nom = models.CharField(max_length=50)
    narx = models.PositiveSmallIntegerField()
    davomiylik = models.CharField(max_length=50)
    dars_narxi = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.nom


class Xona(models.Model):
    qavat = models.CharField(max_length=50)
    xona =  models.CharField(max_length=50,null=True,blank=True)
    nom =  models.CharField(max_length=50)
    sigim = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.qavat

class Oquvchi(models.Model):
    ism = models.CharField(max_length=50)
    yosh = models.PositiveSmallIntegerField()
    tel = models.CharField(max_length=50)
    qayerdan = models.CharField(max_length=50)
    tel2 = models.CharField(max_length=50, null=True,blank=True)

    def __str__(self):
        return self.ism


class Ustoz(models.Model):
    ism_fan = models.CharField(max_length=50)
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)
    daraja = models.CharField(max_length=50)
    tel = models.CharField(max_length=50, null=True, blank = True)

    def __str__(self):
        return self.ism_fan

class Guruh(models.Model):
    nom = models.CharField(max_length=50)
    ustoz = models.ForeignKey(Ustoz, on_delete=models.CASCADE)
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)
    kun = models.CharField(max_length=50, choices=(
        ("Du-Chorshanba-Juma","Du-Chorshanba-Juma"),
        ("Se-Payshanba-Shanba", "Se-Payshanba-Shanba")
    ))
    vaqt = models.CharField(max_length=50)
    xona = models.ForeignKey(Xona, on_delete=models.CASCADE)
    oquvchilar = models.ManyToManyField(Oquvchi, null = True)

class Davomat(models.Model):
    oquvchi = models.ForeignKey(Oquvchi, on_delete=models.CASCADE)
    guruh = models.ForeignKey(Guruh, on_delete=models.CASCADE)
    holat = models.CharField(max_length=50, choices=(
        ("Keldi","Keldi"),
        ("Sababli", "Sababli"),
        ("Sababsiz", "Sababsiz")
    ))
    sana =models.DateField(auto_now_add=True)


    def __str__(self):
        return self.holat

class Tolov(models.Model):
    oquvchi = models.ForeignKey(Oquvchi, on_delete=models.CASCADE)
    guruh = models.ForeignKey(Guruh, on_delete=models.CASCADE)
    chegirma = models.PositiveIntegerField()
    summa = models.PositiveIntegerField()
    tolangan_summa = models.PositiveIntegerField()
    sana = models.DateField(auto_now_add=True)
    oy = models.CharField(max_length=30)
    yil = models.PositiveSmallIntegerField()
    admin = models.CharField(max_length=30)
    turi = models.CharField(max_length=30)

    def __str__(self):
        return self.oquvchi.ism





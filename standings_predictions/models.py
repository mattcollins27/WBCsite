from django.db import models

# Create your models here.
class Team(models.Model):
    POOLS = [
        ('A', 'Pool A'),
        ('B', 'Pool B'),
        ('C', 'Pool C'),
        ('D', 'Pool D'),
    ]

    name = models.CharField(max_length=100)
    pool = models.CharField(max_length=1, choices=POOLS)
    logo = models.ImageField(upload_to='logos/')

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=100)

    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="players"
    )

    position = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.name} ({self.team.name})"


class Submission(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    pool_A = models.TextField()
    pool_B = models.TextField()
    pool_C = models.TextField()
    pool_D = models.TextField()

        # Lineup ForeignKeys
    catcher = models.ForeignKey(Player, related_name="catcher_submissions",
                          on_delete=models.SET_NULL, null=True, blank=True)

    first_base = models.ForeignKey(Player, related_name="first_base_submissions",
                            on_delete=models.SET_NULL, null=True, blank=True)

    second_base = models.ForeignKey(Player, related_name="second_base_submissions",
                            on_delete=models.SET_NULL, null=True, blank=True)

    third_base = models.ForeignKey(Player, related_name="third_base_submissions",
                            on_delete=models.SET_NULL, null=True, blank=True)

    shortstop = models.ForeignKey(Player, related_name="ss_submissions",
                           on_delete=models.SET_NULL, null=True, blank=True)

    outfield_1 = models.ForeignKey(Player, related_name="of1_submissions",
                            on_delete=models.SET_NULL, null=True, blank=True)

    outfield_2 = models.ForeignKey(Player, related_name="of2_submissions",
                            on_delete=models.SET_NULL, null=True, blank=True)

    outfield_3 = models.ForeignKey(Player, related_name="of3_submissions",
                            on_delete=models.SET_NULL, null=True, blank=True)
    
    pitcher = models.ForeignKey(Player, related_name="p_submissions",
                            on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


    
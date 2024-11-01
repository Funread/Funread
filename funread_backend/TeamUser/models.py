
from django.db import models
from User_Levels.models import UserLevels  
from Team.models import Team  

class TeamUser(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, db_column='TeamId')
    user = models.ForeignKey(UserLevels, on_delete=models.CASCADE, db_column='UserId')  

    class Meta:
        db_table = 'teamuser'




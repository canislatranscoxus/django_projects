from django.db import models

# Create your models here.
#

class Node( models.Model ):
    name = models.CharField( max_length = 60 )
    NODES = [
        ( 'b', 'Boy'   ),
        ( 'g', 'Girl'  ),
        ( 'f', 'family') ]
    type = models.CharField( choices = NODES, max_length = 1 )


class Edge(models.Model ):
    src = models.ForeignKey( Node, related_name='parent', on_delete= models.CASCADE )
    tar = models.ForeignKey( Node, related_name='child' , on_delete= models.CASCADE )


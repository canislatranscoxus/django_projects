from django      import forms
from geny.models import Node, Edge

class NodeForm( forms.ModelForm ):
    class Meta:
        model = Node
        fields = '__all__'

class EdgeForm( forms.ModelForm ):
    class Meta:
        model = Edge
        fields = '__all__'
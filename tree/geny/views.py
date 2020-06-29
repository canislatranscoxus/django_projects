from django.http            import request
from django.shortcuts       import render, redirect
from django.views.generic   import ListView, CreateView, UpdateView, DeleteView
from django.urls            import reverse_lazy

from geny.models            import Node, Edge
from geny.forms             import NodeForm, EdgeForm

# Create your views here.
class NodeListView( ListView ):
    model = Node

class NodeCreateView( CreateView ):
    model       = Node
    success_url = reverse_lazy( 'index' )
    fields      = ( 'name', 'type' )

class NodeUpdateView( UpdateView ):
    model       = Node
    success_url = reverse_lazy( 'index' )
    fields      = ( 'name', 'type' )

class NodeDeleteView( DeleteView ):
    model       = Node
    success_url = reverse_lazy( 'index' )

# -----------------------------------------------------------------------------

class EdgeListView( ListView ):
    model = Edge

class EdgeCreateView( CreateView ):
    model       = Edge
    success_url = reverse_lazy( 'index' )
    fields      = ( 'name', 'type' )

class EdgeUpdateView( UpdateView ):
    model       = Edge
    success_url = reverse_lazy( 'index' )
    fields      = ( 'name', 'type' )

class EdgeDeleteView( DeleteView ):
    model       = Edge
    success_url = reverse_lazy( 'index' )

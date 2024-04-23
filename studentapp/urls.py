from django.urls import path
from studentapp.views import *

urlpatterns = [
    path('studentadd/', student_add, name='product'),
    path('studentlist/',student_list,name='student'),
    path('student/<int:student_id>/delete',student_delete,name='studentdelete'),
    
    
    path('schooladd/', school_add, name='product'),
    path('schoollist/',school_list,name='student'),
    path('school/<int:school_id>/delete',school_delete,name='studentdelete'),
    
    
    path('batchadd/', batch_add, name='product'),
    path('batchlist/',batch_list,name='student'),
    path('batch/<int:batch_id>/delete',student_delete,name='studentdelete'),
]
from django.urls import path, include
from . import views

urlpatterns = [
    path('viewpatientdata/', views.viewpatientdata, name = 'viewpatientdata'),
    path('addpatient/', views.addpatient, name = 'addpatient'),
    path('updatepatientdata/<int:id>', views.updatepatientdata, name = 'updatepatientdata'),
    path('deletepatientdata/<int:id>', views.deletepatientdata, name = 'deletepatientdata'),
    
]
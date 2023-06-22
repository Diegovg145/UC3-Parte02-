from django.shortcuts import render, HttpResponse
layout = """
    <div class="flex">
            <div class="imagen">
                <img src="../static/images/logo.png" alt="logo">
            </div>
            <div class="navegacion">
                <a href="/inicio">INICIO</a>
                <a href="">PRIMOS</a>
                <a href="">EXAMEN</a>
            </div>
    </div>
"""
def index(request):
    return render(request,"index.html")

def inicio(request):
    lista=["Matemática","Programación","Diseño Web","Gestion de Procesos","Algoritmos","Requerimientos","Tesis"]
    resultado = """
        Mostrando la lista de los cursos: 
        <br>
        <ul>
    """
    for i in lista:
        resultado+=f"<li>{i}</li>"
    resultado+="</ul>"
    return HttpResponse(layout +resultado)


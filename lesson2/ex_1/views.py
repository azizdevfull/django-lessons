from django.shortcuts import render
from django.http import HttpResponse

def ex1(request, son):
    son = int(son) 
    if son >= 0:
        html = f"""
        <h1>Pilus son: {son}</h1>
            """
    else:
        html = f"""
        <h1>Minus son: {son}</h1>
            """

    return HttpResponse(html)

def ex2(request, son):
    if son % 2 == 0:
        html = f"""
        <h1>Juft son: {son}</h1>
            """
    else:
        html = f"""
        <h1>Toq son: {son}</h1>
            """
    return HttpResponse(html)

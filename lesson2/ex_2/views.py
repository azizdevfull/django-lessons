from django.shortcuts import render
from django.http import HttpResponse

def ex1(request, son):
    son = int(son)
    if son == 1:
        html = f"""
        <h1>Dushanba</h1>
            """
    elif son == 2:
         html = f"""
         <h1>Seshanba</h1>
            """
    elif son == 3:
         html = f"""
         <h1>Chorshanba</h1>
            """
    elif son == 4:
         html = f"""
         <h1>Payshanba</h1>
            """
    elif son == 5:
         html = f"""
         <h1>Juma</h1>
            """
    elif son == 6:
         html = f"""
         <h1>Shanba</h1>
            """
    elif son == 7:
        html = f"""
        <h1>Yakshanba</h1>
            """
    else:
        html = """
        <h1>Xato son!</h1>
        """

    return HttpResponse(html)

def ex2(request, son):
    son = int(son)
    if son > 0:
        son = son + 2
        html = f"""
        <h1>Jabvob: {son}</h1>
            """
    else:
        son = son - 2
        html = f"""
        <h1>Javob: {son}</h1>
            """
    return HttpResponse(html)

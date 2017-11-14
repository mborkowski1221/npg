#!/usr/bin/env python
#-*- coding: utf-8 -*-
print "....:::::KALKULATOR::::...."
 
def menu():
    print "::MENU::"
    print "1 - dodawanie"
    print "2 - odejmowanie"
    print "3 - mno¿enie"
    print "4 - dzielenie"
    print "5 - dzielenie ca³kowite"
    print "6 - potêgowanie"
    print "7 - autor"
    print "8 - o programie"
    print "9 - koniec"
    print "0 - MENU"
    return 
 
def dodawanie():
    a = raw_input("Pierwsza liczba ")
    b = raw_input("Druga liczba ")
    wynik = float(a)+float(b)
    return wynik
 
def odejmowanie():
    a = raw_input("Pierwsza liczba ")
    b = raw_input("Druga liczba ")
    wynik = float(a)-float(b)
    return wynik
def mnozenie():
    a = raw_input("Pierwsza liczba ")
    b = raw_input("Druga liczba ")
    wynik = float(a)*float(b)
    return wynik
def dzielenie():
    a = raw_input("Pierwsza liczba ")
    b = raw_input("Druga liczba ")
    wynik = float(a)/float(b)
    return wynik
def dzieleniecal():
    a = raw_input("Pierwsza liczba ")
    b = raw_input("Druga liczba ")
    dziel = int(a)/int(b)
    reszta = int(a)%int(b)
    wynik = "wynik",dziel,"reszty",reszta
    return wynik
def potegowanie():
    a = raw_input("Liczba ")
    b = raw_input("Potêga ")
    wynik = float(a)**float(b)
    return wynik
def autor():
    wynik = "Autor"
    return wynik
def program():
    wynik = "Program Kalkulator"
    return wynik
 
#Wyswietlanie
 
print menu()
operacja = raw_input("Co wybierzesz ? ")
while operacja<>"9":
    if operacja=="1": print ":::wybra³eœ dodawanie:::\n",dodawanie()
    elif operacja=="2": print ":::wybra³eœ odejmowanie:::\n",odejmowanie()
    elif operacja=="3": print ":::wybra³eœ mno¿enie:::\n",mnozenie()
    elif operacja=="4": print ":::wybra³eœ dzielenie :::\n",dzielenie()
    elif operacja=="5": print ":::wybra³eœ dzielenie calkowite:::\n",dzieleniecal()
    elif operacja=="6": print ":::wybra³eœ potegowanie:::\n",potegowanie()
    elif operacja=="7": print ":::wybra³eœ autor:::\n",autor()
    elif operacja=="8": print ":::wybra³eœ O programie:::\n",program()
    elif operacja=="0": print menu()
    elif operacja=="9": break
    else: print"Error menu"
    operacja = raw_input("Co wybierzesz ? ")
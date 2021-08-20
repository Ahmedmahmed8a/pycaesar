#!/bin/python
"""
┌──────────────────────────────────────────┐
│                                          │
│                                          │
│  ▄▄▄    ▄▄▄    ▄▄▄    ▄▄▄    ▄▄▄    ▄ ▄▄ │
│ █▀  ▀  ▀   █  █▀  █  █   ▀  ▀   █   █▀  ▀│
│ █      ▄▀▀▀█  █▀▀▀▀   ▀▀▀▄  ▄▀▀▀█   █    │
│ ▀█▄▄▀  ▀▄▄▀█  ▀█▄▄▀  ▀▄▄▄▀  ▀▄▄▀█   █    │
│          github.com/ahmedMahmed8a        │
│                                          │
└──────────────────────────────────────────┘
"""
def caesar(text,offset,type):
 out=""
 if(type=="enc"):
  for i in range(len(text)):
   out=out+chr(ord(text[i])+offset)
 elif(type=="dec"):
  for i in range(len(text)):
   out=out+chr(ord(text[i])-offset)
 else:
  out="Error "
 return out
txt=input("Text: ")
off=int(input("Offset: "))
typ=input("enc/dec: ")
print(caesar(txt,off,typ))

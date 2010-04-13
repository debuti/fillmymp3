#!/bin/bash

#TODO:Fix this and give a little format, for Gods sake!

# Descripcion: Programa que me llena aleatoriamente de musica el pendrive, tiene que estar montado en tipo vfat
#              El formato de la coleccion de musica es ALBUMS/<ARTISTA>/<ALBUM>
# Version: 0-0-1

i=0
a=0

if [ $# -ne 4 ]
then
 echo -e "Usage: $0  <directorio coleccion> <No de albums a copiar> <directorio destino> <Borrar todo?(S/N)>"
else
 raiz="$1"							#Reconocimiento de parametros
 num="$2"  
 dest="$3"
 if [ "$4" = "S" ]
 then
  cd "$dest"
  rm -rf *
 fi

 cd "$raiz"							#Cuento el numero de artistas
 contador1=0;
 for i in *
 do
  if [ -d "$i" ]
  then
   let contador1++
  fi
 done
 echo "Hay $contador1 artistas en esa carpeta."


 for ((a=0; a<$num; a++))
 do
  aleatorio1=0;
  while [ $aleatorio1 -lt 100000000 ]				#Si es menor que este numero el let da error ¿?
  do
   aleatorio1=`date +%N`
  done
  let aleatorio1=$aleatorio1/1000
  let aleatorio1=$aleatorio1%$contador1
  let aleatorio1=$aleatorio1+1
  for i in *
  do
   if [ -d "$i" ]						#Recorro la carpeta hasta llegar donde quiero
   then
    let aleatorio1--
   fi
   if [ $aleatorio1 -eq 0 ]
   then
    break
   fi
  done
  echo -e "\nMe ha apetecido copiar algo de $i, que mola mazo :D"
  cd "$i"

  contador2=0;
  for j in *
  do
   if [ -d "$j" ]
   then
    let contador2++
   fi
  done
  echo "Hay $contador2 albums de $i."
  aleatorio2=0;
  while [ $aleatorio2 -lt 100000000 ]
  do
   aleatorio2=`date +%N`
  done
  let aleatorio2=$aleatorio2/1000
  let aleatorio2=$aleatorio2%$contador2
  let aleatorio2=$aleatorio2+1
  for j in *
  do
   if [ -d "$j" ]
   then
    let aleatorio2--
   fi
   if [ $aleatorio2 -eq 0 ]
   then
    break
   fi
  done
  echo -e "Me ha apetecido copiar el $j, que es un album muy guapo"
  cp -r "$j" "$dest"
  cd ..
 done

 sync
fi

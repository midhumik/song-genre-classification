#To crop every song to 30 seconds
for i in /home/midhun/Documents/Project/pgms/inp/*.mp3;
  do 
   name=$(basename "$i")
#  ffmpeg -ss 10 -t 30 -i "$i" -c copy /home/midhun/Documents/Project/pgms/out/file-$(( ctr+=1 )).mp3;
   ffmpeg -ss 10 -t 30 -i "$i" -c copy /home/midhun/Documents/Project/pgms/out/cropped/"$name";


done

for file in /home/midhun/Documents/Project/pgms/out/cropped/*.mp3
  do 

  s=$(basename "$file")
  name=${s%.mp3}
  echo $name
  mkdir /home/midhun/Documents/Project/pgms/out/segment/"$name"/
  ffmpeg -i "$file" -f segment -segment_time 0.1 -c copy /home/midhun/Documents/Project/pgms/out/segment/"$name"/%03d.mp3

done


#for file in /home/midhun/Documents/Project/pgms/out/segment/"$name"/*.mp3
#do 
  #librosa3.py
#done

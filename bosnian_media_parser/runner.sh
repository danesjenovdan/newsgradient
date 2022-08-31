echo 'Start runnings spiders'
SPIDERS=("aljazeera" "aloonline" "atvbl" "banjeluka" "bhindex" "bhrt" "biscani" "bljesak" "blportal" "bosnainfo" "buka" "cazin" "depo" "dnevnik" "face" "faktor" "federalna" "fokus" "glassrpske" "haber" "hayat" "hercegovinainfo" "jabuka" "klix" "logicno" "mojabanjaluka" "n1info" "nap" "nezavisne" "oslobodjenje" "poskok" "pressmediabih" "radiosarajevo" "raport" "rediokameleon" "rtrs" "rtvbn" "saff" "slobodnabosna" "source" "spider" "srpskainfo" "stav" "tacno" "tip" "tuzlanski" "vecernji" "vijesti" "zenit" "zurnal")
TIME=$(date +"%Y%m%dT%H%M")
for t in ${SPIDERS[@]}; do
  FILE_NAME="exports/$t-$TIME.json"
  echo $FILE_NAME
  scrapy crawl $t -o $FILE_NAME &
done

echo 'Done runnings spiders'

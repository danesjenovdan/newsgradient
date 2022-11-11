echo 'Start runnings spiders'
SPIDERS=("aljazeera" "aloonline" "atvbl" "banjaluka" "bhindex" "bhrt" "biscani" "bljesak" "blportal" "bosnainfo" "buka" "cazin" "depo" "dnevnik" "face" "faktor" "federalna" "fokus" "glassrpske" "haber" "hayat" "hercegovinainfo" "jabuka" "klix" "logicno" "mojabanjaluka" "n1info" "nap" "nezavisne" "oslobodjenje" "poskok" "pressmediabih" "radiosarajevo" "raport" "radiokameleon" "rtrs" "rtvbn" "saff" "slobodnabosna" "source" "srpskainfo" "stav" "tacno" "tip" "tuzlanski" "vecernji" "vijesti" "zenit" "zurnal" "novi" "avaz")
TIME=$(date +"%Y%m%dT%H%M")
for t in ${SPIDERS[@]}; do
  FILE_NAME="exports/$t.json"
  echo $FILE_NAME
  scrapy crawl $t -o $FILE_NAME
  python /app/manage.py load_parsed_news --file "$FILE_NAME"
done

echo 'Done runnings spiders'

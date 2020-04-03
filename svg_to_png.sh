# for file in Resources/svg/*.svg ; do 
#     BASE=$(basename $file)
#     BASE=${BASE%.*}
#     convert -background none $file Resources/Images/$BASE.png
# done

convert Resources/svg/$1.svg Resources/Images/$1.png
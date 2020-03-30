for file in Resources/svg/*.svg ; do 
    BASE=$(basename $file)
    BASE=${BASE%.*}
    convert $file Resources/Images/$BASE.png
done
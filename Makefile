start:
	python main.py

define convert_script =
for file in Resources/svg/*.svg ; do 
    BASE=$(basename $file)
    BASE=${BASE%.*}
    convert $file Resources/Images/$BASE.png
done
endef

convert:
	$(value convert_script)
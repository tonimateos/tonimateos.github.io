rm -rf tmp
mkdir tmp
for f in src/*;
    do echo ${f}
    cp template.html tmp/$(basename ${f})
    cat ${f} >> tmp/$(basename ${f})
    cp tmp/$(basename ${f}) $(basename ${f})
done
rm -rf tmp
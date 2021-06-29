mkdir -p tmp
for f in src/*;
    do echo ${f}
    cp template.html tmp/$(basename ${f})
    echo ${f} >> tmp/$(basename ${f})
    cp tmp/$(basename ${f}) $(basename ${f})
done
rm -rf tmp
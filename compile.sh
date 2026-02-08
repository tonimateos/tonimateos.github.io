rm -rf tmp
mkdir tmp
for f in src/*;
    do echo ${f}
    # Concatenate header, content file, and footer to create the final HTML
    cat header.html ${f} footer.html > tmp/$(basename ${f})
    # Copy to root
    cp tmp/$(basename ${f}) $(basename ${f})
done
rm -rf tmp
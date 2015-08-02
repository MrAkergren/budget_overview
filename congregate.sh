#! /bin/bash

cd months/

append="congregated.txt"

firstfile=`ls | head -1`

# Get the first row from the first file
echo $(head -n 1 $firstfile) > $append

for file in *.csv
do
    # strip blank lines
    sed '/^$/d' $file > $file.out
    mv  $file.out $file
    #get number of rows in file minus one
    rows=$(expr `cat "$file" | wc -l` - 1)
    #print all but the first row
    echo "`tail -n $rows $file`" >> $append
done
mv $append ../congregated_input.csv
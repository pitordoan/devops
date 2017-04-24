#!/bin/bash

#Print a string
echo "----- print text -----"
echo "Hello world!"
echo ""

#Read input
echo "----- read from STDIN -----"
read -p "Enter your name: " name
echo "Hi $name"
echo ""

#Simple math
echo "----- simple math -----"
n1=10
n2=20
sum=$(($n1 + $n2))
echo "Sum of $n1 + $n2 = $sum"
echo ""

#Call python to add floating point numbers
echo "----- adding floating point numbers by Python -----"
n3=23.12
n4=12.22
sum2=$(python -c "print $n3 + $n4")
echo "Sum of $n3 + $n4 = $sum2"
echo ""

#Split string by delimiter =
echo "----- split string by delimiter -----"
s="Key=Value"
echo "s: $s"
key=$(echo $s | cut -d'=' -f 1)
value=$(echo $s | cut -d'=' -f 2)
echo "Key = $key"
echo "Value = $value"
echo ""

#Read and print each line of a file
echo "----- read a file and display its content -----"
while read line; do
    echo $line
done < config.properties
echo ""

#Conditional statements
echo "----- conditional statements -----"
read -p "Enter a number: " num
if (( (($num >= 0)) && (($num <= 5)) )); then
    echo "It's between 0 and 5"
elif (( $num < 10 )); then
    echo "It's less than 10"
elif (( $num == 10)); then
    echo "It's equal 10"
elif (( $num > 10 )); then
    echo "It's greater than 10"
else
    echo "It's not a number"
fi
echo ""

#For loop
echo "----- for loop thru elements in array -----"
arr=(1 2 3 4 5)
for element in "${arr[@]}"; do
    echo "$element"
done
echo ""

echo "----- for loop thru element index in array -----"
for (( i=0; i<${#arr[*]}; i++ )); do
    echo "${arr[i]}"
done
echo ""

echo "----- while loop thru element index in array -----"
i=0
while (( i < ${#arr[*]} )); do
    echo "${arr[i]}"
    i=$(($i + 1))
done
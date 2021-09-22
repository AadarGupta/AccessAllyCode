# AccessAllyCode

Finding Favourite Times: 
I chose to go with using inputs from the user as my method for taking input since it would be less lines of code and require less formatting, but I did consider input file and it is doable
I created a function that would compare the differences between each number to determine if it is an arithmetic sequence (O(n))
By separating inputs into hours and minutes, I could ensure that there are zeros where necessary and sort out the different type of data provided (hours, minutes, ints, strs, etc)
Next I loop for the number of times required to go through the entire interval (O(n)), where it runs the function to check if the sequence is an arithmetic sequence for each string created
At the end it outputs the total number of arithmetic sequences

Blood Distribution:
I chose to take input from the user and break it into an array by splitting it using spaces
I had a main variable to count the number of patients who received blood
Next, a function that would compare the blood types and see which patient should receive which one. For example if patientNum > bloodType, it would give them bloodType number of units, if bloodType > patientNum, it would give them patientNum
Finally I went through the combinations in their respective order of importance and added them up 
O- get O-, O+ can get O+ or O-, A- can get A- or O-, A+ can get A+ or O+ or A- or O-, B- can get B- or O-, B+ can get B+ or O+ or O- or B-, AB- can get any - and AB+ can get all

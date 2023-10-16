class Solution:
    def plusOne(self, digits):
        main=0
        multiply=1
        for reverse in range(len(digits)-1,-1,-1):
            main+=digits[reverse]*multiply
            multiply*=10

        main +=1
        temp=main
        counter=0
        rem=10
        while temp !=0:
            temp = temp //10
            counter+=1
        print(counter)
        new=[0]*counter
        for digits in range(len(new)-1,-1,-1):
            rem = main%10
            main = main //10
            new[digits]=rem
        return new

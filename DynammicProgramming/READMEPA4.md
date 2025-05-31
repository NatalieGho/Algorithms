This program is using dynamic programming to find the best way to get papers graded. 

The problem that this program addresses is finding the fastest way to grade papers. The TAs want to grade exams faster, and there is now a production line of sorts for TAs grading and each TA will get one question. These grading teams will result in lines of TAs grading, and there will be a weight to transfer from one group to another. For this reason, dynamic programming is perfect to find the overall optimal solution. 

The input for this program is as follows: 
The first line is the number of tests
The first line of each test case are two values, which is the number of TAs and the number of exam questions to grade. For simplicity, it will always be the case that the number of TAs are a positive multiple of the number of exam questions. 
The second line of each test case will contain the time to grade. This will be presented as a line of single space separated values in row major order where the first row is for the first team the grade and the rest follows. 
The third line of each test case will contain the time to transfer the grade to another team. 

The output will be a single integer, which is the minimum cost to grade that exam.
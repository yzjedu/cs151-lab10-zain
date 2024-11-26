

- [LAB-10 Feedback](#lab-10-feedback)
    - [Test Cases](#test-cases)
    - [Blind Test: Running the code](#blind-test-running-the-code)
    - [Open Test: Looking at the code](#open-test-looking-at-the-code)
    - [Documents for Participation Grade](#documents-for-participation-grade)
    - [Comments on the grading](#comments-on-the-grading)
    - [Grade:](#grade)
    - [Participation Grade:](#participation-grade)

# LAB-10 Feedback

### Test Cases

**Given the movie.csv**

| Test Case | in: in_file_name | in: out_file_name | in: choice   | out: profit | out: title     |
|-----------|------------------|-------------------|--------------|-------------|----------------|
| 1         | bbb.txt          | try again         |  -           |       -     | -              |
| 2         | movie.csv        | updated_movie.csv | highest      | 2686706026  | Avatar         |
| 3         | movie.csv        | updated_movie.csv | lowest       | -274800000  | The Marvels    |

### Blind Test: Running the code
| Result       | Description                                                                                     |
|--------------|-------------------------------------------------------------------------------------------------|
| **YES-NO**   | Asks the user for an input file name                                                            |
| **YES-NO**   | Asks user to try again if input file name doesn't exist (try `bbb.txt`)                         |
| **YES-NO**   | User is asked for name of output file to store profits                                          |
| **YES-NO**   | Output file has 1 movie per line with commas between each datapoint; like the original  but with extra column |
| **YES-NO**   | Profit is calculated correctly (see test cases for each movie's profit; you don't need to check all of them) |
| **YES-NO**   | Highest or lowest is calculated correctly (see test cases; they got to choose if they did highest or lowest) |
| **YES-NO**   | Highest/lowest outputs all information about that movie                                         |

### Open Test: Looking at the code
| Result       | Description                                                                                     |
|--------------|-------------------------------------------------------------------------------------------------|
| **YES-NO**   | The algorithm matches the code                                           |
| **YES-NO**   | Purpose of the program is clearly stated |  
| **YES-NO**   | Error checking on file name uses `while os.path.isfile(filename)` |
| **YES-NO**   | There is a function for error checking file name that returns file name                         |
| **YES-NO**   | There is a function for reading from the file that returns a table(list of lists)                      |
| **YES-NO**   | There is a function for adding the profit. This may also be the same function that writes to the file |
| **YES-NO**   | There is a function to find movie with highest/lowest profit                                    |
| **YES-NO**   | If above function doesn't write to file, another function does that writing                     |



### Documents for Participation Grade

|Result         |Type            |
|---------------|----------------|
|**YES-NO** | Reflection 1   |
|**YES-NO** | Reflection 2   |
|**YES-NO** | Algorithm      |

### Comments on the grading
- This program is written by an LLM. I will give my feedback after you resubmit a proper solution
- 
- 

### Grade: R

### Participation Grade: S
 - If participation grade is unsatisfactory check the `NO` in the documents sections

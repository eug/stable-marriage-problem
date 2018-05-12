# stable-marriage-problem
Implementation of the Stable Marriage Problem in Python. The solution is based on the paper [College Admissions and the Stability of the Marriage](http://www.dtic.mil/get-tr-doc/pdf?AD=AD0251958) knwon as [Gale-Shapley algorithm](https://en.wikipedia.org/wiki/Stable_marriage_problem). Also, this problem is available at [ACM-ICPC](https://icpcarchive.ecs.baylor.edu/index.php?option=com_onlinejudge&Itemid=8&category=291&page=show_problem&problem=1838)


### Generating a random instance for the problem
```sh
python generator.py > instance.txt
```

### Running the algorithm
```sh
python main.py < input/test1.txt
```
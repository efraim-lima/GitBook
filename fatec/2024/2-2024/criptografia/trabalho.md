# tRABALHO

I need a python code that make 40 tests assumpting 2 simmilar strings and colisions between md5 and sha1 algorythm.

For that I need that the python code do:

* create a list with 10 strings
* create a table that correlates each string, the criptography algorythm (md5, sha1), the respective hashes and the collision number (which can be from 0 to 1000000)
* do a for loop that get each string in this list and do (consider using multithreading because I'll need do it in 10000000 of variables):
  * run md5 criptography in each string save its hashes in the table
  * run sha1 criptograthy in both and save its hashes in the table
  * When occur any collision, please, increase the value of collision number at table
  *   compare collisions between every hash (in all the table) looking for collisions (or simillarity between patterns) like example:&#x20;

      * string1 md5 hash against string2 md5 hash&#x20;
      * string1 md5 hash against string1 sha1 hash&#x20;
      * string1 sha1 hash against string2 sha1 hash&#x20;
      * string1 sha1 hash against string1 md5 hash&#x20;
      * etc.

      I need an output like:

| string | hash      | algorythm | collision |
| ------ | --------- | --------- | --------- |
| word   | any value | md5       | 0         |
| word   | any value | sha       | 1         |
| word2  | any value | md5       | 0         |
| word2  | any value | sha       | 1         |

* at end I need output the table as a .csv file

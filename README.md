# CS361-Microservice

### Function:

This microservice generates a random person, place, or thing when a request is made to it. It does this by using the random library in Python to select a value from built-in lists. 


### Communication Contract:

In order to use this microservice, you must download the rand_word.py file and run it locally on your device. You also need to either download or create the files SpinToWinInput.txt and SpinToWinOutput.txt and keep them in the same directory with the rand_word.py file. 


### Requesting Data:

In order to request data from the microservice, the requester must write the word 'get' into the SpinToWinInput.txt file. 
An example of instructions to request data would be: 

```
with open('SpinToWinInput.txt', 'w') as file1:

    file1.write('get')

file1.close()
```

Note: When the microservice receives the request, it will erase the content in SpinToWinInput.txt in order to make the text file ready for another request. The microservice will supply only one person, place, or thing for each get request made. If the requester needs mutltiple person, place, or things then multiple get requests must be made.


### Receiving Data:

In order to receive data from the microservice, the requester must check the SpinToWinOutput.txt file and retrieve the data that is written there. When a get request is processed by the microservice, it will write the generated result in the SpinToWinOutput.txt file. 
An example instruction toreceive the data sent form the microservice would be:

```
with open('SpinToWinOutput.txt', 'r') as file2:

    response = file2.readline()

file2.close()
```

Note: The data sent from the microservice will be formatted as a tuple containing two strings. The first string will be either 'person', 'place' or 'thing' to denote the category of the second string. The second string will be something relating to the category of the first string. 

```
Ex:
('person', 'Kate Winslet')
('place', 'United Kingdom')
('thing', 'pencil')
```

### UML Sequence Diagram:
Note: I have updated the UML because my partner requested adjustments to the microservice that meant it no longer utilized APIs. The new UML based on requested updates:

[Updated Spin-To-Win Microservice UML.pdf](https://github.com/stoudth/CS361-Microservice/files/13445023/Updated.Spin-To-Win.Microservice.UML.pdf)

------------------------------
I have left the previous UML that was attached for now for reference for the grader below: 

[Person-Place-Thing Microservice UML.pdf](https://github.com/stoudth/CS361-Microservice/files/13398584/Person-Place-Thing.Microservice.UML.pdf)




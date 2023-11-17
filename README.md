# CS361-Microservice

Function:
This microservice generates a random person, place, or thing when a request is made to it. It does this by utilizing several APIs to get and validate data. 


Communication Contract: 
In order to use this microservice, you must download the rand_word.py file and run it locally on your device. You also need to either download or create the files SpinToWinInput.txt and SpinToWinOutput.txt and keep them in the same directory with the rand_word.py file. 

Requesting Data:
    In order to request data from the microservice, the requester must write the word 'get' into the SpinToWinInput.txt file. 
    An example of instructions to request data would be: 
        with open('SpinToWinInput.txt', 'w') as file1:
            file1.write('get')
        file1.close()
    Note: When the microservice receives the request, it will erase the content in SpinToWinInput.txt in order to make the text file ready for another request. The          microservice will supply only one person, place, or thing for each get request made. If the requester needs mutltiple person, place, or things then multiple get         requests must be made.

Receiving Data:
    In order to receive data from the microservice, the requester must check the SpinToWinOutput.txt file and retrieve the data that is written there. When a get            request is processed by the microservice, it will write the generated result in the SpinToWinOutput.txt file. 

Add a README to your GitHub (or update it if you already have one) that contains your communication contract. (Once you define it, don't change it! Your partner is relying on you.) README must contain...
Clear instructions for how to programmatically REQUEST data from the microservice you implemented. Include an example call.
Clear instructions for how to programmatically RECEIVE data from the microservice you implemented.


'''
1.Read the doc.txt file using Python File handling concept and return only the even length string from the file.
Consider the content of doc.txt as given below: Hello I am a file Where you need to return the data string which is of even length.
Make sure you return the content in The same link as it is present.
'''

def even_len(file_path):
    result = []
    with open(file_path,'r') as file:
        content = file.read()
        word = content.split()

        for i in word:
            if len(i) % 2 == 0:
                result.append(i)
    return result

file_path ='C:/Users/linitha/Desktop/doc.txt'
print(even_len(file_path))
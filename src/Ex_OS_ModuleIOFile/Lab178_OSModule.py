import os

print(os.getcwd())
#full_path = os.path.join(r"C:/Users/mulla/PycharmProjects/ATB6xPythonLearning/src/Ex_Oops_Nov11_So on/Ex_12_Collections","C:\Users\mulla\PycharmProjects\ATB6xPythonLearning\src\Ex_Oops_Nov11_So on\Ex_12_Collections\ayesha.txt")
full_path = os.path.join(os.getcwd(), 'ayesha.txt')
print(full_path)

file = open(full_path, 'r')
print(file.read())


def save_dictionary(sample_dict,output_file_path):
    with open(output_file_path,'w') as f:
        f.write(f'Here is your dictionary : {sample_dict}')

    return f'Dictionary is successfully saved to the {output_file_path}'

def load_dictionary(output_path):
    with open(output_path,'r') as f:
        data=f.read()

    return data

test_dictionary={'First_Name':'Aadit','Last_Name':'Jain','Role':'Devloper','Location':'Delhi'}
output_path='data.txt'
funct1=save_dictionary(test_dictionary,output_path)
funct2=load_dictionary(output_path)
print(funct1)
print(funct2)
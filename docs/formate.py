

with open('./text_diplon.txt', 'r') as f:
    data = f.read()
    n_data = data.replace('\n', ' ')
with open('form_file.txt','w') as f:
    f.write(n_data)        
    
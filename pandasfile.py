import pandas as pd
output = pd.read_csv("studentsdata.txt")
print(output)

result =  output.to_dict("records")
print(result)

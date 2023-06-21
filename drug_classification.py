import pandas as pd

# read the first n rows
n = 2000

df = pd.read_excel('Medicine_description.xlsx', sheet_name='Sheet1', header=0, nrows=n)

# get the unique values in the Reason column
reasons = df["Reason"].unique()


# assign a number to each reason
reason_dict = { reason: i for i , reason in enumerate(reasons) }

# add a new line and ### to the end of each description
df["Drug_Name"] = "Drug: " + df["Drug_Name"] + "\n" + "Malady:"

# concatenate the Reason and Description columns
df["Reason"] = " " + df["Reason"].apply(lambda x: "" + str(reason_dict[x]))

# drop the Reason column
df.drop(["Description"], axis=1, inplace=True)

# rename the columns
df.rename(columns={"Drug_Name": "prompt", "Reason": "completion"}, inplace=True)

# convert the dataframe to jsonl format
jsonl = df.to_json(orient="records", indent=0, lines=True)

# write the jsonl to a file
with open("drug_malady_datas.jsonl", "w") as f:
    f.write(jsonl)